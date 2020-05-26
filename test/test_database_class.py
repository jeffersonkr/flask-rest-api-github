from core.database_connection import Database
from unittest.mock import MagicMock, patch
import pytest
import MySQLdb


@pytest.fixture
def database():
    database = Database(
        user='db', passwd='secret',
        db='db', host='host', port=3306
    )
    yield database


def test_receiving_params_to_connect_database(database):
    with patch('MySQLdb.connect') as mock_db:
        mock_db.side_effect = lambda **x: x
        conn = database._connect_database()
        assert conn == {'user': 'db', 'passwd': 'secret',
                        'db': 'db', 'host': 'host', 'port': 3306}


def test_method_execute_and_commit_and_close_connection_and_cursor(database, capsys):
    with patch('MySQLdb.connect') as conn:
        database._close_conn_and_cursor = MagicMock()
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        cursor.commit.side_effect = print('commited')
        database.execute_query_commit('some query')
        cursor.execute.assert_called_once_with('some query')
        database._close_conn_and_cursor.assert_called_once()
        capture = capsys.readouterr().out
        assert 'commited' and 'some query' in capture


def test_method_execute_and_commit_raising_error(database):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = Exception()
        with pytest.raises(Exception):
            database.execute_query_commit('some query')


def test_method_execute_and_fetchall_and_close_connection_and_cursor(database, capsys):
    with patch('MySQLdb.connect') as conn:
        database._close_conn_and_cursor = MagicMock()
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        cursor.fetchall.return_value = ('some data fetched')
        data = database.execute_query_fetchall('some query')
        cursor.execute.assert_called_once_with('some query')
        capture = capsys.readouterr().out
        database._close_conn_and_cursor.assert_called_once()
        assert 'some query' in capture
        assert data == ('some data fetched')


def test_method_execute_and_fetchall_raising_error(database):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = Exception()
        with pytest.raises(Exception):
            database.execute_query_fetchall('some query')
