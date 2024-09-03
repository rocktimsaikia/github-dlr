import os

from github_dlr.source import download_content


def test_download_content_succes(requests_mock, tmp_path):
    download_url = "https://github.com/AnimeChan/animechan/tree/main/client/public"
    mock_content = b"This is an image content"

    requests_mock.get(download_url, content=mock_content)

    # Use tmp_path fixure to create temp file path
    output_file = os.path.join(tmp_path, "foo.txt")
    print(output_file)

    # Download the file content and save it locally
    download_content(download_url, output_file)

    # Verify the file was written correctly
    with open(output_file, "rb") as file:
        assert file.read() == mock_content


def test_download_content_failure(requests_mock, tmp_path, capfd):
    download_url = "https://github.com/AnimeChan/animechan/tree/main/client/public"

    requests_mock.get(download_url, status_code=404)

    # Create a temp dir `tmp` to store the test files
    output_file = os.path.join(tmp_path, "foo.txt")
    print(output_file)

    download_content(download_url, output_file)

    captured_stdout = capfd.readouterr().out
    expected_stdout = f"Failed to download {download_url!r}. Skipping this file!"

    assert expected_stdout in captured_stdout
