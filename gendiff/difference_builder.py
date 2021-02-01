def build_dif(dict1, dict2):

    result = []

    # convert to set to have only unique values
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = sorted(dict1_keys.intersection(dict2_keys))
    deleted_keys = sorted(dict1_keys - dict2_keys) # {-}
    new_keys = sorted(dict2_keys - dict1_keys) # {+}

    # handle deleted keys
    for key in deleted_keys:
        row = {'key':key,
               'value': dict1[key],
               'state': 'DELETED'}
        result.append(row)

    # handle new keys
    for key in new_keys:
        row = {'key': key,
               'value': dict2[key],
               'state': 'ADDED'}
        result.append(row)

    # handle common keys
    for key in shared_keys:
        ############################################################
        # value1 == value2              | not dict                 #
        # value1 != value2              | not dict changed -+      #
        # value1 is dict                                           #
        #       AND value 2 is dict     | call build_dif           #
        # value1 is dict                                           #
        #       AND value 2 is not dict | -+changed call build_diff#
        # value1 is NOT dict                                       #
        #       AND value 2 is dict     | -+changed call build_diff#
        ############################################################

        if dict1[key] == dict2[key]:
            row = {'key': key,
                   'value': dict1[key],
                   'state': 'UNCHANGED'
                   }
        # TODO: check if only one of them is a dict
        elif type(dict1[key]) is dict\
                or type(dict2[key]) is dict:
            row = {'key': key,
                   'value': build_dif(dict1[key], dict2[key]),
                   'state': 'PARENT',
                   }
        elif dict1[key] != dict2[key]:  # simple types, non-dictionary
            row = {'key': key,
                   'value_left': dict1[key],
                   'value_right': dict2[key],
                   'state': 'CHANGED'
                   }

        result.append(row)

    return result


def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""

    result = {'key': 'root',
              'value': build_dif(dict1, dict2)
              }

    return result