def get_formatted_string(data, formatter):

    if formatter == "stylish":
        return get_stylish(data)
    else:
        return "unknown formatter string"


# TODO:
def get_stylish(data):

    # compose the text difference using sets and dictionaries created earlier
    # text_diff = '{'
    # for key in keys_left:
    #     text_diff += f'\n - {key}: {dict1[key]}'
    #
    # for key in new_keys:
    #     text_diff += f'\n + {key}: {dict2[key]}'
    #
    # for key in unchanged:
    #     text_diff += f'\n   {key}: {dict1[key]}'
    #
    # for key in changed:
    #     text_diff += f'\n - {key}: {dict1[key]}'
    #     text_diff += f'\n + {key}: {dict2[key]}'
    #
    # text_diff += '\n}'

    return str(data)
