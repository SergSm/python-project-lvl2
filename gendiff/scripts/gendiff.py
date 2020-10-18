'''Script to run gendiff.'''

from gendiff.cli import get_arguments
from gendiff.main import generate_diff

def main():
    args = get_arguments()
    generate_diff(args)


if __name__ == "__main__":
    main()
