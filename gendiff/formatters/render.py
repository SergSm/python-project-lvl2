from .stylish import get_render_stylish
from .plain import get_render_plain


def get_formatted_string(data, formatter):

    if formatter == "stylish":
        return get_render_stylish(data)
    elif formatter == "plain":
        return get_render_plain(data)
    else:
        return "unknown formatter string"
