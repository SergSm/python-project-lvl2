'''Script to run gendiff.'''

from gendiff.cli import get_arguments
from gendiff.main import generate_diff


def main():
    args = get_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))
    #generate_diff(args.first_file, args.second_file, args.format) # TODO remove


if __name__ == "__main__":
    main()
