import argparse
import asyncio

from github_dlr import __version__
from github_dlr.source import main


def cli():
    parser = argparse.ArgumentParser(
        prog="github-dlr",
        description="Download folders and files from Github.",
        epilog="Thanks for using github-dlr (❁´◡`❁)",
    )

    parser.add_argument(
        "github_path",
        help="Github directory full URL path",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Destination directory to download to",
        default="",
        metavar="",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    if args.github_path:
        print("\r")
        asyncio.run(main(args.github_path, output_dir=args.output))
