import os
import shutil

from github_dlr.source import download_content


def test_download_content_succes(requests_mock):
    download_url = "https://github.com/AnimeChan/animechan/tree/main/client/public"
    mock_content = b"This is an image content"

    requests_mock.get(download_url, content=mock_content)

    # Create a temp dir `tmp` to store the test files
    output_dir = "tmp"
    output_file = os.path.join(output_dir, "foo.txt")
    os.makedirs(output_dir)

    # Download the file content and save it locally
    download_content(download_url, output_file)

    try:
        # Verify the file was written correctly
        with open(output_file, "rb") as file:
            assert file.read() == mock_content
    finally:
        if os.path.exists(output_file):
            shutil.rmtree(output_dir)
