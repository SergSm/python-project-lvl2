

def get_mspaces(depth):
    return ' ' * (depth * 4 - 2)


# def get_nicely_printed_data(data, depth):
#
#     # if d
#
#     astier = ''
#
#     count = 0
#     for x, y in dictionary.items():
#         count += 1
#
#         if type(y) is dict:
#
#             if not (depth == 0 and count == 1):
#                 astier += '\n'
#
#             astier += get_mspaces(depth) \
#                       + x \
#                       + ': {' \
#                       + '\n'
#
#             depth += 1
#
#             astier += get_nicely_printed_dict(y, depth) \
#                       + get_mspaces(depth) \
#                       + '\n' \
#                       + get_mspaces(depth) \
#                       + '}'
#         else:
#             astier += get_mspaces(depth) + str(x) + ': ' + str(y)
#             # if it is the last record in dict do not add newstring
#             if count < len(dictionary):
#                 astier += '\n'
#
#     return astier

def to_lowercase_bool(value):
    if type(value) is bool:
        return 'true' if value else 'false'
    else:
        return value


def render_data(data, nesting_level):

    handled_data = ""
    spaces = get_mspaces(nesting_level)

    if type(data) is list:
        handled_data += f'   {spaces}{data["KEY"]}: {{\n' \
                        f'{render_data(data["VALUE"], nesting_level)}' \
                        f'\n{spaces}}}'
    elif data["STATE"] == "CHILDREN":
        handled_data += f'   {spaces}{data["KEY"]}: {{\n' \
                        f'{render_data(data["VALUE"], nesting_level)}' \
                        f'\n{spaces}}}'
    elif "KEY" in data.keys():

        the_key = data["KEY"]
        value_left = to_lowercase_bool(data["VALUE_LEFT"]) if "VALUE_LEFT" in data.keys() else ''
        value_right = to_lowercase_bool(data["VALUE_RIGHT"]) if "VALUE_RIGHT" in data.keys() else ''
        value = to_lowercase_bool(data["VALUE"]) if "VALUE" in data.keys() else ''


        prefix = f'\n{spaces}'

        if data['STATE'] == 'ADDED':
            handled_data += f'{prefix}+ {the_key}: {value}'
        elif data['STATE'] == 'DELETED':
            handled_data += f'{prefix}- {the_key}: {value}'
        elif data['STATE'] == 'UNCHANGED':
            handled_data += f'{prefix}  {the_key}: {value}'
        elif data['STATE'] == 'CHANGED':
            handled_data += f'{prefix}- {the_key}: {value_left}'
            handled_data += f'{prefix}+ {the_key}: {value_right}'

    return handled_data


def get_children(record, nesting_level):

    # for a visual indentation purpose
    spaces = get_mspaces(nesting_level)
    prefix = f'\n{spaces}'

    text_diff = spaces + '{'
    ##########################################

    # if 'STATE' in record.keys():
    #     if not record['STATE'] == 'CHANGED':
    #         if type(record["VALUE"]) is dict:
    #             value_left = get_children(record["VALUE"], nesting_level + 1)
    #         elif type(record["VALUE"]) is list:
    #             value_left = render_data(record["VALUE"], nesting_level)
    #         else:
    #             value_left = record["VALUE"]
    #     elif record['STATE'] == 'CHANGED':
    #         value_left = record["VALUE_LEFT"]
    #         value_right = record["VALUE_RIGHT"]
    #         if type(value_left) is dict:
    #             value_left = get_children(record["VALUE_LEFT"], nesting_level + 1)
    #     else:
    #         value_left = record["VALUE"]
    #         value_right = ''
    # else:
    #     return record
    #

    value = record["VALUE"]

    if "VALUE_LEFT" in record.keys():
        value_left = record["VALUE_LEFT"]
    else:
        value_left = ''

    if "VALUE_RIGHT" in record.keys():
        value_right = record["VALUE_RIGHT"]
    else:
        value_right = ''

    the_key = record["KEY"]
    key_value = f'{the_key}: {value}'

    ##########################################

    if record['STATE'] == 'CHILDREN':
        text_diff += f'{prefix}   {key_value}'
    elif record['STATE'] == 'ADDED':
        text_diff += f'{prefix} + {key_value}'
    elif record['STATE'] == 'DELETED':
        text_diff += f'{prefix} - {key_value}'
    elif record['STATE'] == 'UNCHANGED':
        text_diff += f'{prefix}   {key_value}'
    elif record['STATE'] == 'CHANGED':
        text_diff += f'{prefix} - {key_value}'
        text_diff += f'{prefix} + {the_key}: {value_right}'

    #if nesting_level > 1:
    #text_diff += '\n' + get_mspaces(nesting_level) + '}'
    # else:
    #     text_diff += '\n' + '}'

    return text_diff


def get_render_stylish(data):

    root_node = data.get('ROOT')
    # kind of a guard expression
    # to save some spaces on indentation-levels
    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')
    #return get_children(root_node, nesting_level=0)

    text_diff = "{\n"

    for node in root_node:
        text_diff += render_data(node, nesting_level=0)

    text_diff += "\n}"

    return text_diff
