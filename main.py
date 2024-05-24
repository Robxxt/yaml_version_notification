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
            lib.execute("pre-commit validate-config")
            # install it
            lib.execute("pre-commit install")
        # sets curr_yaml_version
        lib.get_curr_yaml_version(self)
        # sets pack_yaml_version
        self.pack_yaml_version = lib.execute("grep version pack.yaml | awk '{print $2}'").stdout.rstrip()
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
            lib.execute("pre-commit autoupdate")
            lib.execute("pre-commit run --all-files")
            print("Calling pre-commit ...")
        else:
            print("See you once you fix it!")
            sys.exit(0)

if __name__ == '__main__':
    app = MainProgram()
    app.run()
