"""Main module to be called by external code."""

from gendiff.file_handler import get_file_format, open_if_files_exists
from gendiff.parser import parse
from gendiff.difference_builder import get_difference
from gendiff.formatters.render import get_formatted_result


def get_data(filepath):
    data = open_if_files_exists(filepath)
    input_format = get_file_format(filepath).upper()
    return parse(data, input_format)


def generate_diff(filepath1, filepath2, output_format="stylish"):
    """the main function of the library"""

    # file_ext1 = get_file_extension(filepath1).upper()
    # file_ext2 = get_file_extension(filepath2).upper()
    #
    # if not (file_ext1, file_ext2 in ACCEPTABLE_INPUT_EXTENSIONS):
    #     raise ValueError(f'Unknown file extension "{file_ext1}",'
    #                      f' "{file_ext2}" or file(s) has no extension(s)')

    # file1 = get_file(filepath1)
    # file2 = get_file(filepath2)

    # data1 = parse(file1, format=file_ext1[1:])
    # data2 = parse(file2, format=file_ext2[1:])
    data1 = get_data(filepath1)
    data2 = get_data(filepath2)

    comparison_result_data = get_difference(data1, data2)
    rendered_result = get_formatted_result(comparison_result_data,
                                           output_format)
    return rendered_result
