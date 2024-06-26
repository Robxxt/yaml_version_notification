import subprocess
import sys
import lib
import os

class   MainProgram:
    def __init__(self):
        self.curr_yaml_version = None
        self.pack_yaml_version = None

    '''
    Displays warning and allows the user to take action
    '''

    def run(self):
        # checks weather a pack.yaml file exists
        lib.pre_commit_requirement()
        if not os.path.isfile("pack.yaml"):
            print(
                """
                ERROR]: There is no pack.yaml file!. Check weather you are
                in the right directory or create a pack.yaml.
                """
            , file=sys.stderr)
            sys.exit(1)
        if not os.path.isfile('.pre-commit-config.yaml'):
            # create it
            lib.create_pre_commit_config_file()
            # validate .pre-commit-config file
            lib.execute_exit("pre-commit validate-config")
            # install it
            lib.execute_exit("pre-commit install")
            pass
        if not os.path.isfile('CHANGES.md'):
            print("[ERROR]: It's missing CHANGES.md", file=sys.stderr)
            exit(1)
        # sets curr_yaml_version based on the last version from CHANGES.md
        self.curr_yaml_version = lib.execute_exit("egrep '## \[' CHANGES.md | head -1 | awk '{print $2}'").stdout[1:-2]
        # sets pack_yaml_version
        self.pack_yaml_version = lib.execute_exit("grep version pack.yaml | awk '{print $2}'").stdout.rstrip()
        # compares curr_yaml_version and pack_yaml_version values
        if self.curr_yaml_version != self.pack_yaml_version:
            lib.display_warning(self)
            try:
                option = input("Do you want to continue with the commit? [y/n]: ").upper()
            except:
                print('\nGood bye!')
                sys.exit(1)
            if (option == 'Y'):
                # run precommit
                lib.execute_exit("pre-commit autoupdate")
                lib.execute_exit("pre-commit run --all-files")
            else:
                print("See you once you fix it!")
                sys.exit(0)
        else:
            lib.execute_exit("pre-commit autoupdate")
            lib.execute_exit("pre-commit run --all-files")