from core.database_connection import db
from flask import jsonify
from flask import Response
import json
from MySQLdb._exceptions import IntegrityError


class UserDAO(object):
    """Data access object for User."""

    def __init__(self):
        """Init with connection database imported"""

        self.connection = db

    @property
    def users(self):
        """Call internal method to get user.

        Return: list()
            All users from database
        """
        return self._get_users()

    def _get_users(self):
        """Internal method to get all users from database."""

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user;")
        data = cursor.fetchall()

        # get column names of user table from database.
        cursor.execute("""SELECT COLUMN_NAME FROM information_schema.columns 
                            WHERE table_schema='captalys' AND table_name='user'""")
        column = cursor.fetchall()
        # get data outside tuples
        column = [i[0] for i in column]
        # zip columns and values
        data = [dict(zip(column, list(i))) for i in data]

        return data

    def create(self, data):
        """Insert into database user."""

        cursor = self.connection.cursor()
        # prepare sql query to insert user
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO user({columns}) VALUES({placeholders})"
        try:
            cursor.execute(sql, list(data.values()))
            self.connection.commit()
            return jsonify(success=True)
        except Exception as e:
            # if IntegrityError cause by duplicated.
            # then call update method.
            if isinstance(e, IntegrityError):
                self.update(data)

    def update(self, data):
        """Update user into database."""

        cursor = self.connection.cursor()
        # prepare update set query
        set_query = ""
        for k, v in data.items():
            # in case values is boolean convert to int and then to string
            if isinstance(v, bool):
                set_query += k + '=' + str(int(v)) + ", "
            # every else convert to string
            else:
                set_query += k + '=' + "'" + str(v) + "'" + ", "
        sql = f"UPDATE user set {set_query[:-2]} where id={data['id']}"
        try:
            print(sql)
            cursor.execute(sql)
            self.connection.commit()
            return jsonify(success=True)
        except Exception as e:
            print(e)
