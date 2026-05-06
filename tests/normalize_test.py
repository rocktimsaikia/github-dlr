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


def test_normalize_github_url_percent_encoded_space_in_target():
    # Browser address bar produces %20-encoded URLs. The decoded form is what
    # we want on disk and what aiohttp will (re-)encode for the API call.
    expected_result = {
        "owner": "ipython",
        "repo": "ipython",
        "branch": "main",
        "target": "IPython Kernel",
        "target_path": "examples",
    }
    result = normalize_github_url(
        "https://github.com/ipython/ipython/tree/main/examples/IPython%20Kernel"
    )
    assert result == expected_result


def test_normalize_github_url_literal_space_in_target():
    expected_result = {
        "owner": "ipython",
        "repo": "ipython",
        "branch": "main",
        "target": "IPython Kernel",
        "target_path": "examples",
    }
    result = normalize_github_url(
        "https://github.com/ipython/ipython/tree/main/examples/IPython Kernel"
    )
    assert result == expected_result


def test_normalize_github_url_encoded_chars_in_intermediate_path():
    expected_result = {
        "owner": "owner",
        "repo": "repo",
        "branch": "main",
        "target": "file.txt",
        "target_path": "my docs/sub dir",
    }
    result = normalize_github_url(
        "https://github.com/owner/repo/tree/main/my%20docs/sub%20dir/file.txt"
    )
    assert result == expected_result


def test_normalize_github_url_non_ascii_target():
    # Cyrillic "документы" — encoded form is what GitHub serves in the address bar.
    expected_result = {
        "owner": "owner",
        "repo": "repo",
        "branch": "main",
        "target": "документы",
        "target_path": "src",
    }
    result = normalize_github_url(
        "https://github.com/owner/repo/tree/main/src/%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B"
    )
    assert result == expected_result


def test_normalize_github_url_special_chars_in_target():
    # Parentheses and `+` — common in C++/sample folder names.
    expected_result = {
        "owner": "owner",
        "repo": "repo",
        "branch": "main",
        "target": "C++ (samples)",
        "target_path": "src",
    }
    result = normalize_github_url(
        "https://github.com/owner/repo/tree/main/src/C%2B%2B%20%28samples%29"
    )
    assert result == expected_result
