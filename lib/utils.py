import subprocess
import sys

'''
Executes command.
Upon failure prints the error message and exits.
'''
def execute_exit(command):
    try:
        command = subprocess.run(command, shell=True, text=True, capture_output=True)
        # still to see what is the valid output code
        if (command.returncode != 0):
            print(f"\n[ERROR]:\n{command.stdout}", file=sys.stderr)
            sys.exit(1)
        return command
    except:
        sys.exit(1)

'''
Executes command and returns it
'''
def execute(command):
    try:
        command = subprocess.run(command, shell=True, text=True, capture_output=True)
        return command
    except:
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

'''
Retrieves the tag with the yaml version from the repositroy and
sets app.curr_yaml_version = "mj.fa.mn" where mj is major,
fa is feature and mn is minimum
'''
def get_curr_yaml_version(app):
    # this is temporary. Function still to be implemented
    app.curr_yaml_version = "1.0.1"

def display_warning(app):
    print('[WARNING]: YOU SHOULD TAKE A LOOK AT pack.yaml version')
    print(f"curr_version: {app.curr_yaml_version}")
    print(f"pack_yaml_version: {app.pack_yaml_version}")