# Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python
# modules, functions, classes, and methods. It's specified in source code that is used, like a comment,
# to document a specific segment of code.

def format_name(f_name, l_name):
    """
    Takes first name and last name and formats it to return a title cased version of the name.
    :param f_name: a first name
    :param l_name: a last name
    :return: the first name and last name will be returned with a title case.
    """

    f_name = f_name.capitalize()
    l_name = l_name.title()
    return f'{l_name} {f_name}.'


print(format_name('ernEst', 'asena'))

