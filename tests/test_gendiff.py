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
                             output_format,
                             f'file1_file2_reference_{output_format}')
                          )


@pytest.mark.parametrize('file1, file2, formatter, reference', input_cases)
def test_gendiff(file1, file2, formatter, reference):
    path_to_file_1 = FIXTURE_DIR / file1
    path_to_file_2 = FIXTURE_DIR / file2
    test_format = formatter

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)
    comparison_result = comparison_result.replace('\n', '')

    reference_result = get_file(FIXTURE_DIR / reference)
    reference_result = reference_result.replace('\n', '')

    assert comparison_result == reference_result
