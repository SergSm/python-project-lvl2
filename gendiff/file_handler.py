"""Read file from disk and return file object"""

from pathlib import Path


def get_file_extension(filepath):
    return Path(filepath).suffix


def get_file_object(filepath):

    path = Path(filepath)

    if path.is_file():
        return open(filepath)
    else:
        raise ValueError(f'File doesn\'t exit at: {filepath}')
