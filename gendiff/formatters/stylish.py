
def change_jsonized_representation(value):
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    else:
        return value


def get_mspaces(depth):
    return ' ' * (depth * 4 - 2)


def get_state_representation(state):
    if state == "ADDED":
        return "+"
    elif state == "DELETED":
        return "-"
    elif state == "UNCHANGED":
        return " "


def get_stylished_dict(dctnary, nesting_level):

    dict_text = ""
    spaces = get_mspaces(nesting_level)

    for key, val in dctnary.items():

        if type(val) is dict:
            dict_text += f'\n{spaces}  {key}: {{{get_stylished_dict(val, nesting_level + 1)}'
            dict_text += f'\n{spaces}  }}'
        else:
            dict_text += f'\n{spaces}  {key}: {val}'

    return dict_text


def get_element_render(dctnary, nesting_level):

    diff = ""

    spaces = get_mspaces(nesting_level)

    if dctnary["STATE"] == "CHILDREN":
        # \n"    __KEY:_{render}"
        #   "123456             "
        diff += f'\n{spaces}  {dctnary["KEY"]}: {{{render_data(dctnary["VALUE"], nesting_level+1)}'
        diff += f'\n{spaces}  }}'
    else:
        if dctnary["STATE"] == "CHANGED":  # there will be 2 lines
            state_deleted = get_state_representation("DELETED")
            state_added = get_state_representation("ADDED")

            diff += f'\n{spaces}{state_deleted} {dctnary["KEY"]}:'
            if type(dctnary["VALUE_LEFT"], ) is dict:
                diff += f' {{{get_stylished_dict(dctnary["VALUE_LEFT"], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {change_jsonized_representation(dctnary["VALUE_LEFT"])}'

            diff += f'\n{spaces}{state_added} {dctnary["KEY"]}:'
            if type(dctnary["VALUE_RIGHT"], ) is dict:
                diff += f' {{{get_stylished_dict(dctnary["VALUE_RIGHT"], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {change_jsonized_representation(dctnary["VALUE_RIGHT"])}'

        else:
            state = get_state_representation(dctnary["STATE"])
            diff += f'\n{spaces}{state} {dctnary["KEY"]}:'

            # check whether the value is dict or not
            if type(dctnary["VALUE"], ) is dict:
                diff += f' {{{get_stylished_dict(dctnary["VALUE"], nesting_level + 1)}'
                diff += f'\n{spaces}  }}'
            else:
                diff += f' {change_jsonized_representation(dctnary["VALUE"])}'

    return diff


def render_data(data, nesting_level):
    diff = ""
    if type(data) is list:
        for element in data:
            diff += get_element_render(element, nesting_level)

    return diff


def get_render_stylish(data):

    root_node = data.get('ROOT')
    # kind of a guard expression
    # to save some spaces on indentation-levels
    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')

    text_diff = "{"

    text_diff += render_data(root_node, nesting_level=1)

    text_diff += "\n}"

    return text_diff
