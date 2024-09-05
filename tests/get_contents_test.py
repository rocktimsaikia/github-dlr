# This file contains tests for `get_contents` which is responsible for
# getting the download urls for the content files of the provided GitHub URL.

import json

import pytest
from aiohttp import web

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


@pytest.mark.asyncio
async def test_get_contents_from_dir_success(aiohttp_client):
    # When the provided link is a directory with sub-contents
    # it should return all of it's contents as a list containing
    # the data in dict.
    content_url = "/repos/owner/repo/contents/path"

    async def mock_handler(request):
        return web.Response(
            body=json.dumps([content_api_response]), content_type="application/json"
        )

    app = web.Application()
    app.router.add_get(content_url, mock_handler)

    expected_content_data = [
        {
            "name": "README.md",
            "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
        }
    ]
    client = await aiohttp_client(app)
    content_url = client.make_url(content_url)

    content_data = await get_contents(content_url)
    assert content_data == expected_content_data


@pytest.mark.asyncio
async def test_get_content_from_file_success(aiohttp_client):
    # When the provided link is a file object itself.
    # it should return a dict instead of a list.
    content_url = "/repos/owner/repo/contents/path"

    async def mock_handler(request):
        return web.Response(
            body=json.dumps(content_api_response), content_type="application/json"
        )

    app = web.Application()
    app.router.add_get(content_url, mock_handler)

    expected_content_data = {
        "name": "README.md",
        "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
        "content_blob": "aGVsbG8gd29ybGQ=",
    }
    client = await aiohttp_client(app)
    content_url = client.make_url(content_url)

    content_data = await get_contents(content_url)
    assert content_data == expected_content_data
