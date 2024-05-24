# yaml_version_notification

## Description
Notify the user if a pack.yaml file is not been updated within a specific range of time and automate some steps
from pre-commit

## Requirements
You need to be in a virtual environment
for that you can run the next commands:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step by step
Once you are in the virtual environment run:
```bash
git clone https://github.com/Robxxt/yaml_version_notification.git
cd yaml_version_notification
pip install -e .
```

Now you can run
```bash
pp_commit
```
everywhere in the system as long as is part of the session of venv
