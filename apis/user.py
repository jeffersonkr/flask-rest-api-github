from flask_restplus import Namespace, Resource, fields
from core.models.user_dao import UserDAO
from core.models.repository_dao import RepositoryDAO

api = Namespace('User', description='github user operations')

user = api.model('User', {
    'avatar_url': fields.String(required=True, description="Avatar url"),
    'bio': fields.String(required=True, description="User bio"),
    'blog': fields.String(required=True, description="User blog"),
    'company': fields.String(required=True, description="User company"),
    'created_at': fields.DateTime(required=True, description="Created at"),
    'email': fields.String(required=True, description="User email"),
    'events_url': fields.String(required=True, description="User bio"),
    'followers': fields.Integer(required=True, description="total of followers"),
    'followers_url': fields.String(required=True, description="Followers url"),
    'following': fields.Integer(required=True, description="total of following"),
    'following_url': fields.String(required=True, description="Following url"),
    'gists_url': fields.String(required=True, description="gists url"),
    'gravatar_id': fields.String(required=True, description="gravatar id"),
    'hireable': fields.Boolean(required=True, description="hireable"),
    'html_url': fields.String(required=True, description="Followers url"),
    'id': fields.Integer(required=True, description='Github username id'),
    'location': fields.String(required=True, description="User location"),
    'login': fields.String(required=True, description='Username to github'),
    'name': fields.String(required=True, description="Name"),
    'node_id': fields.String(required=True, description="node_id"),
    'organizations_url': fields.String(required=True, description="organizations_url"),
    'public_gists': fields.String(required=True, description="public_gists"),
    'public_repos': fields.String(required=True, description="public_repos"),
    'received_events_url': fields.String(required=True, description="received_events_url"),
    'repos_url': fields.String(required=True, description="repos_url"),
    'site_admin': fields.Boolean(required=True, description="site admin"),
    'starred_url': fields.String(required=True, description="starred url"),
    'subscriptions_url': fields.String(required=True, description="subscriptions url"),
    'type': fields.String(required=True, description="type"),
    'updated_at': fields.DateTime(required=True, description="updated at"),
    'url': fields.String(required=True, description="url"),
})

user_dao = UserDAO()
repos_dao = RepositoryDAO()


@api.route('/')
class UserList(Resource):
    @api.doc('list user')
    @api.marshal_with(user, code=200, mask=False)
    def get(self):
        '''List all users'''

        return user_dao.users, 200


@api.route('/<id>')
@api.param("id", "user's github id")
@api.doc(responses={
    400: 'Id must be a numeric value',
    404: 'User not found in database'})
class UserAndRepositoriesDetail(Resource):
    def get(self, id):
        """Return user details and repositories details."""

        if not id.isnumeric():
            api.abort(400)

        user = user_dao.get_user_by_id(id)
        if user:
            user_column = user_dao.get_columns_name()
            user = dict(zip(user_column, user[0]))
            user_repositories = repos_dao.get(id)
            columns = repos_dao.get_columns_names()
            repositories_dict = [
                dict(zip(columns, i)) for i in user_repositories]
            data = {
                'user': user,
                'repositories': repositories_dict
            }
            return data, 200

        api.abort(404)
