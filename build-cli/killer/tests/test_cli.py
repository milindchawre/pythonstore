import pytest
from killer import cli


@pytest.fixture
def parser():
    return cli.create_parser()


def test_valid_port_number(parser):
    """
    Parser should exit out if port number is invalid (< 0)
    """
    args = parser.parse_args(["-1"])
    with pytest.raises(SystemExit):
        cli.is_valid_port(args.port_number)
