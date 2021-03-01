
from gendiff import tree_description as t


def build_dif(dict1, dict2):

    result = []

    # convert to set to have only unique values
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    # sorted set of a union of all keys from both dictionaries
    all_keys = sorted(set().union(dict1_keys, dict2_keys))

    # handle common keys
    for key in all_keys:
        # key uniqueness checks
        if key not in list(dict1.keys()):  # new key
            row = {t.KEY: key,
                   t.VALUE: dict2[key],
                   t.STATE: t.ADDED}
        elif key not in list(dict2.keys()):  # deleted key
            row = {t.KEY: key,
                   t.VALUE: dict1[key],
                   t.STATE: t.DELETED}
        # same keys values checks
        elif (dict1[key] == dict2[key]) \
                and not type(dict1[key]) is dict\
                and not type(dict2[key]) is dict:
            row = {t.KEY: key,
                   t.VALUE: dict1[key],
                   t.STATE: t.UNCHANGED
                   }
        elif type(dict1[key]) is dict\
                and type(dict2[key]) is dict:  # both dictionaries
            row = {t.KEY: key,
                   t.VALUE: build_dif(dict1[key], dict2[key]),
                   t.STATE: t.CHILDREN,
                   }
        elif type(dict1[key]) is dict\
                and not type(dict2[key]) is dict:  # left value is a dictionary
            row = {t.KEY: key,
                   t.VALUE_LEFT: dict1[key],
                   t.VALUE_RIGHT: dict2[key],
                   t.STATE: t.CHANGED,
                   }
        elif not type(dict1[key]) is dict\
                and type(dict2[key]) is dict:  # right value is a dictionary
            row = {t.KEY: key,
                   t.VALUE_LEFT: dict1[key],
                   t.VALUE_RIGHT: dict2[key],
                   t.STATE: t.CHANGED,
                   }
        elif dict1[key] != dict2[key]:  # simple types, non-dictionary
            row = {t.KEY: key,
                   t.VALUE_LEFT: dict1[key],
                   t.VALUE_RIGHT: dict2[key],
                   t.STATE: t.CHANGED
                   }
        else:
            raise Exception("Impossible situation while comparing 2 files")

        result.append(row)

    return result


def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""
    return {'ROOT': build_dif(dict1, dict2)}
