def get_difference(dict1, dict2):
    """Return the difference between 2 dicts"""




    # convert to set to have only unique values
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

    #
    if val1 != val2 and val2 has children

    return diff_tree  # DEBUG
