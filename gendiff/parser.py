"""Parse provided file according to the transfered format."""

import json
import yaml


def parse(data, input_format):
    """Read file object and return it's data as a collection"""

    if input_format == 'JSON':
        return json.load(data)
    elif input_format in ('YAML', 'YML'):
        return yaml.safe_load(data)
    else:
        raise ValueError(f'Unknown format type {input_format}')
