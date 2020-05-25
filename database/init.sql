CREATE DATABASE captalys;
USE captalys;

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
    id int, node_id varchar(50), name varchar(100), full_name varchar(150),
    private BOOLEAN DEFAULT false, owner int, html_url varchar(150),
    description varchar(255), fork BOOLEAN DEFAULT false, url varchar(150),
    forks_url varchar(150), keys_url varchar(150), collaborators_url varchar(150),
    teams_url varchar(150), hooks_url varchar(150), issue_events_url varchar(150),
    events_url varchar(150), assignees_url varchar(150), branches_url varchar(150),
    tags_url varchar(150), blobs_url varchar(150), git_tags_url varchar(150),
    git_refs_url varchar(150), trees_url varchar(150), statuses_url varchar(150),
    languages_url varchar(150), stargazers_url varchar(150), contributors_url varchar(150),
    subscribers_url varchar(150), subscription_url varchar(150), commits_url varchar(150),
    git_commits_url varchar(150), comments_url varchar(150), issue_comment_url varchar(150),
    contents_url varchar(150), compare_url varchar(150), merges_url varchar(150),
    archive_url varchar(150), downloads_url varchar(150), issues_url varchar(150),
    pulls_url varchar(150), milestones_url varchar(150), notifications_url varchar(150),
    labels_url varchar(150), releases_url varchar(150), deployments_url varchar(150),
    created_at varchar(50), updated_at varchar(50), pushed_at varchar(50),
    git_url varchar(150), ssh_url varchar(150), clone_url varchar(155),
    svn_url varchar(150), homepage varchar(150), size int, stargazers_count int,
    watchers_count int, language varchar(50), has_issues BOOLEAN DEFAULT false,
    has_projects BOOLEAN DEFAULT false, has_downloads BOOLEAN DEFAULT false,
    has_wiki BOOLEAN DEFAULT false, has_pages BOOLEAN DEFAULT false,
    forks_count int, mirror_url varchar(150), archived BOOLEAN DEFAULT false,
    disabled BOOLEAN DEFAULT false, open_issues_count int, license varchar(150),
    forks int, open_issues int, watchers int, default_branch varchar(150),
    temp_clone_token varchar(100), parent int, source int,
    organization varchar(150), network_count int, subscribers_count int,
    PRIMARY KEY(id),
    CONSTRAINT FK_ReposOwner FOREIGN KEY(owner) REFERENCES user(id)
);