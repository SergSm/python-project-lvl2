"""Module describes keys and types of nodes
for an internal structure which is used
to render the difference using formatters"""

# left part of the dictionary
KEY = 'KEY'
VALUE = 'VALUE'
STATE = 'STATE'

# if the type is CHANGED then the left part consists
# of these two keys instead of VALUE
VALUE_LEFT = 'VALUE_LEFT'
VALUE_RIGHT = 'VALUE_RIGHT'

# right part of the dictionary
# Node types
ADDED = 'ADDED'
DELETED = 'DELETED'
UNCHANGED = 'UNCHANGED'
CHILDREN = 'CHILDREN'
CHANGED = 'CHANGED'
ROOT = 'ROOT'
