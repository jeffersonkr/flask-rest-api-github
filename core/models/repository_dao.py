from MySQLdb._exceptions import IntegrityError
from flask import jsonify
from flask import Response
import json

from core.database_connection import Database


class RepositoryDAO(object):
    """Data access object for repository."""

    def __init__(self):
        """Init with connection database imported"""

        self._connection = Database()

    def get(self, user_id):
        """
        Params:
            user_id: int()
                github user's id.
        Return:
            list with user's repositories.
        """

        query = f"SELECT * from repository where owner={user_id}"
        data = self._connection.execute_query_fetchall(query)
        return [i for i in data]

    def create(self, data):
        """
        First extract and transform data to fit database
        then insert into a database repository data.
        If already exist call update method.

        Params:
            data: json()
                data containing repository information,
                fetched from github api.
        Return:
            return jsonify(sucess=True)
        """

        # necessitamos apenas do id do owner
        data['owner'] = data['owner']['id']

        # apenas precisamos do nome da licença
        data['license'] = data['license']['name'] \
            if data.get('license') else ""

        # necessitamos apenas do url do organization
        data['organization'] = data['organization']['organizations_url'] \
            if data.get('organization') else ""

        # necessitamos apenas do id do parent
        data['parent'] = data['parent']['id'] \
            if data.get('parent') else None

        # necessitamos apenas do id do source
        data['source'] = data['source']['id'] \
            if data.get('source') else None

        # cria se a query para inserir no banco de dados
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
        sql = f"""INSERT INTO repository({columns}) VALUES({values});"""
        try:
            self._connection.execute_query_commit(sql)
            return jsonify(success=True)
        except Exception as e:
            print(e)
            # Caso de erro de integridade sabe-se
            # que é erro de duplicidade por isso
            # enviamos chamamos o update
            if isinstance(e, IntegrityError):
                self.update(data)

    def update(self, data):
        """Update repository info.

        Params:
            data: json()
                data containing repository information,
                fetched from github api.
        Return:
            return jsonify(sucess=True)
        """

        # prepara query de update
        set_query = ""
        for k, v in data.items():
            # caso valor seja bolean converte o boolean
            # para inteiro e depois para string
            if isinstance(v, bool):
                set_query += k + '=' + str(int(v)) + ", "
            # caso valor seja None insere NULL no lugar
            elif v is None:
                set_query += k + '=' + "NULL" + ", "
            # outros casos converte em strings
            else:
                set_query += k + '=' + "'" + str(v) + "'" + ", "
        # set_query[:-2] para remover o ultima virgula e espaço adicionado.
        sql = f"UPDATE repository set {set_query[:-2]} where id={data['id']}"
        try:
            self._connection.execute_query_commit(sql)
            return jsonify(success=True)
        except Exception as e:
            print(e)

    def get_columns_names(self):
        """Get columns name from table repository."""

        query = """SELECT COLUMN_NAME FROM information_schema.columns
                    WHERE table_schema='captalys' AND table_name='repository'"""
        columns = self._connection.execute_query_fetchall(query)
        columns = [i[0] for i in columns]

        return columns
