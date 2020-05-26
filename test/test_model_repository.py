import pytest
from core.models.repository_dao import RepositoryDAO
from unittest.mock import patch, MagicMock
from MySQLdb._exceptions import IntegrityError


@pytest.fixture
def repos_dao():
    yield RepositoryDAO()


def test_get_repos_from_database_by_user_id(repos_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        cursor.fetchall.return_value = ((123, 'repos_test'))
        data = repos_dao.get(1)
        capture = capsys.readouterr().out
        assert "SELECT * from repository where owner=1" in capture
        assert data == [123, 'repos_test']


def test_create_repos(repos_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        data = repos_dao.create({'owner': {'id': 213}})
        capture = capsys.readouterr().out
        assert "INSERT INTO repository(owner, license, organization, parent, source)" in capture


def test_create_repos_ducplicated_exception_then_update(repos_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = IntegrityError()
        repos_dao.update = MagicMock()
        repos_dao.create({'owner': {'id': 123}})
        repos_dao.update.assert_called_once()


def test_update_user(repos_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        repos_dao.update({'owner': {'id': 123}, 'id': 111})
        capture = capsys.readouterr().out
        assert "UPDATE repository set owner='{'id': 123}', id='111' where id=111" in capture


def test_get_columns_name_method(repos_dao):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.fetchall.return_value = (('nome',), ('id',))
        column = repos_dao.get_columns_names()
        assert column == ['nome', 'id']
