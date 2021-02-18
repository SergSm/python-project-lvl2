

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


def render_data(data, nesting_level):

    handled_data = ''+get_mspaces(nesting_level) + '{' + '\n'

    if type(data) is list:
        for record in data:
            handled_data += render_data(record, nesting_level + 1)
    elif type(data) is dict:
        handled_data += get_children(data, nesting_level + 1)

    handled_data += get_mspaces(nesting_level) + handled_data + '\n' + '}'

    return handled_data


def get_children(record, nesting_level):

    # for a visual indentation purpose
    spaces = get_mspaces(nesting_level)
    prefix = f'\n{spaces}'

    text_diff = spaces + '{'
    ##########################################

    if 'STATE' in record.keys():
        if not record['STATE'] == 'CHANGED':
            if type(record["VALUE"]) is dict:
                value_left = get_children(record["VALUE"], nesting_level + 1)
            elif type(record["VALUE"]) is list:
                value_left = render_data(record["VALUE"], nesting_level)
            else:
                value_left = record["VALUE"]
        elif record['STATE'] == 'CHANGED':
            value_left = record["VALUE_LEFT"]
            value_right = record["VALUE_RIGHT"]
            if type(value_left) is dict:
                value_left = get_children(record["VALUE_LEFT"], nesting_level + 1)
        else:
            value_left = record["VALUE"]
            value_right = ''
    else:
        return record

    the_key = record["KEY"]
    key_value = f'{the_key}: {value_left}'

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
    text_diff += '\n' + get_mspaces(nesting_level) + '}'
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
    return render_data(root_node, nesting_level=0)
