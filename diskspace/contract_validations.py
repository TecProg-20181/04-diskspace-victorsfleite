from contracts import new_contract

import os


# Helper functions
def validate_command_values(values):
    if values[0] != 'du' or \
       values[1] != '-d' or \
       int(values[2]) <= 0 or  \
       not os.path.exists(values[3]):
        return False

    return True

def valid_command(command):
    values = command.strip().split(' ')
    if not isinstance(command, str) or \
       len(values) != 4 or \
       not validate_command_values(values):
        return False

# Contracts
new_contract('valid_command', valid_command)
