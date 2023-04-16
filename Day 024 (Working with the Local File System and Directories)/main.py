# Relative Path is the hierarchical path that locates a file or folder on a file system starting from
# the current directory. The relative path is different from the absolute path, which locates the file or folder
# starting from the root of the file system.

# An absolute path refers to the complete details needed to locate a file or folder, starting from the root element
# and ending with the other subdirectories. Absolute paths are used in websites and operating systems for locating
# files and folders. An absolute path is also known as an absolute pathname or full path.


file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()

# if you don't want to remember to close the file;

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('my_file.txt', mode='w') as file:
    file.write('Did you look at the stats?')        # write to a file, deletes everything else that was in there.

with open('my_file.txt', mode='a') as file:
    file.write('\nThey are incredible!!!\nI love them.')         # edit or rather just append to the file, do not delete its contents

# if you use open (write mode) with a file name that does not exist already, python will create the file for you.
# Take a look;
with open('../../Desktop/arsenal_players', mode='w') as players:
    players.write('Leno, \nGabriel, \nWhite, \nTomiyasu, \nSaka')

