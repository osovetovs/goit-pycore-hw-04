from helpers import *


def total_salary(path: str) -> tuple:
    """
    Calculate the total and average salary from a file.

    :param path: Path to the file containing salary information.
    :return: Tuple containing total and average salaries.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [
                int(line.strip().split(',')[1])
                for line in file if line.strip()
            ]

        if not salaries:
            return 0, 0

        total = sum(salaries)
        average = total / len(salaries)

        return total, average

    except FileNotFoundError:
        print(Error.FILE_NOT_FOUND)
        return 0, 0

    except (ValueError, IndexError):
        print(Error.INVALID_DATA_FORMAT)
        return 0, 0