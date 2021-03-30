import pytest
from pathlib import Path

from gendiff import generate_diff


WORKING_DIR = Path(__file__).resolve().parent

FIXTURE_DIR = WORKING_DIR / 'fixtures'


def get_file(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


input_formats = ['json', 'yml']
output_formatters = ['stylish', 'plain', 'json']


input_cases = []
for input_format in input_formats:
    for output_format in output_formatters:
        input_cases.append(
            (f'file1_nested.{input_format}',
             f'file2_nested.{input_format}',
             f'file1_file2_reference_{output_format}',
             output_format))


@pytest.mark.parametrize('file1, file2, reference, formatter', input_cases)
def test_gendiff(file1, file2, reference, formatter):
    path_to_file_1 = FIXTURE_DIR / file1
    path_to_file_2 = FIXTURE_DIR / file2
    test_format = formatter

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)

    reference_result = get_file(FIXTURE_DIR / reference)

    assert comparison_result == reference_result


# special cases - when the gendiff is called without the specified
# parameter output_format
@pytest.mark.parametrize('input_format', input_formats)
def test_gendiff_no_formatter_specified(input_format):
    path_to_file_1 = FIXTURE_DIR / f'file1_nested.{input_format}'
    path_to_file_2 = FIXTURE_DIR / f'file2_nested.{input_format}'

    comparison_result_stylish = generate_diff(path_to_file_1,
                                              path_to_file_2)

    reference_result_stylish = get_file(FIXTURE_DIR / 'file1_file2_reference_stylish')

    assert comparison_result_stylish == reference_result_stylish
