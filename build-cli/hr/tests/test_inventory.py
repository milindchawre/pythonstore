import tempfile
from hr import inventory


def test_get_user_dict():
    """
    Test the user dictionary creation from inventory file
    """
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(b'[{"name": "kevin"},{"name": "john"}]')
    fp.close()
    user_list = inventory.get_user_dict(fp.name)
    assert user_list[0] == {"name": "kevin"}
    assert user_list[1] == {"name": "john"}


def test_gnerate_inventory(mocker):
    """
    `generate_inventory` takes a destination path and optional list of users to export then exports the existing user information. # noqa
    """
    dest_file = tempfile.NamedTemporaryFile(delete=False)
    dest_file.close()

    # spwd.getspnam can't be used by non-root user normally.
    # Mock the implementation so that we can test.
    mocker.patch("spwd.getspnam", return_value=mocker.Mock(sp_pwd="password"))

    # grp.getgrall will return the values from the test machine.
    # To get consistent results we need to mock this.
    mocker.patch(
        "grp.getgrall",
        return_value=[
            mocker.Mock(gr_name="star", gr_mem=["robin"]),
            mocker.Mock(gr_name="other", gr_mem=[]),
            mocker.Mock(gr_name="class", gr_mem=["robin", "mike"]),
        ],
    )

    inventory.generate_inventory(dest_file.name, ["mike", "robin"])

    with open(dest_file.name) as f:
        assert (
            f.read()
            == """[{"name": "mike", "groups": ["class"], "password": "password"}, {"name": "robin", "groups": ["star", "class"], "password": "password"}]"""  # noqa
        )
