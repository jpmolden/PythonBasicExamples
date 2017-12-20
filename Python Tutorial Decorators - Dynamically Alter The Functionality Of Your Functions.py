#
# def outer_function():
#     """
#     Example 1 - Using the local variable message
#     Inner function has access to the message variable
#     Returns the executed inner function
#     """
#     message = 'Hi'
#
#     def inner_function():
#         print(message)
#
#     print("Exe inner")
#     return inner_function()
#
# outer_function()Closures

# Closures the inner function still has access to the variables in the local scope in which it was created.
# Basically if return inner_function is used, my_func = outer_function() will "remember" the local variable message


# # Closures
# def outer_function(msg):
#     """
#     Example 1 - Using the local variable message
#     Inner function has access to the message variable
#     See the closures video https://www.youtube.com/watch?v=swU3c34d2NQ&feature=youtu.be
#     """
#     message = msg
#
#     def inner_function():
#         """
#         Prints out specific message
#         """
#         print(message)
#
#     print("Exeinner")
#     return inner_function
#
# # my_func = outer_function()
# # my_func()
# # my_func()
# # my_func()
# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
# hi_func()

# # Decorator Example - Allows to easily add functionality to existing functions without modifying the original function
# def decorator_function(original_function):
#     def wrapper_function():
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#
#     return wrapper_function
#
# def display():
#     print('Display function ran')
#
# decorated_display = decorator_function(display)
#
# decorated_display()

# # Decorator Example - Alternate and typical syntax
# def decorator_function(original_function):
#     def wrapper_function():
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#
#     return wrapper_function
#
# @decorator_function
# def display():
#     print('Display function ran')
#
# display()


# Decorator Example 3 - Alternate and typical syntax
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

@decorator_function
def display():
    print('Display function ran')

def display_info(name, age):
    print('Display info ran with arguments ({}, {})'.format(name, age))

display()
display_info('Bob', 50)
