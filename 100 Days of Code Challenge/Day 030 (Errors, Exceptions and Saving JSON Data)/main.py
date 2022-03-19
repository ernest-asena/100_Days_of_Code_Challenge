# Examples of Errors;
# 1. FileNotFoundError
# 2. IndexError
# 3. TypeError
# 4. KeyError
# 5. ZeroDivisionError

# Keywords: try, except, else, finally

try:
    file = open('a_file.txt', 'r')
    dict_try = {'key': 'value'}
    dict_try['key']
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(F'The key {error_message} does not exist.')
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print('File was closed.')
