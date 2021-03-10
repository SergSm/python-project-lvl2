from .stylish import get_render_stylish
from .plain import get_render_plain
from .json import get_render_json


def get_formatted_result(data, formatter):

    if formatter == "stylish":
        return get_render_stylish(data)
    elif formatter == "plain":
        return get_render_plain(data)
    elif formatter == "json":
        return get_render_json(data)
    else:
        raise ValueError(f'unknown formatter {formatter}')
