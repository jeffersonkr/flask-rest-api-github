from flask import jsonify
from flask import Response
import json
from MySQLdb._exceptions import IntegrityError

from core.database_connection import Database


class UserDAO(object):
    """Data access object for User."""

    def __init__(self):
        """Init with connection database imported"""

        self._connection = Database()

    @property
    def users(self):
        """Call internal method to get user.

        Return: list()
            All users from database
        """
        return self._get_users()

    def _get_users(self):
        """Internal method to get all users from database."""

        query = "SELECT * FROM user;"
        data = self._connection.execute_query_fetchall(query)

        # get column names of user table from database.
        query = ("""SELECT COLUMN_NAME FROM information_schema.columns
                            WHERE table_schema='captalys' AND table_name='user'""")
        column = self._connection.execute_query_fetchall(query)

        # get data outside tuples
        column = [i[0] for i in column]
        # zip columns and values
        data = [dict(zip(column, list(i))) for i in data]

        return data

    def create(self, data):
        """Insert into database user."""

        # prepare sql query to insert user
        columns = ', '.join(data.keys())

        def tratamento(x):
            if isinstance(x, bool):
                return str(x).upper()
            elif x is None:
                return "NULL"
            elif isinstance(x, int):
                return str(x)
            else:
                return "'"+str(x)+"'"

        dados_list = list(data.values())
        values = ", ".join(list(map(tratamento, dados_list)))

        sql = f"INSERT INTO user({columns}) VALUES({values})"

        try:
            self._connection.execute_query_commit(sql)
            return jsonify(success=True)
        except Exception as e:
            # if IntegrityError cause by duplicated.
            # then call update method.
            if isinstance(e, IntegrityError):
                self.update(data)

    def update(self, data):
        """Update user into database."""

        # prepare update set query
        set_query = ""
        for k, v in data.items():
            if isinstance(v, bool):
                set_query += k + '=' + str(v).upper() + ", "
            elif v is None:
                set_query += k + '=' + "NULL" + ", "
            elif isinstance(v, int):
                set_query += k + '=' + str(v) + ", "
            else:
                set_query += k + '=' + "'"+str(v)+"'" + ", "

        sql = f"UPDATE user set {set_query[:-2]} where id={data['id']}"

        try:
            self._connection.execute_query_commit(sql)
            return jsonify(success=True)
        except Exception as e:
            print(e)
