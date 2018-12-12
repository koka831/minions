import os
import sys
from subprocess import Popen, PIPE
from time import sleep
from minion import MinionConfig
from .git_client import GitClient
from .mail_client import MailClient


class Minion:

    def __init__(self, config):
        '''
        config: RepositoryConfig
        '''
        self.config = config
        self.git = GitClient(config.url)
        self.run()

    def run(self):
        while True:
            try:
                print('check repository: {}'.format(self.config.url))
                self.do_task()
                sleep(MinionConfig.INTERVAL)
            except KeyboardInterrupt:
                print('Process killed')
            except Exception as e:
                print('Exception: {}\n exits\n'.format(e))
                sys.exit(1)

    def do_task(self):
        if not self.git.check_is_updated():
            print('pulling... {}'.format(self.config.url))
            self.git.pull()
            print('running {}'.format(self.config.url))
            res, err = self.run_cmd()

            MailClient(self.config.mail_to).send(res)
        else:
            print('updated. {}'.format(self.config.url))

    def run_cmd(self):
        os.chdir(self.git.local_dir)
        cmd_file = os.path.join(os.getcwd(), 'runner.sh')
        if not os.path.isfile(cmd_file):
            return ('runner.sh not found.', 'file not found')
            sys.exit(1)
        proc = Popen(['bash', cmd_file], stdout=PIPE)
        out, err = proc.communicate()
        return (out, err)
