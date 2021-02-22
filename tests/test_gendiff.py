from pathlib import Path

from gendiff import generate_diff


WORKING_DIR = Path(__file__).resolve().parent

FIXTURE_DIR = WORKING_DIR / 'fixtures'


def get_file(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content


def do_comparison(file1, file2, formatter, reference):
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


def test_comparison_json_in_stylish_out():
    do_comparison('file1_nested.json',
                  'file2_nested.json',
                  'stylish',
                  'file1_file2_reference_stylish')


def test_comparison_yml_in_stylish_out():
    do_comparison('file1_nested.yml',
                  'file2_nested.yml',
                  'stylish',
                  'file1_file2_reference_stylish')


def test_comparison_json_in_plain_out():
    do_comparison('file1_nested.json',
                  'file2_nested.json',
                  'plain',
                  'file1_file2_reference_plain')


def test_comparison_yml_in_plain_out():
    do_comparison('file1_nested.yml',
                  'file2_nested.yml',
                  'plain',
                  'file1_file2_reference_plain')


def test_comparison_json_in_json_out():
    do_comparison('file1_nested.json',
                  'file2_nested.json',
                  'json',
                  'file1_file2_reference_json')


def test_comparison_yml_in_json_out():
    do_comparison('file1_nested.yml',
                  'file2_nested.yml',
                  'json',
                  'file1_file2_reference_json')
