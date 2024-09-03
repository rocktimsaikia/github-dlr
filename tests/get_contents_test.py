# This file contains tests for `get_contents` which is responsible for
# getting the download urls for the content files of the provided GitHub URL.

from github_dlr.source import get_contents

content_api_response = {
    "type": "file",
    "encoding": "base64",
    "size": 5362,
    "name": "README.md",
    "path": "README.md",
    "content": "aGVsbG8gd29ybGQ=",
    "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
    "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
    "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
    "_links": {
        "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
        "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
        "html": "https://github.com/octokit/octokit.rb/blob/master/README.md",
    },
}


def test_get_contents_from_dir_success(requests_mock):
    # When the provided link is a directory with sub-contents
    # it should return all of it's contents as a list containing
    # the data in dict.
    content_url = "https://api.github.com/repos/owner/repo/contents/path"
    requests_mock.get(content_url, json=[content_api_response])

    expected_content_data = [
        {
            "name": "README.md",
            "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
        }
    ]
    content_data = get_contents(content_url)
    assert content_data == expected_content_data
    pass


def test_get_content_from_file_success(requests_mock):
    # When the provided link is a file object itself.
    # it should return a dict instead of a list.
    content_url = "https://api.github.com/repos/owner/repo/contents/path"
    requests_mock.get(content_url, json=content_api_response)

    expected_content_data = {
        "name": "README.md",
        "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
        "content_blob": "aGVsbG8gd29ybGQ=",
    }
    content_data = get_contents(content_url)
    assert content_data == expected_content_data
