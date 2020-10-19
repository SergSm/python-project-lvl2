'''Main module to be called by external code.'''

import json

DEFAULT_FORMAT = 'json'


# TODO
def get_difference(dict1, dict2):
    '''Return the difference between 2 dicts'''

    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = dict1_keys.intersection(dict2_keys)
    print("shared_keys")  # DEBUG
    print(shared_keys)

    new_keys = dict1_keys - dict2_keys
    print("new_keys")
    print(new_keys)

    shared_items = {k: dict1[k] for k in dict1
                    if k in dict2 and dict1[k] == dict2[k]}

    return {}  # DEBUG

def get_comparison(first_file, second_file, format_type):
    if format_type == 'json':
        dict1 = json.load(open(first_file))
        print(dict1) # DEBUG
        dict2 = json.load(open(second_file))
        print(dict2) # DEBUG

        difference = get_difference(dict1, dict2)

    else:
        return ""

def generate_diff(args):
    '''the main function of the library'''

    print(args)  # DEBUG
    format_type = DEFAULT_FORMAT if not args.format else args.format
    print(format_type)  # DEBUG

    # TODO: absolute and relative pathes

    comparison_result = get_comparison(args.first_file,
                                       args.second_file,
                                       format_type)
    print(comparison_result)  # DEBUG
    return comparison_result
