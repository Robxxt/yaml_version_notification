import subprocess
import sys

'''
Executes command.
Upon failure prints the error message and exits.
'''
def execute(command):
    try:
        command = subprocess.run(command, shell=True, text=True, capture_output=True)
        # still to see what is the valid output code
        if (command.returncode != 0):
            print(f"\n[ERROR]:\n{command.stdout}", file=sys.stderr)
            sys.exit(1)
        return command
    except:
        sys.exit(1)