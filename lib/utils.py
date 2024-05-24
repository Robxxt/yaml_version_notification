import subprocess
import sys

'''
Executes command.
Upon failure prints the error message and exits.
'''
def execute(command):
    try:
        command = subprocess.run(command, shell=True)
        # still to see what is the valid output code
        if (command.returncode != 0):
            print(command.stderr, file=sys.stderr)
            sys.exit(1)
    except:
        print('There was a problem executing', file=sys.stderr)
        sys.exit(1)