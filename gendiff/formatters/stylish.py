def get_spaces(number_of_spaces):
    spaces = ""
    for i in range(0, number_of_spaces):
        #spaces += "\t"
        spaces += "    "
    return spaces


def get_children(data, nesting_level):

    nesting_level += 1

    text_diff = '{'

    for record in data:
        spaces = get_spaces(nesting_level)  # for a visual indentation purpose

        if record['STATE'] == 'CHILDREN':
            text_diff += f'\n{spaces}   {record["KEY"]}: ' \
                         f'{get_children(record["VALUE"], nesting_level)}'
        elif record['STATE'] == 'ADDED':
            text_diff += f'\n{spaces} + {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'DELETED':
            text_diff += f'\n{spaces} - {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'UNCHANGED':
            text_diff += f'\n{spaces}   {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'CHANGED':
            text_diff += f'\n{spaces} - {record["KEY"]}: ' \
                         f'{record["VALUE_LEFT"]}'
            text_diff += f'\n{spaces} + {record["KEY"]}: ' \
                         f'{record["VALUE_RIGHT"]}'

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
