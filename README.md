# Requirements
- Python 3.9
- Pip
- docker
- docker-compose 3.2+

# Setup
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -pv instances
```

## Create New Nextcloud Instance
```sh
./new-instance-prepare.py --help
```

## Update all instances
```sh
./update-all-instances.py
```

## Disable Python Virtual Env
```sh
deactivate
```
