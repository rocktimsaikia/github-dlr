import pytest

from github_dlr.source import normalize_github_url


def test_normalize_github_url():
    expected_result = {
        "owner": "AnimeChan",
        "repo": "animechan",
        "branch": "main",
        "target": "images",
        "target_path": "client/public",
    }
    result = normalize_github_url(
        "https://github.com/AnimeChan/animechan/tree/main/client/public/images"
    )
    assert result == expected_result


def test_normalize_github_url_case_insensetive():
    expected_result = {
        "owner": "AnimeChan",
        "repo": "animechan",
        "branch": "main",
        "target": "images",
        "target_path": "client/public",
    }
    result = normalize_github_url(
        "https://GITHUB.com/AnimeChan/animechan/tree/main/client/public/images"
    )
    assert result == expected_result


def test_normalize_github_url_spaces_around():
    expected_result = {
        "owner": "AnimeChan",
        "repo": "animechan",
        "branch": "main",
        "target": "images",
        "target_path": "client/public",
    }
    result = normalize_github_url(
        " https://GITHUB.com/AnimeChan/animechan/tree/main/client/public/images "
    )
    assert result == expected_result


def test_normalize_github_url_single_file():
    expected_result = {
        "owner": "AnimeChan",
        "repo": "animechan",
        "branch": "main",
        "target": "logo.png",
        "target_path": "client/public/images",
    }
    result = normalize_github_url(
        "https://github.com/AnimeChan/animechan/tree/main/client/public/images/logo.png"
    )
    assert result == expected_result


def test_normalize_github_url_invalid_url():
    with pytest.raises(ValueError, match="Not a valid Github URL"):
        normalize_github_url(
            "https://gitlab.com/AnimeChan/animechan/tree/main/client/public/images/logo.png"
        )
