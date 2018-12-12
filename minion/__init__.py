import os
import toml
from dataclasses import dataclass
import multiprocessing


@dataclass
class MinionConfig:
    config_path: str = os.path.join(os.path.dirname(__file__), '../config.toml')
    _config = toml.load(config_path)

    N_PROC: int = _config['config'].get('n_proc', multiprocessing.cpu_count() - 1)
    INTERVAL: int = _config['config'].get('interval', 5)
    TIMEOUT: int = _config['config'].get('timeout', 0)
    DEST: str = _config['config'].get('dest', './repositories')
    ID_RSA: str = _config['config'].get('id_rsa', '~/.ssh/id_rsa')

    mail_from: str = _config['config'].get('mail_from', 'mail@localhost')


@dataclass
class RepositoryConfig:
    url: str
    mail_to: str
