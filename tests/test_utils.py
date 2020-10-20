from unittest.mock import patch, mock_open

from flore.utils import open_yaml_file


def test_open_yaml_file():
    with patch("builtins.open", mock_open(read_data="pg")):
        f = open_yaml_file("config.yaml")
        assert f == "pg"
