import argparse
from github_dl import __version__

def cli():
    parser = argparse.ArgumentParser(
            prog="github-dl",
            description="Download folders and files from Github",
            epilog="Thanks for using github-dl!",
        )

    parser.add_argument("github_path", help="Github directory full URL path")
    parser.add_argument("--target", help="Target directory to download to")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    if args.github_path:
        print(args.github_path)
