
def change_jsonized_representation(value):
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
    if state == "ADDED":
        return "+"
    elif state == "DELETED":
        return "-"
    elif state == "UNCHANGED":
        return " "


def get_stylished_dict(dctnary, nesting_level):
    """pretty formats the dictionary according to
    its indentation level"""
    dict_text = ""
    spaces = get_spaces(nesting_level)

    for key, val in dctnary.items():

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
        diff += f' {change_jsonized_representation(value)}'

    return diff


def get_element_render(dctnary, nesting_level):

    diff = ""
    spaces = get_spaces(nesting_level)

    if dctnary["STATE"] == "CHILDREN":
        list_diff = handle_list(dctnary["VALUE"], nesting_level + 1)
        diff += f'\n{spaces}  {dctnary["KEY"]}: {{' \
                f'{list_diff}'
        diff += f'\n{spaces}  }}'
    else:
        if dctnary["STATE"] == "CHANGED":  # there will be 2 lines

            diff += render_value(dctnary["KEY"],
                                 dctnary["VALUE_LEFT"],
                                 nesting_level,
                                 state="DELETED")

            diff += render_value(dctnary["KEY"],
                                 dctnary["VALUE_RIGHT"],
                                 nesting_level,
                                 state="ADDED")
        else:

            diff += render_value(dctnary["KEY"],
                                 dctnary["VALUE"],
                                 nesting_level,
                                 state=dctnary["STATE"])

    return diff


def handle_list(data, nesting_level):
    """Handles the list from the internal tree structure
    the data may come from a ROOT node on its first run
    whether from a node with a "CHILDREN" state"""
    diff = ""
    for element in data:
        diff += get_element_render(element, nesting_level)

    return diff


def get_render_stylish(data):

    root_node = data.get('ROOT')
    # kind of a guard expression
    # to save some spaces on indentation-levels
    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')

    diff = "{"
    diff += handle_list(root_node, nesting_level=1)
    diff += "\n}"

    return diff
