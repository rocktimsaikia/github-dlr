# Github-dlr

Download files and folders from GitHub without cloning the whole repo.

[![Tests](https://github.com/rocktimsaikia/github-dlr/actions/workflows/tests.yml/badge.svg)](https://github.com/rocktimsaikia/github-dlr/actions/workflows/tests.yml)

[![Demo](https://github.com/user-attachments/assets/49e4068c-1090-4c9e-9b56-59388ff407a9)](https://github.com/user-attachments/assets/8927d4ef-f8e1-4699-b75b-b7e28291d509)

## Install

Requires Python 3.8+.

```sh
pip install github-dlr
```

Or with [pipx](https://pipx.pypa.io/):

```sh
pipx install github-dlr
```

## Usage

Pass any GitHub file or folder URL:

```sh
github-dlr https://github.com/makccr/wallpapers/blob/master/wallpapers/space
```

Use `-o` to choose an output directory (defaults to the current one):

```sh
github-dlr -o wallpapers https://github.com/makccr/wallpapers/blob/master/wallpapers/space
```

`gh-dlr` works as a shorter alias.

## License

[MIT](./LICENSE) &copy; [Rocktim Saikia](https://rocktimsaikia.dev) 2026
