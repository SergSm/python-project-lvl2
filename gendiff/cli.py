import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate diff")

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    print(args.echo)
