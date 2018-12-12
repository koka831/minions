import multiprocessing
import toml
from minion import MinionConfig, RepositoryConfig
from minion.minion import Minion


def main():
    config = toml.load(MinionConfig.config_path)

    minions = []
    for repo in config['repository']:
        print('append: {}'.format(repo['url']))
        minions.append(RepositoryConfig(repo['url'], repo['mail_to']))

    with multiprocessing.Pool(MinionConfig.N_PROC) as pool:
        pool.map_async(Minion, minions)
        pool.close()
        pool.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('done')
