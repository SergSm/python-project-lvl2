def build_path(parent):

    return f'{parent}.' if parent != '' else ''


def change_jsonized_representation(value):
    """Handles side effects of json.load function"""
    if value is None:
        return 'null'
    if type(value) is bool:
        return 'true' if value else 'false'
    else:
        return value


def format_if_complex(value_right):
    if type(value_right) is dict:
        return '[complex value]'
    else:
        return value_right


def get_children(data, parent=""):

    info_string = ''

    for record in data:

        if record['STATE'] == 'CHILDREN':
            info_string += f"{build_path(parent)}"\
                           f"{get_children(change_jsonized_representation(record['VALUE']), record['KEY'])}"
        elif record['STATE'] == 'ADDED':
            info_string += f"Property '{build_path(parent)}" \
                           f"{record['KEY']}' was added with value: " \
                           f"{format_if_complex(change_jsonized_representation(record['VALUE']))}\n"
        elif record["STATE"] == "DELETED":
            info_string += f"Property {build_path(parent)}" \
                           f"'{record['KEY']}' was removed\n"
        elif record["STATE"] == "CHANGED":
            info_string += f"Property {build_path(parent)}" \
                           f"'{record['KEY']}' was updated. " \
                           f"From " \
                           f"{format_if_complex(change_jsonized_representation(record['VALUE_LEFT']))}" \
                           f" to " \
                           f"{format_if_complex(change_jsonized_representation(record['VALUE_RIGHT']))}\n"

    return info_string


def get_render_plain(data):
    root_node = data.get('ROOT')

    if root_node is None:
        raise Exception('No ROOT node in the internal representation.')

    return get_children(root_node)
