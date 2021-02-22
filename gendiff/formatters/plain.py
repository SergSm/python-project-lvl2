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
    if type(value) is dict:
        return '[complex value]'
    else:
        return value


def get_children(record, parent=""):

    info_string = ""
    if record['STATE'] == 'CHILDREN':
        list_diff = handle_list(record["VALUE"],
                                f'{build_path(parent)}{record["KEY"]}')
        info_string += f"{list_diff}"
    elif record['STATE'] == 'ADDED':
        info_string += f"\nProperty \'{build_path(parent)}{record['KEY']}\' " \
                       f"was added with value: " \
                       f"{format_value(record['VALUE'])}"
    elif record["STATE"] == "DELETED":
        info_string += f"\nProperty \'{build_path(parent)}{record['KEY']}\' " \
                       f"was removed"
    elif record["STATE"] == "CHANGED":
        info_string += f"\nProperty \'{parent}.{record['KEY']}\'" \
                       f" was updated. " \
                       f"From " \
                       f"{format_value(record['VALUE_LEFT'])}" \
                       f" to " \
                       f"{format_value(record['VALUE_RIGHT'])}"

    return info_string


def handle_list(data, parent=""):

    diff = ""
    for element in data:
        diff += f"{get_children(element, parent)}"

    return diff


def get_render_plain(data):
    root_node = data.get('ROOT')

    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')

    diff = handle_list(root_node)
    diff = diff[1:]  # removes the first new string character

    return diff
