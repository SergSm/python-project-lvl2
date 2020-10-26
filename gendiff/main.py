"""Main module to be called by external code."""

from gendiff.file_handler import get_file_extension, get_file_object
from gendiff.parser import get_parsed_data
from gendiff.difference_builder import get_difference


ACCEPTABLE_INPUT_FORMATS = ('JSON', 'YML', 'YAML')


def generate_diff(filepath1, filepath2, output_format):
    """the main function of the library"""

    file_ext1 = get_file_extension(filepath1).upper()
    file_ext2 = get_file_extension(filepath2).upper()

    if not (file_ext1, file_ext2 in ACCEPTABLE_INPUT_FORMATS):
        raise ValueError(f'Unknown format or file(s) has no extension(s)')

    file1 = get_file_object(filepath1)
    file2 = get_file_object(filepath2)

    data1 = get_parsed_data(file1, output_format)
    data2 = get_parsed_data(file2, output_format)

    # print(data1)  # DEBUG
    # print(data2)  # DEBUG

    comparison_result = get_difference(data1, data2)

    print(comparison_result)  # DEBUG2
    return comparison_result
