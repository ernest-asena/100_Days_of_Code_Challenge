def format_name(f_name, l_name):
    """Take a first and last name and format it"""
    f_name = f_name.capitalize()
    l_name = l_name.title()
    return f'{l_name} {f_name}.'


print(format_name('ernEst', 'asena'))
