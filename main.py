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
        if (os.path.isfile("pack.yaml") == False):
            print("[ERROR]: There is no pack.yaml file!. Check weather you are in the right directory or create a pack.yaml.", file=sys.stderr)
            sys.exit(1)
        # sets curr_yaml_version
        print(f"pre_commit_config_exists(): {lib.pre_commit_config_exists()}")
        lib.get_curr_yaml_version(self)
        # sets pack_yaml_version
        lib.get_pack_yaml_version(self)
        # compares curr_yaml_version and pack_yaml_version values
        if (lib.is_diff_yaml_versions(self) == False):
            lib.display_warning(self)
        option = input("Do you want to continue with the commit? [y/n]: ").upper()
        if (option == 'Y'):
            # run precommit
            print("Calling pre-commit ...")
        else:
            print("See you once you fix it!")
            sys.exit(0)

if __name__ == '__main__':
    app = MainProgram()
    app.run()