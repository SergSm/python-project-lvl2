import pytest

from pathlib import Path

from gendiff import generate_diff


WORKING_DIR = Path(__file__).resolve().parent

FIXTURE_DIR = WORKING_DIR / 'fixtures'


def get_file(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def test_comparison_json_in_stylish_out():

    path_to_file_1 = FIXTURE_DIR / 'file1_nested.json'
    path_to_file_2 = FIXTURE_DIR / 'file2_nested.json'
    test_format = 'stylish'

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)
    comparison_result = comparison_result.replace('\n', '')

    reference_result = get_file(FIXTURE_DIR / 'file1_file2_reference_stylish')
    reference_result = reference_result.replace('\n', '')

    assert comparison_result == reference_result


def test_comparison_yml_in_stylish_out():

    path_to_file_1 = FIXTURE_DIR / 'file1_nested.yml'
    path_to_file_2 = FIXTURE_DIR / 'file2_nested.yml'
    test_format = 'stylish'

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)
    comparison_result = comparison_result.replace('\n', '')

    reference_result = get_file(FIXTURE_DIR / 'file1_file2_reference_stylish')
    reference_result = reference_result.replace('\n', '')

    assert comparison_result == reference_result

