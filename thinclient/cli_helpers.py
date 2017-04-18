"""
Helps us create CLIs
"""

def tokenize(cmd_do_func):
    def wrapper(self, line):
        tokens = line.split()
        return cmd_do_func(self, *tokens)

    return wrapper

def num_tokens(num_args):
    def decorator(cmd_do_func):
        def wrapper(self, *args):
            args = list(args)
            if len(args) == num_args:
                return cmd_do_func(self, *args)
            print('Incorrect number of arguments, consult help')

        return wrapper

    return decorator

