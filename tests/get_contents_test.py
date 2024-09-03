# This file contains tests for `get_contents` which is responsible for
# getting the download urls for the content files of the provided GitHub URL.

import pytest
import requests_mock

from github_dlr.source import get_contents


def test_get_contents_from_dir_success():
    # When the provided link is a directory with sub-contents
    # it should return all of it's contents as a list containing
    # the data in dict.
    # TODO: Write the tests
    pass


def test_get_content_from_file_success():
    # When the provided link is a file object itself.
    # it should return a dict instead of a list.
    # TODO: Write the tests
    pass
