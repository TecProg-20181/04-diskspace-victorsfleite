from contracts import new_contract

import os


# Helper functions
def is_valid_path(value):
    return os.path.exists(value)

def validate_command_values(values):
    if values[0] != 'du' or \
       values[1] != '-d' or \
       int(values[2]) <= 0 or  \
       not is_valid_path(values[3]):
        return False

    return True

def valid_command(command):
    values = command.strip().split(' ')
    if not isinstance(command, str) or \
       len(values) != 4 or \
       not validate_command_values(values):
        return False

def valid_file_tree_node(node):
    if type(node) != dict or \
       not 'print_size' in node or \
       not 'children' in node or \
       not 'size' in node:
        return False


# Contracts
new_contract('is_valid_path', is_valid_path)
new_contract('valid_command', valid_command)
new_contract('valid_file_tree_node', valid_file_tree_node)
