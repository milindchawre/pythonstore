import json
import pwd
import spwd
import grp


def user_names():
    return [user.pw_name for user in pwd.getpwall() if user.pw_uid >= 1000 and "home" in user.pw_dir]


def _groups_for_user(user_name):
    return [g.gr_name for g in grp.getgrall() if user_name in g.gr_mem]


def get_user_dict(path):
    """
    Function to generate user dictionary from inventory file
    """
    with open(path, "r") as f:
        content = json.load(f)
    return content


def generate_inventory(path, user_names=user_names()):
    """
    Function to generate inventory file from current state of system
    """
    users_list = []
    for user in user_names:
        user_dict = {}
        user_dict["name"] = user
        user_dict["groups"] = _groups_for_user(user)
        user_dict["password"] = spwd.getspnam(user).sp_pwd
        users_list.append(user_dict)
    with open(path, "w") as f:
        json.dump(users_list, f)
