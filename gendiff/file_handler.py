"""Read file from disk and return file object"""

from pathlib import Path


def get_file_extension(filepath):
    """Returns file extension without dot"""
    return Path(filepath).suffix


def get_file(filepath):

    path = Path(filepath)

    if path.is_file():
        return open(filepath)
    else:
        raise ValueError(f'File doesn\'t exit at: {filepath}')
