import subprocess
import sys
'''
Retrieves the tag with the yaml version from the repositroy and
sets app.curr_yaml_version = "mj.fa.mn" where mj is major, 
fa is feature and mn is minimum
'''
def get_curr_yaml_version(app):
    # this is temporary. Function still to be implemented
    app.curr_yaml_version = "1.0.1"

'''
Searches for the yaml file, once it finds it, captures the version
and sets app.pack_yaml_version = "mj.fa.mn" where mj is major, 
fa is feature and mn is minimum
'''
def get_pack_yaml_version(app):
    try:
        app.pack_yaml_version = subprocess.run("grep version pack.yaml | awk '{print $2}'", shell=True, text=True, capture_output=True).stdout.rstrip()
    except:
        print('Failed to get_pack_yaml_version!', file=sys.stderr)
        sys.exit(1)

'''
Compares self.curr_yaml_version and self.pack_yaml_version if they are different
return false otherwise true
'''
def is_diff_yaml_versions(app):
        return app.curr_yaml_version == app.pack_yaml_version

def display_warning(app):
    print('[WARNING]: YOU SHOULD TAKE A LOOK AT pack.yaml version')
    print(f"curr_version: {app.curr_yaml_version}")
    print(f"pack_yaml_version: {app.pack_yaml_version}")