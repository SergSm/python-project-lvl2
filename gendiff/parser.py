"""Parse provided file according to the transfered format."""

import json
import yaml


def get_parsed_data(fileobject, format_type):

    """Read file object and return it's data as a collection"""
    if format_type == '.JSON':
        return json.load(fileobject)
    elif format_type in ('.YAML', '.YML'):
        return yaml.safe_load(fileobject)
    else:
        raise ValueError(f'Unknown format type {format_type}')
