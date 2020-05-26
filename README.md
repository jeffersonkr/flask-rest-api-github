![App unit test](https://github.com/jeffersonkr/flask-rest-api-github/workflows/App%20unit%20test/badge.svg)

# Flask REST API - GITHUB
This is an Flask REST API software for fetch data from github and save at MYSQL database to retrieve data when needed.
Currently for this project we just fetch three end-point with are for user and repositories details.
 - `https://api.github.com/users/<username>/repos`
 - `https://api.github.com/users/<username>`
 - `https://api.github.com/repos/<username>/<repository_name>`

-----------------------------------------------------------------
## HOW TO START:

1. Clone this repository.
    - `git clone https://github.com/jeffersonkr/flask-rest-api-github.git`

2. In the terminal go to the directory of repository.
3. Run docker composer
    - `docker-compose up --build`
-----------------------------------------------------------------
## Using REST API

<b>Getting user's public repositories name list, user's data will automactly be saved into the database, and getting the repository details will save repository's data into the database.

</b>
This address was set at docker-compose.yml - http://172.25.0.10:5000 .


###### API End-Points:
 - Get all users ` GET : /users/ `
 - Get user and his all repositories details ` GET : /users/<id>/ `
 - Get user's public repositories name list ` GET : /repos/public_repository/<username> `
 - Get user's public repository details ` GET : /repos/detail_repository/<username>/<repository_name> `


###### Using API with curl:
 - Get all users:
    - `curl -X GET http://172.25.0.10:5000/users/`
 - Get user and his all repositories details:
    - `curl -X GET http://172.25.0.10:5000/users/<id>`
 - Get user's public repositories name list 
    - `curl -X GET http://172.25.0.10:5000/repos/public_repository/<username> `
 - Get user's public repository details 
    - `curl -X GET http://172.25.0.10:5000/repos/detail_repository/<username>/<repository_name> `


##### Usage Example:

- Get my public repositories:

```console
>> curl -X GET http://172.25.0.10:5000/repos/public_repository/jeffersonkr

{
   "list_repository_name":[
      "flask-rest-api-github",
      "fiap-courses-ia",
      "opencv",
      "django_realtime",
      "projeto_ope_imobiliaria",
      "django",
      "Luizalabs-Employee-Manager",
      "firebase-admin-python",
      "imobel_app","pynbiobsp",
      "Adafruit_CircuitPython_Fingerprint",
      "flask_forum_API",
      "Tkinter-Imobiliaria",
      "lms-atividades-continuas-time-grupope2b"
      ]
} 
```  

- Get all users saved on database:

```console
>> curl -X GET http://172.25.0.10:5000/users/

[
   {
      "avatar_url": "https://avatars1.githubusercontent.com/u/36552733?v=4", 
      "bio": "Python Developer", 
      "blog": "", 
      "company": null, 
      "created_at": "2018-02-16T22:19:15+00:00", 
      "email": null, 
      "events_url": "https://api.github.com/users/jeffersonkr/events{/privacy}", 
      "followers": 6, 
      "followers_url": "https://api.github.com/users/jeffersonkr/followers", 
      "following": 8, 
      "following_url": "https://api.github.com/users/jeffersonkr/following{/other_user}", 
      "gists_url": "https://api.github.com/users/jeffersonkr/gists{/gist_id}", 
      "gravatar_id": "", 
      "hireable": true, 
      "html_url": "https://github.com/jeffersonkr", 
      "id": 36552733, 
      "location": "Sao Paulo", 
      "login": "jeffersonkr", 
      "name": "Jefferson Kwak", 
      "node_id": "MDQ6VXNlcjM2NTUyNzMz", 
      "organizations_url": "https://api.github.com/users/jeffersonkr/orgs", 
      "public_gists": "0", 
      "public_repos": "14", 
      "received_events_url": "https://api.github.com/users/jeffersonkr/received_events", 
      "repos_url": "https://api.github.com/users/jeffersonkr/repos", 
      "site_admin": false, 
      "starred_url": "https://api.github.com/users/jeffersonkr/starred{/owner}{/repo}", 
      "subscriptions_url": "https://api.github.com/users/jeffersonkr/subscriptions", 
      "type": "User", 
      "updated_at": "2020-05-26T08:04:45+00:00", 
      "url": "https://api.github.com/users/jeffersonkr"
   }
]
```  

- Get my fiap-courses-ia repository details:

```console
>> curl -X GET http://172.25.0.10:5000/repos/detail_repository/jeffersonkr/fiap-courses-ia

{
   "id": 264438370, 
   "node_id": "MDEwOlJlcG9zaXRvcnkyNjQ0MzgzNzA=", 
   "name": "fiap-courses-ia", 
   "full_name": "jeffersonkr/fiap-courses-ia", 
   "private": false, 
   "owner": {
      "login": "jeffersonkr", 
      "id": 36552733, 
      "node_id": "MDQ6VXNlcjM2NTUyNzMz", 
      "avatar_url": "https://avatars1.githubusercontent.com/u/36552733?v=4", 
      "gravatar_id": "", 
      "url": "https://api.github.com/users/jeffersonkr", 
      "html_url": "https://github.com/jeffersonkr", 
      "followers_url": "https://api.github.com/users/jeffersonkr/followers", 
      "following_url": "https://api.github.com/users/jeffersonkr/following{/other_user}", 
      "gists_url": "https://api.github.com/users/jeffersonkr/gists{/gist_id}", 
      "starred_url": "https://api.github.com/users/jeffersonkr/starred{/owner}{/repo}", 
      "subscriptions_url": "https://api.github.com/users/jeffersonkr/subscriptions", 
      "organizations_url": "https://api.github.com/users/jeffersonkr/orgs", 
      "repos_url": "https://api.github.com/users/jeffersonkr/repos", 
      "events_url": "https://api.github.com/users/jeffersonkr/events{/privacy}", 
      "received_events_url": "https://api.github.com/users/jeffersonkr/received_events", 
      "type": "User", 
      "site_admin": false
      }, 
   "html_url": "https://github.com/jeffersonkr/fiap-courses-ia", 
   "description": "fiap IA class notebooks, exercise and others.", 
   "fork": false, 
   "url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia", 
   "forks_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/forks", 
   "keys_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/keys{/key_id}", 
   "collaborators_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/collaborators{/collaborator}", 
   "teams_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/teams", 
   "hooks_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/hooks", 
   "issue_events_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/issues/events{/number}", 
   "events_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/events", 
   "assignees_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/assignees{/user}", 
   "branches_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/branches{/branch}", 
   "tags_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/tags", 
   "blobs_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/git/blobs{/sha}", 
   "git_tags_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/git/tags{/sha}", 
   "git_refs_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/git/refs{/sha}", 
   "trees_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/git/trees{/sha}", 
   "statuses_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/statuses/{sha}", 
   "languages_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/languages", 
   "stargazers_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/stargazers", 
   "contributors_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/contributors", 
   "subscribers_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/subscribers", 
   "subscription_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/subscription", 
   "commits_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/commits{/sha}", 
   "git_commits_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/git/commits{/sha}", 
   "comments_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/comments{/number}", 
   "issue_comment_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/issues/comments{/number}", 
   "contents_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/contents/{+path}", 
   "compare_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/compare/{base}...{head}", 
   "merges_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/merges", 
   "archive_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/{archive_format}{/ref}", 
   "downloads_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/downloads", 
   "issues_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/issues{/number}", 
   "pulls_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/pulls{/number}", 
   "milestones_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/milestones{/number}", 
   "notifications_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/notifications{?since,all,participating}", 
   "labels_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/labels{/name}", 
   "releases_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/releases{/id}", 
   "deployments_url": "https://api.github.com/repos/jeffersonkr/fiap-courses-ia/deployments", 
   "created_at": "2020-05-16T13:01:38Z", 
   "updated_at": "2020-05-16T14:26:29Z", 
   "pushed_at": "2020-05-16T14:26:27Z", 
   "git_url": "git://github.com/jeffersonkr/fiap-courses-ia.git", 
   "ssh_url": "git@github.com:jeffersonkr/fiap-courses-ia.git", 
   "clone_url": "https://github.com/jeffersonkr/fiap-courses-ia.git", 
   "svn_url": "https://github.com/jeffersonkr/fiap-courses-ia", 
   "homepage": null, 
   "size": 8, 
   "stargazers_count": 0, 
   "watchers_count": 0, 
   "language": "Jupyter Notebook", 
   "has_issues": true, 
   "has_projects": true, 
   "has_downloads": true, 
   "has_wiki": true, 
   "has_pages": false, 
   "forks_count": 0, 
   "mirror_url": null, 
   "archived": false, 
   "disabled": false, 
   "open_issues_count": 0, 
   "license": null, 
   "forks": 0, 
   "open_issues": 0, 
   "watchers": 0, 
   "default_branch": "master", 
   "temp_clone_token": null, 
   "network_count": 0, 
   "subscribers_count": 1
}
```  

- Get my details and all repositories saved into database:

```console
>> curl -X GET http://172.25.0.10:5000/users/36552733

{
    "user": {
        "avatar_url": "https://avatars1.githubusercontent.com/u/36552733?v=4", 
        "bio": "Python Developer", 
        "blog": "", 
        "company": null, 
        "created_at": "2018-02-16T22:19:15Z", 
        "email": null, 
        "events_url": "https://api.github.com/users/jeffersonkr/events{/privacy}", 
        "followers": "6", 
        "followers_url": "https://api.github.com/users/jeffersonkr/followers", 
        "following": "8", 
        "following_url": "https://api.github.com/users/jeffersonkr/following{/other_user}", 
        "gists_url": "https://api.github.com/users/jeffersonkr/gists{/gist_id}", 
        "gravatar_id": "", 
        "hireable": 1, 
        "html_url": "https://github.com/jeffersonkr", 
        "id": 36552733, 
        "location": "Sao Paulo", 
        "login": "jeffersonkr", 
        "name": "Jefferson Kwak", 
        "node_id": "MDQ6VXNlcjM2NTUyNzMz", 
        "organizations_url": "https://api.github.com/users/jeffersonkr/orgs", 
        "public_gists": 0, 
        "public_repos": 14, 
        "received_events_url": "https://api.github.com/users/jeffersonkr/received_events", 
        "repos_url": "https://api.github.com/users/jeffersonkr/repos", 
        "site_admin": 0, 
        "starred_url": "https://api.github.com/users/jeffersonkr/starred{/owner}{/repo}", 
        "subscriptions_url": "https://api.github.com/users/jeffersonkr/subscriptions", 
        "type": "User", 
        "updated_at": "2020-05-26T08:04:45Z", 
        "url": "https://api.github.com/users/jeffersonkr"
    }, 
    "repositories": [
        {
            "id": 261314781, 
            "node_id": "MDEwOlJlcG9zaXRvcnkyNjEzMTQ3ODE=", 
            "name": "opencv", 
            "full_name": "jeffersonkr/opencv", 
            "private": 0, 
            "owner": 36552733, 
            "html_url": "https://github.com/jeffersonkr/opencv", 
            "description": "Open Source Computer Vision Library", 
            "fork": 1, 
            "url": "https://api.github.com/repos/jeffersonkr/opencv", 
            "forks_url": "https://api.github.com/repos/jeffersonkr/opencv/forks", 
            "keys_url": "https://api.github.com/repos/jeffersonkr/opencv/keys{/key_id}", 
            "collaborators_url": "https://api.github.com/repos/jeffersonkr/opencv/collaborators{/collaborator}", 
            "teams_url": "https://api.github.com/repos/jeffersonkr/opencv/teams", 
            "hooks_url": "https://api.github.com/repos/jeffersonkr/opencv/hooks", 
            "issue_events_url": "https://api.github.com/repos/jeffersonkr/opencv/issues/events{/number}", 
            "events_url": "https://api.github.com/repos/jeffersonkr/opencv/events", 
            "assignees_url": "https://api.github.com/repos/jeffersonkr/opencv/assignees{/user}", 
            "branches_url": "https://api.github.com/repos/jeffersonkr/opencv/branches{/branch}", 
            "tags_url": "https://api.github.com/repos/jeffersonkr/opencv/tags", 
            "blobs_url": "https://api.github.com/repos/jeffersonkr/opencv/git/blobs{/sha}", 
            "git_tags_url": "https://api.github.com/repos/jeffersonkr/opencv/git/tags{/sha}", 
            "git_refs_url": "https://api.github.com/repos/jeffersonkr/opencv/git/refs{/sha}", 
            "trees_url": "https://api.github.com/repos/jeffersonkr/opencv/git/trees{/sha}", 
            "statuses_url": "https://api.github.com/repos/jeffersonkr/opencv/statuses/{sha}", 
            "languages_url": "https://api.github.com/repos/jeffersonkr/opencv/languages", 
            "stargazers_url": "https://api.github.com/repos/jeffersonkr/opencv/stargazers", 
            "contributors_url": "https://api.github.com/repos/jeffersonkr/opencv/contributors", 
            "subscribers_url": "https://api.github.com/repos/jeffersonkr/opencv/subscribers", 
            "subscription_url": "https://api.github.com/repos/jeffersonkr/opencv/subscription", 
            "commits_url": "https://api.github.com/repos/jeffersonkr/opencv/commits{/sha}", 
            "git_commits_url": "https://api.github.com/repos/jeffersonkr/opencv/git/commits{/sha}", 
            "comments_url": "https://api.github.com/repos/jeffersonkr/opencv/comments{/number}", 
            "issue_comment_url": "https://api.github.com/repos/jeffersonkr/opencv/issues/comments{/number}", 
            "contents_url": "https://api.github.com/repos/jeffersonkr/opencv/contents/{+path}", 
            "compare_url": "https://api.github.com/repos/jeffersonkr/opencv/compare/{base}...{head}", 
            "merges_url": "https://api.github.com/repos/jeffersonkr/opencv/merges", 
            "archive_url": "https://api.github.com/repos/jeffersonkr/opencv/{archive_format}{/ref}", 
            "downloads_url": "https://api.github.com/repos/jeffersonkr/opencv/downloads", 
            "issues_url": "https://api.github.com/repos/jeffersonkr/opencv/issues{/number}", 
            "pulls_url": "https://api.github.com/repos/jeffersonkr/opencv/pulls{/number}", 
            "milestones_url": "https://api.github.com/repos/jeffersonkr/opencv/milestones{/number}", 
            "notifications_url": "https://api.github.com/repos/jeffersonkr/opencv/notifications{?since,all,participating}", 
            "labels_url": "https://api.github.com/repos/jeffersonkr/opencv/labels{/name}", 
            "releases_url": "https://api.github.com/repos/jeffersonkr/opencv/releases{/id}", 
            "deployments_url": "https://api.github.com/repos/jeffersonkr/opencv/deployments", 
            "created_at": "2020-05-04T23:05:35Z", 
            "updated_at": "2020-05-04T23:05:38Z", 
            "pushed_at": "2020-05-04T17:01:24Z", 
            "git_url": "git://github.com/jeffersonkr/opencv.git", 
            "ssh_url": "git@github.com:jeffersonkr/opencv.git", 
            "clone_url": "https://github.com/jeffersonkr/opencv.git", 
            "svn_url": "https://github.com/jeffersonkr/opencv", 
            "homepage": "https://opencv.org", 
            "size": 480194, 
            "stargazers_count": 0, 
            "watchers_count": 0, 
            "language": null, 
            "has_issues": 0, 
            "has_projects": 1, 
            "has_downloads": 1, 
            "has_wiki": 1, 
            "has_pages": 0, 
            "forks_count": 0, 
            "mirror_url": null, 
            "archived": 0, 
            "disabled": 0, 
            "open_issues_count": 0, 
            "license": "Other", 
            "forks": 0, 
            "open_issues": 0, 
            "watchers": 0, 
            "default_branch": "master", 
            "temp_clone_token": null, 
            "parent": 5108051, 
            "source": 5108051, 
            "organization": "", 
            "network_count": 36010, 
            "subscribers_count": 0
        }
    ]
}
```  