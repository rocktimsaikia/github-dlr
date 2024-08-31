import os
from urllib.parse import urlparse

import requests


def normalize_github_url(github_url):
    """Normalize the provided Github directory path into a dict."""

    parsed_url = urlparse(github_url)
    github_path = parsed_url.path.split("/")
    owner = github_path[1]
    repo = github_path[2]
    branch = github_path[4]
    target = github_path[-1]
    target_path = "/".join(github_path[5:-1])
    return {
        "owner": owner,
        "repo": repo,
        "branch": branch,
        "target": target,
        "target_path": target_path,
    }


def get_contents(content_url):
    """Extract all contents of given content url and return a 1D array."""

    response = requests.get(content_url)
    download_urls = []
    if response.ok:
        response = response.json()
        for resp in response:
            content_name = resp.get("name")
            content_type = resp.get("type")
            content_self_url = resp.get("url")
            content_download_url = resp.get("download_url")
            if content_type == "dir":
                sub_content = get_contents(content_self_url)
                for sub_item in sub_content:
                    sub_item["name"] = f"{content_name}/{sub_item.get('name')}"
                    download_urls.append(sub_item)
            elif content_type == "file":
                download_urls.append(
                    {"name": content_name, "download_url": content_download_url}
                )
        return download_urls


def main(github_url, outputDir=None):
    """Main function."""

    repo_data = normalize_github_url(github_url)
    owner = repo_data.get("owner")
    repo = repo_data.get("repo")
    branch = repo_data.get("branch")
    root_target_dir = repo_data.get("target")
    target_path = repo_data.get("target_path") + "/" + root_target_dir

    content_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{target_path}?ref={branch}"
    contents = get_contents(content_url)

    # Create the target directory first.
    root_target_dir = os.path.join(outputDir, root_target_dir)
    os.makedirs(root_target_dir, exist_ok=True)

    for content in contents:
        content_path = content.get("name")
        download_url = content.get("download_url")

        if download_url is None:
            continue

        # Extract the parent directory path and file from the current
        # 'content_path' and properly join with root target directory.
        content_parentdir = os.path.dirname(content_path)
        content_parentdir = os.path.join(root_target_dir, content_parentdir)
        content_filename = os.path.join(root_target_dir, content_path)

        os.makedirs(content_parentdir, exist_ok=True)

        resp = requests.get(download_url)
        resp_content = resp.content

        print(content_filename)
        with open(content_filename, mode="wb") as file:
            file.write(resp_content)

    print(f"Downloaded {root_target_dir}")
