"""Main module to be called by external code."""

import json

DEFAULT_FORMAT = 'json'


def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""

    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = dict1_keys.intersection(dict2_keys)

    # {-}
    keys_left = sorted(dict1_keys - dict2_keys)  # foreseeing the order change

    # {+}
    new_keys = sorted(dict2_keys - dict1_keys)

    # {-} {+} or { }
    unchanged, changed = set(), set()
    for key in shared_keys:
        if dict2[key] == dict1[key]:
            unchanged.add(key)
        else:
            changed.add(key)

    unchanged = sorted(unchanged)
    changed = sorted(changed)

    # compose the text difference using sets and dictionaries created earlier
    text_diff = '{'
    for key in keys_left:
        text_diff += f'\n - {key}: {dict1[key]}'

    for key in new_keys:
        text_diff += f'\n + {key}: {dict2[key]}'

    for key in unchanged:
        text_diff += f'\n   {key}: {dict1[key]}'

    for key in changed:
        text_diff += f'\n - {key}: {dict1[key]}'
        text_diff += f'\n + {key}: {dict2[key]}'

    text_diff += '\n}'

    return text_diff  # DEBUG


def get_comparison(first_file, second_file, format_type):

    if format_type == 'json':
        dict1 = json.load(open(first_file))
        dict2 = json.load(open(second_file))

        difference = get_difference(dict1, dict2)
    else:
        return f'unknown format {format_type}'

    return difference


def generate_diff(first_file, second_file, format_type=DEFAULT_FORMAT):
    """the main function of the library"""


    comparison_result = get_comparison(first_file,
                                       second_file,
                                       format_type)

    print(comparison_result)  # DEBUG

    return comparison_result
