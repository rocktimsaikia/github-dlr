import os

import pytest
from aiohttp import web

from github_dlr.source import download_content


@pytest.mark.asyncio
async def test_download_content_succes(aiohttp_client, tmp_path):
    # aiohttp expects the url path to start with '/' hence not passing
    # the full Github URL here.
    download_url = "/AnimeChan/animechan/tree/main/client/public"
    mock_content = b"This is an image content"

    # Create test server to mock the download URL
    async def mock_handler(request):
        return web.Response(body=mock_content)

    app = web.Application()
    app.router.add_get(download_url, mock_handler)

    client = await aiohttp_client(app)
    download_url = client.make_url(download_url)

    # Use tmp_path fixure to create temp file path
    output_file = os.path.join(tmp_path, "foo.txt")

    # Download the file content and save it locally
    await download_content(download_url, output_file)

    # Verify the file was written correctly
    with open(output_file, "rb") as file:
        assert file.read() == mock_content


@pytest.mark.asyncio
async def test_download_content_failure(aiohttp_client, tmp_path, capfd):
    download_url = "/AnimeChan/animechan/tree/main/client/public"

    # Create test server to mock the download URL
    async def mock_handler(request):
        return web.Response(status=404)

    app = web.Application()
    app.router.add_get(download_url, mock_handler)

    client = await aiohttp_client(app)
    download_url = client.make_url(download_url)

    # Create a temp dir `tmp` to store the test files
    output_file = os.path.join(tmp_path, "foo.txt")

    await download_content(download_url, output_file)

    captured_stdout = capfd.readouterr().out
    expected_stdout = f"Failed to download {download_url!r}. Skipping this file!"

    assert expected_stdout in captured_stdout
