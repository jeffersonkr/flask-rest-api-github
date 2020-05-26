import pytest
from core.models.user_dao import UserDAO
from unittest.mock import patch, MagicMock
from MySQLdb._exceptions import IntegrityError


@pytest.fixture
def user_dao():
    yield UserDAO()


@patch.object(UserDAO, '_get_users', MagicMock())
def test_property_users(user_dao):
    user_dao.users
    user_dao._get_users.assert_called_once()


def test_private_get_users(user_dao):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.fetchall.return_value = (('s'))
        users = user_dao._get_users()
        assert users == [{'s': 's'}]


def test_get_columns_name_method(user_dao):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.fetchall.return_value = (('nome',), ('id',))
        column = user_dao.get_columns_name()
        assert column == ['nome', 'id']


def test_get_user_by_id(user_dao):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.fetchall.return_value = (('josue', 123))
        user = user_dao.get_user_by_id(123)
        assert user == ('josue', 123)


def test_insert_user_to_database(user_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        user_dao.create({'id': 123, 'name': 'jose'})
        capture = capsys.readouterr().out
        assert "INSERT INTO user(id, name) VALUES(123, 'jose')" in capture


def test_insert_user_to_database_duplicated_exception_then_update(user_dao):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = IntegrityError()
        user_dao.update = MagicMock()
        user_dao.create({'id': 123, 'name': 'jose'})
        user_dao.update.assert_called_once()


def test_update_user(user_dao, capsys):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        cursor.execute.side_effect = print
        user_dao.update({'id': 123, 'name': 'jose'})
        capture = capsys.readouterr().out
        assert "UPDATE user set id=123, name='jose' where id=123" in capture
