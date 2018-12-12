## minion

a task runner/watching git repository, pull & run runner.sh when detects changes on remote.
### motivation/background
Since we do not have any GIP on our laboratory, we need to go there to use GPU machine.
Up to now we run program before going home, and we couldn't know if it goes well/failed until go there next time.
minion helps us to manage the tasks above; fetch program from git, run it, and send mail the result.

### usage

#### setup

```sh

git clone git@github.com:koka831/minion.git

cd minion

# installation
pip install -r requirements.txt
# or pipenv shell && pipenv install

# edit config.py to add the target repository.
# examples on the section #configure below.
$EDITOR config.py

# launch minion, then minion check each repos 5 minutes each.
# can modify the interval in config.toml.
python runner.py
```
#### configure

**config.toml**

```toml
[config]
interval = 5

[[repository]]
repo = 'git@github.com/koka831/minion.git'
mail_to = 'koka.code@gmail.com'

# or
[[repository]]
repo = 'https://github.com/koka831/minion.git'
mail_to = '...'
```

#### requirements for target git repository
needs two files below in root directory.
- `/runner.sh`
- `config.minion.toml`

see examples in `/examples`.

### future works
- [ ] run jobs in docker
- [ ] daemonize/fault tolerance

### LICENSE
MIT.
