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
# outer_function()

# Closures the inner function still has access to the variables in the local scope in which it was created.
# Basically if return inner_function is used, my_func = outer_function() will "remember" the local variable message


def outer_function(msg):
    """
    Example 1 - Using the local variable message
    Inner function has access to the message variable
    See the closures video https://www.youtube.com/watch?v=swU3c34d2NQ&feature=youtu.be
    """
    message = msg

    def inner_function():
        print(message)

    print("Exeinner")
    return inner_function

# my_func = outer_function()
# my_func()
# my_func()
# my_func()
hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
