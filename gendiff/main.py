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

    data1 = get_data(filepath1)
    data2 = get_data(filepath2)

    comparison_result_data = get_difference(data1, data2)
    rendered_result = get_formatted_result(comparison_result_data,
                                           output_format)
    return rendered_result
