import os, subprocess, sys

cmd = 'sudo'
ls = 'ls'
chown = 'chown'
user = os.getlogin()
root = 'root'
base_path = r"/usr/share/backgrounds"
try:
    dir_name = sys.argv[1]
except IndexError:
        pass

"""
    This module handles the manipulation of the unix file system,

    Args:
        login(): Handles your super user login

        user_perm(): Handles the switching of user and group permissions to the logged in user

        root_perm():  Handles the switching of users and group permissions to the superuser or root

        dir_maker(): Handles the creation of directory

        getdirname(): Gets directory name

        getpath(): Gets base_path 
"""

def login():

    root_pass = subprocess.Popen([cmd, '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    out, err = root_pass.communicate()
    
def user_perm():
    payload = subprocess.Popen([cmd, chown, '-R', user+':'+user, base_path], stdout = subprocess.PIPE)
    output = payload.communicate()

def root_perm():
    payload = subprocess.Popen([cmd, chown,'-R', root+':'+root, base_path], stdout = subprocess.PIPE)
    output = payload.communicate()

def dir_maker():

    os.chdir(base_path)

    ### THIS PART BELOW IS WORKING PERFECTLY

    try:
        # dir_name = input("Input Directory Name: ")
        print(f"Creating Directory '{dir_name}'")
        os.mkdir(dir_name)
        print(f"'{dir_name}' Created")
    except FileExistsError as e:
        print(f"Use another filename: \n{e}")

    os.chdir(base_path + '/' + dir_name)

def getdirname():
    try:
        return dir_name
    except IndexError:
        pass

def getpath():
    return base_path


if __name__ == '__main__':
    # login()
    dir_maker()
