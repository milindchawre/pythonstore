import pytest
import crypt
import subprocess
from hr import users

password = crypt.crypt("password", crypt.mksalt(crypt.METHOD_SHA512))


@pytest.fixture
def user_dict():
    user = {"name": "luther123", "groups": ["wheel", "dev"], "password": password}
    return user


def test_check_valid_user(user_dict):
    """
    test whether valid user exists
    """
    assert users.check_valid_user(user_dict) is False


def test_create_user(user_dict, mocker):
    """
    test new user creation
    """
    mocker.patch("subprocess.run")
    users.create_user(user_dict)
    groups = ",".join(user_dict["groups"])
    subprocess.run.assert_called_with(["useradd", "-p", user_dict["password"], "-G", groups, user_dict["name"]])


def test_update_user(user_dict, mocker):
    """
    test update user
    """
    mocker.patch("subprocess.run")
    users.update_user(user_dict)
    groups = ",".join(user_dict["groups"])
    subprocess.run.assert_called_with(
        ["usermod", "-l", user_dict["name"], "-G", groups, "-p", user_dict["password"], user_dict["name"]]
    )


def test_remove_user(user_dict, mocker):
    """
    test remove user
    """
    mocker.patch("subprocess.run")
    username = user_dict["name"]
    users.remove_user(username)
    subprocess.run.assert_called_with(["userdel", "-r", username])
