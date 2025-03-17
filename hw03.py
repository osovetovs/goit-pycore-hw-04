import sys
from pathlib import Path
from colorama import Fore, init

from helpers import *

init()

def print_directory_contents(path: Path, indent=0):
    """
    Recursively print the contents of a directory with colored output.

    :param path: Path to the directory.
    :param indent: Indentation level for recursive calls.
    """
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"{'  ' * indent}📂{item.name}/")
            print_directory_contents(item, indent + 1)
        else:
            print(Fore.GREEN + f"{'  ' * indent}📜{item.name}")

def main():
    """
    Main function to handle directory visualization.
    """
    if len(sys.argv) < 2:
        print("Usage: python hw03.py <directory_path>")
        return

    path = Path(sys.argv[1])

    if not path.exists() or not path.is_dir():
        print(Error.DIR_NOT_FOUND)
        return

    print_directory_contents(path)

if __name__ == "__main__":
    main()