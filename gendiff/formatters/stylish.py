
from gendiff import tree_description as t


def format_value(value):
    """Handles side effects of json.load function"""
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    else:
        return value


def get_spaces(depth):
    """returns the required number of spaces
     for indentation purpose"""
    return ' ' * (depth * 4 - 2)


def get_state_representation(state):
    """converts internal structure states
    to the stylish representation"""
    if state == t.ADDED:
        return "+"
    elif state == t.DELETED:
        return "-"
    elif state == t.UNCHANGED:
        return " "


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


def render_value(key, value, nesting_level, state):
    diff = ""
    spaces = get_spaces(nesting_level)
    state = get_state_representation(state)

    diff += f'\n{spaces}{state} {key}:'
    # check whether the value is dict or not
    if type(value) is dict:
        diff += f' {{{get_stylished_dict(value, nesting_level + 1)}'
        diff += f'\n{spaces}  }}'
    else:
        diff += f' {format_value(value)}'

    return diff


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

            diff += render_value(node[t.KEY],
                                 node[t.VALUE_LEFT],
                                 nesting_level,
                                 state=t.DELETED)

            diff += render_value(node[t.KEY],
                                 node[t.VALUE_RIGHT],
                                 nesting_level,
                                 state=t.ADDED)
        else:

            diff += render_value(node[t.KEY],
                                 node[t.VALUE],
                                 nesting_level,
                                 state=node[t.STATE])

    return diff


def handle_list(data, nesting_level):
    """Handles the list from the internal tree structure
    the data may come from a ROOT node on its first run
    whether from a node with a "CHILDREN" state"""

    if type(data) is list:
        diff = ""
        for element in data:
            diff += get_element_render(element, nesting_level)
    else:
        root_node = data.get('ROOT')
        diff = "{"
        diff += handle_list(root_node, nesting_level)
        diff += "\n}"

    return diff


def get_render_stylish(data):
    diff = handle_list(data, nesting_level=1)
    return diff
