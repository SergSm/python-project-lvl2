
def get_spaces(number_of_spaces):
    spaces = ""
    for i in range(0, number_of_spaces):
        #spaces += "\t"
        spaces += " "
    return spaces


# DEBUG
dct = {'group2': {'abc': '12345', 'deep': {'id': '45'}}}


def get_mspaces(depth):
    spaaaace = ''
    for x in range(1, 4*depth):
        spaaaace += ' '
    return spaaaace


def get_nicely_printed_dict(dictionary, depth):

    astier = ''

    count = 0
    for x, y in dictionary.items():
        count += 1

        if type(y) is dict:

            if not (depth == 0 and count == 1):
                astier += '\n'

            astier += get_mspaces(depth) \
                      + x + ': {' \
                      + '\n'

            depth += 1

            astier += get_nicely_printed_dict(y, depth) \
                      + get_mspaces(depth) \
                      + '\n' \
                      + get_mspaces(depth) \
                      + '}'
        else:
            astier += get_mspaces(depth) + str(x) + ': ' + str(y)
            # if it is the last record in dict do not add newstring
            if count < len(dct):
                astier += '\n'

    return astier


#  try 3
def get_formatted_dict(dictionary, nesting_level):

    dict_str_result = ""
    for x, y in dictionary.items():
        if not type(y) is dict:
            dict_str_result += f'{x}: {y}'
        else:
            dict_str_result += f'{x}: {get_formatted_dict(y)}'

    return dict_str_result


def get_children(data, nesting_level):

    nesting_level += 1

    text_diff = '{'

    for record in data:
        spaces = get_spaces(nesting_level)  # for a visual indentation purpose

        ############################################################################

        prefix = f'\n{spaces}'

        if record['STATE'] == 'CHANGED':
            value_left = record["VALUE_LEFT"]
            value_right = record["VALUE_RIGHT"]
        else:
            value_left = record["VALUE"]
            if type(value_left) is dict:
                #value_left = get_formatted_dict(value_left)
                pass
                #value_left = '{\n' \
                 #           git  + get_nicely_printed_dict(value_left, nesting_level) \
                  #           + '\n' \
                   #          + get_mspaces(nesting_level) + '}'
            value_right = ''

        if record['STATE'] == 'CHILDREN':
            pretty_children = get_children(record["VALUE"], nesting_level)
        else:
            pretty_children = ''

        the_key = record["KEY"]

        ############################################################################

        if record['STATE'] == 'CHILDREN':
            text_diff += f'{prefix}   {the_key}: ' \
                         f'{pretty_children}'
        elif record['STATE'] == 'ADDED':

            if type(value_left) is dict:
                txt = get_nicely_printed_dict({prefix + ' + ' + the_key: value_left}, nesting_level)
            else:
                txt = f' {the_key}: {value_left}'

            #text_diff += f'{prefix} + {the_key}: {value_left}'
            text_diff += txt

        elif record['STATE'] == 'DELETED':
            text_diff += f'{prefix} - {the_key}: {value_left}'
        elif record['STATE'] == 'UNCHANGED':
            text_diff += f'{prefix}   {the_key}: {value_left}'
        elif record['STATE'] == 'CHANGED':
            text_diff += f'{prefix} - {the_key}: ' \
                         f'{value_left}'
            text_diff += f'{prefix} + {the_key}: ' \
                         f'{value_right}'

    if nesting_level > 1:
        text_diff += '\n' + get_spaces(nesting_level) + '}'
    else:
        text_diff += '\n' + '}'

    return text_diff


def get_render_stylish(data):

    root_node = data.get('ROOT')
    # kind of a guard expression to save some spaces on indentation-levels
    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')
    return get_children(root_node, nesting_level=0)
