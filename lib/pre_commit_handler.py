import subprocess
import sys
import os

'''
check if .pre-commit-config.yaml file exists
'''
def pre_commit_config_exists():
    return os.path.isfile('.pre-commit-config.yaml')

'''
validate .pre-commit-config.yaml file
'''
def validate_pre_commit_config():
    try:
        command = subprocess.run('pre-commit validate-config', shell=True)
        # still to see what is the valid output code
        if (command.returncode != 0):
            print('Invalid [pre-commit validate-config]', file=sys.stderr)
            sys.exit(1)
    except:
        print('There was a problem executing [pre-commit validate-config]', file=sys.stderr)
        sys.exit(1)

'''
create .pre-commit-config.yaml template file
'''
def create_pre_commit_config_file():
    print("""
    [INFO]: .pre-commit-config.yaml doesn't exists.
    Creating one based on a template. Feel free to modify it!
    [IMPORTANT] If you modify it run: pre-commit install
    """)
    with open('.pre-commit-config.yaml', 'w') as file:
        file.write('---\nThis is a template pre-commit-config file')

'''
run auto-update
'''
def auto_update_pre_commit_config():
    try:
        command = subprocess.run('pre-commit auto-update', shell=True)
        # still to see what is the valid output code
        if (command.returncode != 0):
            print('Invalid [pre-commit auto-update]', file=sys.stderr)
            sys.exit(1)
    except:
        print('There was a problem executing [pre-commit auto-update]', file=sys.stderr)
        sys.exit(1)
