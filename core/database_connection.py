import MySQLdb


class Database:
    """A simple wrapper for MySQLdb."""

    def __init__(self, user="root", passwd="secret", db="captalys", host="database", port=3306):
        """
        Params:
            user: str()
                username for database
            passwd: str()
                password for database
            db: str()
                database's name
            host: str()
                ip address or name for database
            port: int()
                port for database
        """

        self._user = user
        self._passwd = passwd
        self._db = db
        self._host = host
        self._port = port

    def _connect_database(self):
        """Internal method to create a new connection with database."""
        conn = MySQLdb.connect(
            user=self._user,
            passwd=self._passwd,
            db=self._db,
            host=self._host,
            port=self._port
        )
        return conn

    def _close_conn_and_cursor(self, conn, cursor):
        """Internal method to close connection and cursor"""

        cursor.close()
        conn.close()

    def execute_query_commit(self, query):
        """Open a new connection and a cursor, execute 
        query, commit then close cursor and connection.
        """

        conn = self._connect_database()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            self._close_conn_and_cursor(conn, cursor)

    def execute_query_fetchall(self, query):
        """Open a new connection and a cursor, execute 
        query, fetchall then close cursor and connection.

        Return: fetched data from database
        """

        conn = self._connect_database()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            self._close_conn_and_cursor(conn, cursor)

        return data
