from .stylish import get_render_stylish


def get_formatted_string(data, formatter):

    if formatter == "stylish":
        return get_render_stylish(data)
    else:
        return "unknown formatter string"
