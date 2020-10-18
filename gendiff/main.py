'''Main module to be called by external code.'''


DEFAULT_FORMAT = 'json'

# TODO
def read_to_dict():
    pass

# TODO
def get_difference(dict1, dict2):
    '''Return the difference between 2 dicts'''
    return {}  # DEBUG

def get_comparison(first_file, second_file, format_type):
    if format_type = 'json':
        dict1 = read_to_dict(first_file)
        dict2 = read_to_dict(second_file)

        difference = get_difference(dict1, dict2)

    else:
        return ""

def generate_diff(args):
    '''the main function of the library'''

    print(args)  # DEBUG
    format_type = DEFAULT_FORMAT if not args.format else args.format
    print(format_type)  # DEBUG

    comparison_result = get_comparison(args.first_file,
                                       args.second_file,
                                       format_type)
    return comparison_result
