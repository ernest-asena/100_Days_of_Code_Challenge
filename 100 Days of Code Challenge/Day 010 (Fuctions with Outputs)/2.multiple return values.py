def format_name(f_name, l_name):
    if f_name =='' or l_name =='':
        return 'You did not provide any inputs.'
    f_name = f_name.capitalize()
    l_name = l_name.title()
    return f'{l_name} {f_name}.'


print(format_name('e', 'asena'))