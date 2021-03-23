from gendiff import tree_description as t


def build_path(parent):
    return f'{parent}.' if parent != '' else ''


def format_value(value):
    """Handles side effects of json.load function"""
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    if type(value) is str:
        return f'\'{value}\''
    if type(value) is dict \
       or type(value) is list:
        return '[complex value]'
    else:
        return value


def get_children(node, parent=""):

    info_string = ""
    if node[t.STATE] == t.CHILDREN:
        list_diff = handle_list(node[t.VALUE],
                                f'{build_path(parent)}{node[t.KEY]}')
        info_string += f"{list_diff}"
    elif node[t.STATE] == t.ADDED:
        info_string += f"\nProperty \'{build_path(parent)}{node[t.KEY]}\' " \
                       f"was added with value: " \
                       f"{format_value(node[t.VALUE])}"
    elif node[t.STATE] == t.DELETED:
        info_string += f"\nProperty \'{build_path(parent)}{node[t.KEY]}\' " \
                       f"was removed"
    elif node[t.STATE] == t.CHANGED:
        info_string += f"\nProperty \'{parent}.{node[t.KEY]}\'" \
                       f" was updated. " \
                       f"From " \
                       f"{format_value(node[t.VALUE_LEFT])}" \
                       f" to " \
                       f"{format_value(node[t.VALUE_RIGHT])}"

    return info_string


def handle_list(data, parent=""):

    diff = ""
    for element in data:
        diff += f"{get_children(element, parent)}"

    return diff


def get_render_plain(data):
    root_node = data.get('ROOT')

    diff = handle_list(root_node)
    diff = diff[1:]  # removes the first new string character

    return diff
