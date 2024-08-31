from github_dl.source import normalize_github_url


def test_normalize_github_url():
    expected_result = {
        "owner": "D3Ext",
        "repo": "aesthetic-wallpapers",
        "branch": "main",
        "target": "images",
        "target_path": "",
    }
    result = normalize_github_url(
        "https://github.com/D3Ext/aesthetic-wallpapers/tree/main/images"
    )
    assert result == expected_result
