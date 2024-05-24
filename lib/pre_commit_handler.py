from .utils import execute
import sys

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
Checks if pre_commit exists. If it doesn't informs the users and exists
'''
def pre_commit_requirement():
    if (execute("pip list | grep pre-commit").returncode != 0):
        print('[WARNING]: pre-commit is not installed')
        try:
            option = input('Do you want to install it [y/n]: ').upper()
            if (option == 'Y'):
                print('Installing pre-commit ...')
                execute('pip install pre-commit')
                print('Installed!')
            else:
                sys.exit(0)
        except:
            print('\nBye!')
            sys.exit(0)