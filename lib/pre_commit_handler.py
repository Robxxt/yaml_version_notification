import subprocess
import sys
import os
import lib

'''
check if .pre-commit-config.yaml file exists
'''
def pre_commit_config_exists():
    return os.path.isfile('.pre-commit-config.yaml')


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

