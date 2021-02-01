

def get_children(data):

    text_diff = '{'

    for record in data:
        if record['STATE'] == 'CHILDREN':
            text_diff += f'\n {record["KEY"]}: {get_children(record["VALUE"])}'
        elif record['STATE'] == 'ADDED':
            text_diff += f'\n + {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'DELETED':
            text_diff += f'\n - {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'UNCHANGED':
            text_diff += f'\n {record["KEY"]}: {record["VALUE"]}'
        elif record['STATE'] == 'CHANGED':
            text_diff += f'\n - {record["KEY"]}: {record["VALUE_LEFT"]}'
            text_diff += f'\n + {record["KEY"]}: {record["VALUE_RIGHT"]}'

    text_diff += '\n}'

    return text_diff


def get_render_stylish(data):

    root_node = data.get('ROOT')
    # kind of a guard expression to save some spaces on indentation-levels
    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')
    return get_children(root_node)


def get_formatted_string(data, formatter):

    if formatter == "stylish":
        return get_render_stylish(data)
    else:
        return "unknown formatter string"
