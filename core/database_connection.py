import MySQLdb


class Database:
    """A simple wrapper for MySQLdb.
    Obs: This wrapper never close the cursor or
    connection be cautious to this.
    """

    def __init__(self, user="root", passwd="secrets", db="captalys", host="database", port=3306):
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
        self._conn = MySQLdb.connect(
            user=user, passwd=passwd, db=db, host=host, port=port)
        self._cursor = self._get_cursor()

    def _get_cursor(self):
        """Internal method to get cursor."""

        return self._conn.cursor()

    def cursor(self):
        """Method to get a cursor."""

        return self._cursor

    def commit(self):
        """Method to commit an connection"""

        self._conn.commit()

    def close(self):
        """Method to close MySQLdb.connect object."""

        self._conn.close()


db = Database()

# caso arquivo seja executado, chama o cursor e
# executa a query, seguindo com o fechamento do
# cursor e a conexão.
if __name__ == "__main__":
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            avatar_url varchar(255), bio varchar(255) DEFAULT '', blog varchar(255) DEFAULT '',
            company varchar(255) DEFAULT '', created_at varchar(255), email varchar(255) DEFAULT '',
            events_url varchar(255), followers varchar(255), followers_url varchar(255),
            following varchar(255), following_url varchar(255), gists_url varchar(255),
            gravatar_id varchar(255) DEFAULT '', hireable BOOLEAN DEFAULT false,
            html_url varchar(255), id int, location varchar(100), login varchar(100),
            name varchar(100), node_id varchar(255) DEFAULT '', organizations_url varchar(255),
            public_gists int DEFAULT 0, public_repos int DEFAULT 0, received_events_url varchar(255),
            repos_url varchar(255), site_admin BOOLEAN DEFAULT false, starred_url varchar(255),
            subscriptions_url varchar(255), type varchar(100), updated_at varchar(255),
            url varchar(255), PRIMARY KEY(id)
        );
        CREATE TABLE IF NOT EXISTS repository(
            id int, node_id varchar(255), name varchar(255), full_name varchar(255),
            private BOOLEAN DEFAULT false, owner int, html_url varchar(255),
            description varchar(250), fork BOOLEAN DEFAULT false, url varchar(255),
            forks_url varchar(255), keys_url varchar(255), collaborators_url varchar(255),
            teams_url varchar(255), hooks_url varchar(255), issue_events_url varchar(255),
            events_url varchar(255), assignees_url varchar(255), branches_url varchar(255),
            tags_url varchar(255), blobs_url varchar(255), git_tags_url varchar(255),
            git_refs_url varchar(255), trees_url varchar(255), statuses_url varchar(255),
            languages_url varchar(255), stargazers_url varchar(255), contributors_url varchar(255),
            subscribers_url varchar(255), subscription_url varchar(255), commits_url varchar(255),
            git_commits_url varchar(255), comments_url varchar(255), issue_comment_url varchar(255),
            contents_url varchar(255), compare_url varchar(255), merges_url varchar(255),
            archive_url varchar(255), downloads_url varchar(255), issues_url varchar(255),
            pulls_url varchar(255), milestones_url varchar(255), notifications_url varchar(255),
            labels_url varchar(255), releases_url varchar(255), deployments_url varchar(255),
            created_at varchar(255), updated_at varchar(255), pushed_at varchar(255),
            git_url varchar(255), ssh_url varchar(255), clone_url varchar(255),
            svn_url varchar(255), homepage varchar(255), size int, stargazers_count int,
            watchers_count int, language varchar(255), has_issues BOOLEAN DEFAULT false,
            has_projects BOOLEAN DEFAULT false, has_downloads BOOLEAN DEFAULT false,
            has_wiki BOOLEAN DEFAULT false, has_pages BOOLEAN DEFAULT false,
            forks_count int, mirror_url varchar(255), archived BOOLEAN DEFAULT false,
            disabled BOOLEAN DEFAULT false, open_issues_count int, license varchar(255),
            forks int, open_issues int, watchers int, default_branch varchar(255),
            temp_clone_token varchar(255), parent int, source int,
            organization varchar(255), network_count int, subscribers_count int,
            PRIMARY KEY(id),
            CONSTRAINT FK_ReposOwner FOREIGN KEY(owner) REFERENCES user(id));""")
    cursor.close()
    db.close()
