def build_dif(dict1, dict2):

    result = []

    # convert to set to have only unique values
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = sorted(dict1_keys.intersection(dict2_keys))
    deleted_keys = sorted(dict1_keys - dict2_keys)  # {-}
    new_keys = sorted(dict2_keys - dict1_keys)  # {+}

    # handle deleted keys
    for key in deleted_keys:
        row = {'KEY': key,
               'VALUE': dict1[key],
               'STATE': 'DELETED'}
        result.append(row)

    # handle new keys
    for key in new_keys:
        row = {'KEY': key,
               'VALUE': dict2[key],
               'STATE': 'ADDED'}
        result.append(row)

    # handle common keys
    for key in shared_keys:

        if dict1[key] == dict2[key]:
            row = {'KEY': key,
                   'VALUE': dict1[key],
                   'STATE': 'UNCHANGED'
                   }
        elif type(dict1[key]) is dict\
                and type(dict2[key]) is dict:  # both dictionaries
            row = {'KEY': key,
                   'VALUE': build_dif(dict1[key], dict2[key]),
                   'STATE': 'CHILDREN',
                   }
        elif type(dict1[key]) is dict\
                and not type(dict2[key]) is dict:  # left value is a dictionary
            row = {'KEY': key,
                   'VALUE_LEFT': dict1[key],
                   'VALUE_RIGHT': dict2[key],
                   'STATE': 'CHANGED',
                   }
        elif not type(dict1[key]) is dict\
                and type(dict2[key]) is dict:  # right value is a dictionary
            row = {'KEY': key,
                   'VALUE_LEFT': dict1[key],
                   'VALUE_RIGHT': dict2[key],
                   'STATE': 'CHANGED',
                   }
        elif dict1[key] != dict2[key]:  # simple types, non-dictionary
            row = {'KEY': key,
                   'VALUE_LEFT': dict1[key],
                   'VALUE_RIGHT': dict2[key],
                   'STATE': 'CHANGED'
                   }

        result.append(row)

    return result


def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""

    result = {'KEY': 'ROOT',
              'VALUE': build_dif(dict1, dict2)
              }

    return result
