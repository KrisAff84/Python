import os
import time

while True:
    path = input('Enter a directory path or press RETURN for current directory: ')
    if path == '':
        path = os.getcwd()
        print('Current Directory:')
        print(os.getcwd())
        break
    elif os.path.exists(path):
        print('Current Directory:')
        print(path)
        break
    else:
        print('Please enter a valid path: ')

file_dict = {}
for dirpaths, dirs, filenames in os.walk(path):
    for filename in filenames:
        if os.path.isfile(os.path.join(path, filename)):
            file_size = os.stat(os.path.join(path, filename)).st_size / 1024
            file_mod_time = time.ctime(os.path.getmtime(os.path.join(path, filename)))
            file_dict[filename] = 'File',\
                f'Size {file_size} KB', \
                f'Modified {file_mod_time} '
    for dir in dirs:
        if os.path.isdir(os.path.join(path, dir)):
            dir_size = os.stat(os.path.join(path, dir)).st_size / 1024
            dir_mod_time = time.ctime(os.path.getmtime(os.path.join(path, dir)))
            file_dict[dir] = 'Directory',\
                f'Size {dir_size} KB', \
                f'Modified {dir_mod_time}'

print()
print('List of files and sub-directories in current directory:')
print()
for key in file_dict.keys():
    print(key)
print()

while True:
    user_input = input('Enter a file or directory name to get information about it, or type ALL or EXIT: ')
    print()
    if user_input == 'EXIT':
        print('Goodbye for now!')
        break
    elif user_input in file_dict:
        print(user_input, file_dict[user_input])
    elif user_input == 'ALL':
        for key, value in file_dict.items():
            print(key, ' : ', value)
    else:
        print('File not found!')
    print()

# Works! Now figure out how to catalog files in sub-directories












