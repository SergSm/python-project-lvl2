"""Main module to be called by external code."""

from gendiff.file_handler import get_file_extension, get_file
from gendiff.parser import get_parsed_data
from gendiff.difference_builder import get_difference
from gendiff.formatters.render import get_formatted_string


ACCEPTABLE_INPUT_EXTENSIONS = ('.JSON', '.YML', '.YAML')


def generate_diff(filepath1, filepath2, output_format="stylish"):
    """the main function of the library"""

    file_ext1 = get_file_extension(filepath1).upper()
    file_ext2 = get_file_extension(filepath2).upper()

    if not (file_ext1, file_ext2 in ACCEPTABLE_INPUT_EXTENSIONS):
        raise ValueError(f'Unknown file extension "{file_ext1}",'
                         f' "{file_ext2}" or file(s) has no extension(s)')

    file1 = get_file(filepath1)
    file2 = get_file(filepath2)

    data1 = get_parsed_data(file1, format_type=file_ext1[1:])
    data2 = get_parsed_data(file2, format_type=file_ext2[1:])

    comparison_result_data = get_difference(data1, data2)

    comparison_result = get_formatted_string(comparison_result_data,
                                             output_format)
    return comparison_result
