import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Generate diff")

    # positional arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # optional arguments shor and long forms
    parser.add_argument('-f',
                        '--format',
                        help="set format of output",
                        default='stylish'
                        )

    args = parser.parse_args()

    return args
