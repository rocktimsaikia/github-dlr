# Github-dl

Download individual files and folders from Github without needing to clone the entire repo.

[![Tests](https://github.com/rocktimsaikia/github-dl/actions/workflows/tests.yml/badge.svg)](https://github.com/rocktimsaikia/github-dl/actions/workflows/tests.yml)

## Motivation

The project aims to save time and resources by allowing users to download only the specific folders and files they need from a GitHub repository, without the hassle of cloning the entire repo. It's designed for efficiency, making development and learning more streamlined.

## Install

```sh
pip install github-dl
```

or using [pipx](https://pipx.pypa.io/)

```sh
pipx install cambd
```

## Usage

> Using the tool is straightforward, copy the Github URL of the target repository folder and paste it after the command `github-dl` or it's alias `gh-dl`.

```sh
github-dl <github_path>

# Basic Example
github-dl https://github.com/linuxdotexe/nordic-wallpapers/tree/master/dynamic-wallpapers/Coast
```

By default it will download the entire folder from Github and place in the current directory from where the command is being executed. If you want to specify a different output directory, you can do it via the `--output` or `-o` flag.

```sh
github-dl --output wallpapers https://github.com/linuxdotexe/nordic-wallpapers/tree/master/dynamic-wallpapers/Coast
```

\
Find all available options using `--help`

```sh
usage: github-dl [-h] [-o] [-v] github_path

Download folders and files from Github.

positional arguments:
  github_path     Github directory full URL path

options:
  -h, --help      show this help message and exit
  -o , --output   Destination directory to download to
  -v, --version   show program version number and exit

Thanks for using github-dl!
```

## LICENSE

[MIT](./LICENSE) License &copy; [Rocktim Saikia](https://rocktimsaikia.dev) 2024
