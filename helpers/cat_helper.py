from helpers import *


def get_cats_info(path: str) -> list:
    """
    Read cat information from a file and return it as a list of dictionaries.

    :param path: Path to the file containing cat information.
    :return: List of dictionaries with cat information (id, name, age).
    """
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info

    except FileNotFoundError:
        print(Error.FILE_NOT_FOUND)
        return []