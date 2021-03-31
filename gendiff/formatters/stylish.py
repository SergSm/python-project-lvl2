
from gendiff import tree_description as t


def format_value(value, nesting_level=0):
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    if type(value) is dict:

        dict_text = '{{'

        for key, val in value.items():

            spaces = get_spaces(nesting_level + 1)
            if type(val) is dict:  # for the dictionaries
                dict_text += f'\n{spaces}  {key}: ' \
                             f'{format_value(val, nesting_level + 1)}'
            else:
                dict_text += f'\n{spaces}  {key}: {val}'

        dict_text += f'\n{get_spaces(nesting_level)}  }}'

        return dict_text

    else:
        return value


def get_spaces(depth):
    """returns the required number of spaces
     for indentation purpose"""
    return ' ' * (depth * 4 - 2)


def get_element_render(node, nesting_level):

    diff = ""
    spaces = get_spaces(nesting_level)

    if node[t.STATE] == t.CHILDREN:
        list_diff = handle_list(node[t.VALUE], nesting_level + 1)
        diff += f'\n{spaces}  {node[t.KEY]}: {{' \
                f'{list_diff}'
        diff += f'\n{spaces}  }}'
    elif node[t.STATE] == t.ADDED:
        diff += f'\n{spaces}+ {node[t.KEY]}:'
        diff += f' {format_value(node[t.VALUE], nesting_level)}'
    elif node[t.STATE] == t.DELETED:
        diff += f'\n{spaces}- {node[t.KEY]}:'
        diff += f' {format_value(node[t.VALUE], nesting_level)}'
    elif node[t.STATE] == t.CHANGED:  # there will be 2 lines
        # DELETED -
        diff += f'\n{spaces}- {node[t.KEY]}:'
        diff += f' {format_value(node[t.VALUE_LEFT], nesting_level)}'
        # ADDED +
        diff += f'\n{spaces}+ {node[t.KEY]}:'
        diff += f' {format_value(node[t.VALUE_RIGHT], nesting_level)}'
    elif node[t.STATE] == t.UNCHANGED:
        diff += f'\n{spaces}  {node[t.KEY]}:'
        diff += f' {format_value(node[t.VALUE], nesting_level)}'

    elif node[t.STATE] == t.ROOT:
        diff = "{"
        for element in node:
            diff += get_element_render(element, nesting_level)
        diff += handle_list(node.get("VALUE"), nesting_level)
        diff += "\n}"

    else:
        raise ValueError("Unknown node type")

    return diff


def handle_list(data, nesting_level):
    """Handles the list from the internal tree structure.
    the data may come from a ROOT node on its first run
    whether from a node with a "CHILDREN" state"""

    if type(data) is list:
        diff = ""
        for element in data:
            diff += get_element_render(element, nesting_level)
    else:  # being called on the first iteration
        if data.get("KEY") == "ROOT":
            diff = "{"
            diff += handle_list(data.get("VALUE"), nesting_level)
            diff += "\n}"

    return diff


def get_render_stylish(diff):
    return handle_list(diff, nesting_level=1)
