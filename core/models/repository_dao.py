from MySQLdb._exceptions import IntegrityError
from flask import jsonify
from flask import Response
import json

from core.database_connection import db


class RepositoryDAO(object):
    """Data access object for repository."""

    def __init__(self):
        """Init with connection database imported"""

        self.connection = db

    def get(self, user_id):
        """
        Params:
            user_id: int()
                github user's id.
        Return:
            list with user's repositories.
        """

        query = f"SELECT * from repository where owner={user_id}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return [i for i in cursor.fetchall()]

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

        cursor = self.connection.cursor()

        # cria se a query para inserir no banco de dados
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"""INSERT INTO repository({columns}) VALUES({placeholders});"""
        try:
            cursor.execute(sql, list(data.values()))
            self.connection.commit()
            return jsonify(success=True)
        except Exception as e:
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

        cursor = self.connection.cursor()
        # prepara query de update
        set_query = ""
        for k, v in data.items():
            # caso valor seja bolean converte para o boolean
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
            cursor.execute(sql)
            self.connection.commit()
            return jsonify(success=True)
        except Exception as e:
            print(e)
