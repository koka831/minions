import os
from git import Git, Repo, GitDB
from minion import MinionConfig


class GitClient:

    def __init__(self, url, dest=None):
        '''
        url: string; url of target git repository.
        dest: string; destination to clone target repository.
            default: `/repositories/${user_name}/${project_name}`
        '''
        self.remote_url = url
        self.git_dir = dest if dest else os.path.basename(url)
        self.work_dir = os.path.join(os.path.dirname(__file__), '../', MinionConfig.DEST)
        self.local_dir = os.path.join(self.work_dir, self.git_dir)

        if not os.path.isdir(self.work_dir):
            print('init /{} directory'.format(MinionConfig.DEST))
            os.mkdir(self.work_dir)
        else:
            print('/{} directory exists. skip'.format(MinionConfig.DEST))

        if not os.path.isdir(self.local_dir):
            print('cloning {}...'.format(self.remote_url))
            Git().clone(url, self.local_dir)

    def check_is_updated(self):
        '''detect if remote is updated.
        '''
        repo = Repo(self.local_dir, odbt=GitDB)
        local_hash = repo.commit()
        remote_hash = repo.remotes.origin.fetch()[0].commit
        if local_hash == remote_hash:
            return False
        else:
            return True

    def pull(self):
        repo = Repo(self.local_dir, odbt=GitDB)
        repo.remotes.origin.pull()
