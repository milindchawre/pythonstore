import pytest
from urlgetter import cli

@pytest.fixture
def parser():
    return cli.create_parser()

def test_invalid_response_type(parser):
    """
    Verify response type is only HTML or JSON
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["https://www.google.com/", "./somefile", "text"])

