
from gendiff import tree_description as t


def format_value(value):
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    if value == t.ADDED:
        return "+"
    if value == t.DELETED:
        return "-"
    if value == t.UNCHANGED:
        return " "
    else:
        return value


def get_spaces(depth):
    """returns the required number of spaces
     for indentation purpose"""
    return ' ' * (depth * 4 - 2)


def get_stylished_dict(node, nesting_level):
    """pretty formats the dictionary according to
    its indentation level"""
    dict_text = ""
    spaces = get_spaces(nesting_level)

    for key, val in node.items():

        if type(val) is dict:
            dict_value = get_stylished_dict(val, nesting_level + 1)
            dict_text += f'\n{spaces}  {key}: {{{dict_value}'
            dict_text += f'\n{spaces}  }}'
        else:
            dict_text += f'\n{spaces}  {key}: {val}'

    return dict_text


def get_element_render(node, nesting_level):

    diff = ""
    spaces = get_spaces(nesting_level)

    if node[t.STATE] == t.CHILDREN:
        list_diff = handle_list(node[t.VALUE], nesting_level + 1)
        diff += f'\n{spaces}  {node[t.KEY]}: {{' \
                f'{list_diff}'
        diff += f'\n{spaces}  }}'
    else:
        if node[t.STATE] == t.CHANGED:  # there will be 2 lines
            # DELETED
            diff += f'\n{spaces}{format_value(t.DELETED)} {node[t.KEY]}:'
            if type(node[t.VALUE_LEFT]) is dict:
                diff += f' {{{get_stylished_dict(node[t.VALUE_LEFT], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {format_value(node[t.VALUE_LEFT])}'

            # ...and ADDED
            diff += f'\n{spaces}{format_value(t.ADDED)} {node[t.KEY]}:'
            if type(node[t.VALUE_RIGHT]) is dict:
                diff += f' {{{get_stylished_dict(node[t.VALUE_RIGHT], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {format_value(node[t.VALUE_RIGHT])}'

        else:

            diff += f'\n{spaces}{format_value(node[t.STATE])} {node[t.KEY]}:'
            if type(node[t.VALUE]) is dict:
                diff += f' {{{get_stylished_dict(node[t.VALUE], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {format_value(node[t.VALUE])}'

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
        root_node = data.get('ROOT')
        diff = "{"
        diff += handle_list(root_node, nesting_level)
        diff += "\n}"

    return diff


def get_render_stylish(data):
    diff = handle_list(data, nesting_level=1)
    return diff
