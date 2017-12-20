"""
https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Closures/closure.py
Added commends to the python tutorial code to better understand closures.
An alternative to this would be to use decorators.
"""


# Closures

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    """
    Recieves a function and returns that function appended to the log.
    """
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

def mult(x, y):
    return x * y


add_logger = logger(add)
sub_logger = logger(sub)
mult_logger = logger(mult)

"""
Because of closure the add_logger "remembers" that when it was created the add functions was used as an arg to
the outer function. Therefore add_logger will remember to use add even though add is outside the scope of log_func(*args)
"""
add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

mult_logger(4, 2)
