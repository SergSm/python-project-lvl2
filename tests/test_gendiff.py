import pytest

from pathlib import Path

from gendiff import generate_diff


WORKING_DIR = Path(__file__).resolve().parent

FIXTURE_DIR = WORKING_DIR / 'fixtures'


def get_file(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def test_comparison_json():

    path_to_file_1 = FIXTURE_DIR / 'file1.json'
    path_to_file_2 = FIXTURE_DIR / 'file2.json'
    test_format = 'json'

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)
    comparison_result = comparison_result.replace('\n', '')

    reference_result = get_file(FIXTURE_DIR / 'file1_file2_reference')
    reference_result = reference_result.replace('\n', '')

    assert comparison_result == reference_result


def test_comparison_yml():

    path_to_file_1 = FIXTURE_DIR / 'file1.yml'
    path_to_file_2 = FIXTURE_DIR / 'file2.yml'
    test_format = 'yml'

    comparison_result = generate_diff(path_to_file_1,
                                      path_to_file_2,
                                      test_format)
    comparison_result = comparison_result.replace('\n', '')

    reference_result = get_file(FIXTURE_DIR / 'file1_file2_reference')
    reference_result = reference_result.replace('\n', '')

    assert comparison_result == reference_result
