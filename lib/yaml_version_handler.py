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
Compares self.curr_yaml_version and self.pack_yaml_version if they are different
return false otherwise true
'''
def is_diff_yaml_versions(app):
        return app.curr_yaml_version != app.pack_yaml_version

def display_warning(app):
    print('[WARNING]: YOU SHOULD TAKE A LOOK AT pack.yaml version')
    print(f"curr_version: {app.curr_yaml_version}")
    print(f"pack_yaml_version: {app.pack_yaml_version}")