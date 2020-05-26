import pytest
import json
from unittest.mock import patch, MagicMock

from app import app
from core.database_connection import Database
from core.models.user_dao import UserDAO
from core.models.repository_dao import RepositoryDAO
from test.FakeRequest import FakeRequest


@pytest.fixture(scope='session')
def client():
    app.testing = True
    client = app.test_client()
    yield client


@patch.object(UserDAO, '_get_users', MagicMock(return_value=(())))
def test_get_users_route(client):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        r = client.get('users/')
        assert '[]' in r.data.decode('utf-8')


def test_get_user_by_id_if_not_numeric_abort_400(client):
    r = client.get('users/asdd')
    assert r.status == '400 BAD REQUEST'


@patch.object(UserDAO, 'get_user_by_id', MagicMock(return_value=()))
def test_get_user_by_id_if_not_found(client):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        r = client.get('users/123')
        assert r.status == '404 NOT FOUND'


@patch.object(UserDAO, 'get_user_by_id', MagicMock(return_value=((123, 'jose'),)))
@patch.object(RepositoryDAO, 'get', MagicMock(return_value=((321, 'repos_test'),)))
@patch.object(UserDAO, 'get_columns_name', MagicMock(return_value=['id', 'nome']))
@patch.object(RepositoryDAO, 'get_columns_names', MagicMock(return_value=['id', 'nome']))
def test_get_details_users_and_repositories_route(client):
    with patch('MySQLdb.connect') as conn:
        cursor = conn().cursor.return_value
        r = client.get('users/123')
        response_data = json.loads(r.data.decode('utf-8'))
        assert_data = {
            "user": {
                "id": 123,
                "nome": "jose"
            },
            "repositories": [{
                "id": 321,
                "nome": "repos_test"
            }]
        }
        assert assert_data == response_data


def test_get_public_repository_detail_user_repos_not_found(client):
    with patch('requests.get') as req:
        req.return_value = FakeRequest(status_code=404)
        r = client.get('repos/detail_repository/jose/repos_test')
        r_status = json.loads(r.data.decode('utf-8'))['status']
        assert r_status == 404


@patch.object(UserDAO, 'create', MagicMock())
@patch.object(RepositoryDAO, 'create', MagicMock())
def test_get_public_repository_detail(client):
    with patch('requests.get') as req:
        req.return_value = FakeRequest(data={'owner': ''})
        r = client.get('repos/detail_repository/jose/repos_test')
        r_status = json.loads(r.data.decode('utf-8'))
        assert r_status == {'owner': ''}


def test_get_public_repository_user_not_found(client):
    with patch('requests.get') as req:
        req.return_value = FakeRequest(status_code=404)
        r = client.get('repos/public_repository/jose')
        r_status = json.loads(r.data.decode('utf-8'))['status']
        assert r_status == 404


@patch.object(UserDAO, 'create', MagicMock())
@patch.object(RepositoryDAO, 'create', MagicMock())
def test_get_public_repository(client):
    with patch('requests.get') as req:
        req.return_value = FakeRequest(
            data=[{'id': 123, 'full_name': 'jose/repos_test'}])
        r = client.get('repos/public_repository/jose')
        r_status = json.loads(r.data.decode('utf-8'))
        assert r_status == {'list_repository_name': ['repos_test']}
