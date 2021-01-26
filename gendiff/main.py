"""Main module to be called by external code."""

from gendiff.file_handler import get_file_extension, get_file_object
from gendiff.parser import get_parsed_data
from gendiff.difference_builder import get_difference


ACCEPTABLE_INPUT_EXTENSIONS = ('.JSON', '.YML', '.YAML')
ACCEPTABLE_OUTPUT_FORMATTERS = ('stylish',)


def generate_diff(filepath1, filepath2, output_format):
    """the main function of the library"""

    file_ext1 = get_file_extension(filepath1).upper()
    file_ext2 = get_file_extension(filepath2).upper()

    if not (file_ext1, file_ext2 in ACCEPTABLE_INPUT_EXTENSIONS):
        raise ValueError(f'Unknown file extension "{file_ext1}",'
                         f' "{file_ext2}" or file(s) has no extension(s)')

    file1 = get_file_object(filepath1)
    file2 = get_file_object(filepath2)

    data1 = get_parsed_data(file1, file_ext1)
    data2 = get_parsed_data(file2, file_ext2)

    # TODO: separate a diff building and rendering a result
    comparison_result = get_difference(data1, data2)

    # Console output
    # diff_text_representatiuon = get_formatted_text(FROMATTER_ARG)
    ###

    print(comparison_result)  # DEBUG

    return comparison_result
