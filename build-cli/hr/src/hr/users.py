import pwd
import subprocess

"""
{
'name': 'kevin',
'groups': ['wheel', 'dev'],
'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
}
"""

user_dict = {}


def get_user_names(user_dict):
    return [user.pw_name for user in pwd.getpwall() if user.pw_uid >= 1000 and "home" in user.pw_dir]


def check_valid_user(user_dict):
    """
    Check if user exists in system
    """
    try:
        pwd.getpwnam(user_dict["name"])
    except KeyError:
        print(f"User {user_dict['name']} doesn't exists.")
        return False
    return True


def create_user(user_dict):
    """
    Create new user
    """
    # useradd -p password -G group1,group2 username
    groups = ",".join(user_dict["groups"])
    print(f"Adding user {user_dict['name']}")
    subprocess.run(["useradd", "-p", user_dict["password"], "-G", groups, user_dict["name"]])


def update_user(user_dict):
    """
    Update user
    """
    # usermod -l new_username -G new_group1,new_Group2 / -a -G append_new_group1 -p new_password
    groups = ",".join(user_dict["groups"])
    print(f"Updating user {user_dict['name']}")
    subprocess.run(["usermod", "-l", user_dict["name"], "-G", groups, "-p", user_dict["password"], user_dict["name"]])


def remove_user(username):
    """
    Remove user
    """
    # userdel username
    print(f"Removing user {username}")
    subprocess.run(["userdel", "-r", username])
