from flask_restplus import Namespace, Resource, fields
from core.models.user_dao import UserDAO
from core.models.repository_dao import RepositoryDAO
from flask import jsonify
import requests

api = Namespace(
    'Repository',
    description='github user repository operation'
)

repos = api.model('Repository', {
    "id": fields.Integer(required=True, description="Repository id"),
    "node_id": fields.String(required=True, description="node_id"),
    "name": fields.String(required=True, description="name"),
    "full_name": fields.String(required=True, description="full_name"),
    "private": fields.Boolean(required=True, description="private true/false"),
    "owner": fields.Integer(required=True, description="owner id's"),
    "html_url": fields.String(required=True, description="html_url"),
    "description": fields.String(required=True, description="description"),
    "fork": fields.Boolean(required=True, description="fork true/false"),
    "url": fields.String(required=True, description="url"),
    "forks_url": fields.String(required=True, description="forks_url"),
    "keys_url": fields.String(required=True, description="keys_url"),
    "collaborators_url": fields.String(required=True, description="collaborators_url"),
    "teams_url": fields.String(required=True, description="teams_url"),
    "hooks_url": fields.String(required=True, description="hooks_url"),
    "issue_events_url": fields.String(required=True, description="issue_events_url"),
    "events_url": fields.String(required=True, description="events_url"),
    "assignees_url": fields.String(required=True, description="assignees_url"),
    "branches_url": fields.String(required=True, description="branches_url"),
    "tags_url": fields.String(required=True, description="tags_url"),
    "blobs_url": fields.String(required=True, description="blobs_url"),
    "git_tags_url": fields.String(required=True, description="git_tags_url"),
    "git_refs_url": fields.String(required=True, description="git_refs_url"),
    "trees_url": fields.String(required=True, description="trees_url"),
    "statuses_url": fields.String(required=True, description="statuses_url"),
    "languages_url": fields.String(required=True, description="languages_url"),
    "stargazers_url": fields.String(required=True, description="stargazers_url"),
    "contributors_url": fields.String(required=True, description="contributors_url"),
    "subscribers_url": fields.String(required=True, description="subscribers_url"),
    "subscription_url": fields.String(required=True, description="subscription_url"),
    "commits_url": fields.String(required=True, description="commits_url"),
    "git_commits_url": fields.String(required=True, description="git_commits_url"),
    "comments_url": fields.String(required=True, description="comments_url"),
    "issue_comment_url": fields.String(required=True, description="issue_comment_url"),
    "contents_url": fields.String(required=True, description="contents_url"),
    "compare_url": fields.String(required=True, description="compare_url"),
    "merges_url": fields.String(required=True, description="merges_url"),
    "archive_url": fields.String(required=True, description="archive_url"),
    "downloads_url": fields.String(required=True, description="downloads_url"),
    "issues_url": fields.String(required=True, description="issues_url"),
    "pulls_url": fields.String(required=True, description="pulls_url"),
    "milestones_url": fields.String(required=True, description="milestones_url"),
    "notifications_url": fields.String(required=True, description="notifications_url"),
    "labels_url": fields.String(required=True, description="labels_url"),
    "releases_url": fields.String(required=True, description="releases_url"),
    "deployments_url": fields.String(required=True, description="deployments_url"),
    "created_at": fields.String(required=True, description="created_at"),
    "updated_at": fields.String(required=True, description="updated_at"),
    "pushed_at": fields.String(required=True, description="pushed_at"),
    "git_url": fields.String(required=True, description="git_url"),
    "ssh_url": fields.String(required=True, description="ssh_url"),
    "clone_url": fields.String(required=True, description="clone_url"),
    "svn_url": fields.String(required=True, description="svn_url"),
    "homepage": fields.String(required=True, description="homepage"),
    "size": fields.Integer(required=True, description="size"),
    "stargazers_count": fields.Integer(required=True, description="stargazers_count"),
    "watchers_count": fields.Integer(required=True, description="watchers_count"),
    "language": fields.String(required=True, description="language"),
    "has_issues": fields.Boolean(required=True, description="has_issues"),
    "has_projects": fields.Boolean(required=True, description="has_projects"),
    "has_downloads": fields.Boolean(required=True, description="has_downloads"),
    "has_wiki": fields.Boolean(required=True, description="has_wiki"),
    "has_pages": fields.Boolean(required=True, description="has_pages"),
    "forks_count": fields.Integer(required=True, description="forks_count"),
    "mirror_url": fields.String(required=True, description="mirror_url"),
    "archived": fields.Boolean(required=True, description="archived"),
    "disabled": fields.Boolean(required=True, description="disabled"),
    "open_issues_count": fields.Integer(required=True, description="open_issues_count"),
    "license": fields.String(required=False, description="license"),
    "forks": fields.Integer(required=True, description="forks"),
    "open_issues": fields.Integer(required=True, description="open_issues"),
    "watchers": fields.Integer(required=True, description="watchers"),
    "default_branch": fields.String(required=True, description="default_branch"),
    "temp_clone_token": fields.String(required=True, description="temp_clone_token"),
    "network_count": fields.Integer(required=True, description="network_count"),
    "subscribers_count": fields.Integer(required=True, description="subscribers_count"),
})

user_dao = UserDAO()
repos_dao = RepositoryDAO()


@api.route('/detail_repository/<username>/<repository_name>')
class get_public_repository_detail(Resource):
    """Route to get public repository details."""

    def _get_user_repository_details(self, username, repository_name):
        """Internal method to get repository and insert 
        or update the user into database.

        Params:
            username: str()
                github login
            repository_name: str()
                github repository name

        Return:
            Response.json() or Jsonify Object
        """

        url = f"https://api.github.com/repos/{username}/{repository_name}"
        r = requests.get(url)
        if r.status_code == 200:
            # insere os dados do usuario no banco de dados.
            user_dao.create(r.json()['owner'])
            # insere os dados do repositorio no banco de dados.
            repos_dao.create(r.json())
            return r.json()
        else:
            return jsonify({
                "status": r.status_code,
                "description": r.json()
            })

    def get(self, username, repository_name):
        """Return repository details.

        Params:
            username: str()
                github login
            repository_name: str()
                github repository name

        Return:
            Internal method _get_user_repository_details()
        """
        return self._get_user_repository_details(username, repository_name)


@api.route('/public_repository/<username>')
@api.response(404, 'User not found')
@api.response(200, 'Sucess')
class get_public_repository(Resource):
    """Route to get user's public repositories."""

    def _get_user_public_repository(self, username):
        """Internal method to get user repositories list name
        and insert or update the user."""

        # primeiro pegamos os dados do usuario para inserir ou
        # atualizar no banco de dados.
        url = f"https://api.github.com/users/{username}"
        r_user = requests.get(url)
        if r_user.status_code == 200:
            data = r_user.json()
            create_response = user_dao.create(data)
        else:
            error_msg = {
                "status": r_user.status_code,
                "description": r_user.json()
            }
            return error_msg

        # agora pegamos os repositorios públicos desse usuario.
        url_repos = f"https://api.github.com/users/{username}/repos"
        r_repos = requests.get(url_repos, {"sort": "created"})

        if r_repos.status_code == 200:
            repository_names = {
                "list_repository_name": [
                    self._filter_username(
                        username, i["full_name"]) for i in r_repos.json()]}

            return repository_names
        else:
            error_msg = {
                "status": r.status_code,
                "description": r.json()
            }
            return error_msg

    def _filter_username(self, username, repos_name):
        """Internal method to remove username from respository name.

        Params:
            username: str()
                github login
            repository_name: str()
                github repository name

        Return:
            repository name without user
            example: IN > jeffersonkr/repository > OUT > repository
        """

        return repos_name.replace(f"{username}/", "")

    def get(self, username):
        """Username's public repositories.

        Params:
            username: str()
                github login
        Return:
            jsonify object
        """
        return jsonify(self._get_user_public_repository(username))
