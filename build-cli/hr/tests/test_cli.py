import pytest
from hr import cli


@pytest.fixture
def parser():
    return cli.create_parser()


def test_no_argument(parser):
    """
    Should error out if no argument passed
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_argument_pass(parser):
    """
    Should run proper with argument
    """
    args = parser.parse_args(["/some/path/to/file.txt"])
    assert args.path == "/some/path/to/file.txt"


def test_argument_export(parser):
    """
    Test --export flag
    """
    args = parser.parse_args(["/some/path/to/file.txt"])
    assert args.export is False
    args = parser.parse_args(["/some/path/to/file.txt", "--export"])
    assert args.export is True
