# Github-dlr

Download individual files and folders from GitHub recursively.

[![Tests](https://github.com/rocktimsaikia/github-dlr/actions/workflows/tests.yml/badge.svg)](https://github.com/rocktimsaikia/github-dlr/actions/workflows/tests.yml)

[![Demo](https://github.com/user-attachments/assets/49e4068c-1090-4c9e-9b56-59388ff407a9)](https://github.com/user-attachments/assets/8927d4ef-f8e1-4699-b75b-b7e28291d509)

## Motivation

The project aims to save time and resources by allowing users to download only the specific folders and files they need from a GitHub repository, without the hassle of cloning the entire repo. It's designed for efficiency, making development and learning more streamlined.

## Install

Requires Python version 3.8 or higher.

```sh
pip install github-dlr
```

or using [pipx](https://pipx.pypa.io/)

```sh
pipx install github-dlr
```

## Usage

> [!NOTE]
> Using the tool is straightforward, copy the GitHub URL of the target repository folder and paste it after the command `github-dlr` or it's alias `gh-dlr`.

```sh
github-dlr <github_path>

# Basic Example
github-dlr https://github.com/makccr/wallpapers/blob/master/wallpapers/space
```

> [!NOTE]
> By default it will download the entire folder from GitHub and place in the current directory from where the command is being executed. If you want to specify a different output directory, you can do it via the `--output` or `-o` flag.

```sh
github-dlr --output wallpapers https://github.com/makccr/wallpapers/blob/master/wallpapers/space
```

\
Find all available options using `--help`

```sh
usage: github-dlr [-h] [-o] [-v] github_path

Download folders and files from Github.

positional arguments:
  github_path     Github directory full URL path

options:
  -h, --help      show this help message and exit
  -o, --output   Destination directory to download to
  -v, --version   show program version number and exit

Thanks for using github-dlr!
```

## LICENSE

[MIT](./LICENSE) License &copy; [Rocktim Saikia](https://rocktimsaikia.dev) 2025
