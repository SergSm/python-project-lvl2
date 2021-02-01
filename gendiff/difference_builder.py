def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""

    # convert to set to have only unique values
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())

    shared_keys = sorted(dict1_keys.intersection(dict2_keys))

    # {-}
    keys_left = sorted(dict1_keys - dict2_keys)

    # {+}
    new_keys = sorted(dict2_keys - dict1_keys)

    # {-} {+} or { }
    unchanged, changed = set(), set()

    for key in shared_keys:

        if type(dict1[key]) is dict\
                or type(dict2[key]) is dict:
            return get_difference(dict1[key], dict2[key])

        #if type(dict2[key]) is dict:


        if dict1[key] == dict2[key]

        if dict2[key] == dict1[key]:
            unchanged.add(key)
        else:
            changed.add(key)

    unchanged = sorted(unchanged)
    changed = sorted(changed)

    #
    if val1 != val2 and val2 has children

    return diff_tree  # DEBUG
