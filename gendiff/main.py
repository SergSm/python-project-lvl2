'''Main module to be called by external code.'''

import json

DEFAULT_FORMAT = 'json'


# TODO
def get_difference(dict1, dict2):
    '''Return the difference between 2 dicts'''

    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = dict1_keys.intersection(dict2_keys)

    # {-}
    keys_left = dict1_keys - dict2_keys

    # {+}
    new_keys = dict2_keys - dict1_keys

    # {-} {+} or { }
    unchanged = set()
    changed = set()
    for key in shared_keys:
        if dict2[key] == dict1[key]:
            unchanged.add(key)
        else:
            changed.add(key)

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
        
    text_diff += f'\n'
    text_diff += '}'

    return text_diff  # DEBUG

def get_comparison(first_file, second_file, format_type):
    if format_type == 'json':
        dict1 = json.load(open(first_file))
        dict2 = json.load(open(second_file))

        difference = get_difference(dict1, dict2)
    else:
        return ""

    return difference

def generate_diff(args):
    '''the main function of the library'''

    format_type = DEFAULT_FORMAT if not args.format else args.format

    # TODO: absolute and relative pathes

    comparison_result = get_comparison(args.first_file,
                                       args.second_file,
                                       format_type)
    print(comparison_result)  # DEBUG
    return comparison_result
