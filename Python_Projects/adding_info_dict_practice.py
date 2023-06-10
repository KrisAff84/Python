import os
import time


class Format:      # defines various text styles
    end = '\033[0m'
    underline = '\033[4m'
    green = '\033[92m'


def get_dir_size(path):
    try:
        dirsize = 0
        with os.scandir(path) as itr:
            for entry in itr:
                if entry.is_file(follow_symlinks=False):
                    dirsize += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    dirsize += get_dir_size(entry.path)
        return dirsize
    except PermissionError:
        dirsize = os.path.getsize(path)
        return dirsize


def size_convert(s):
    if 1000 <= s < 1000 ** 2:
        s = round(s / 1000, 2)
        return str(s) + ' KB'
    if 1000 ** 2 <= s < 1000 ** 3:
        s = round(s / (1000 ** 2), 2)
        return str(s) + ' MB'
    if 1000 ** 3 <= s < 1000 ** 4:
        s = round(s / (1000 ** 3), 2)
        return str(s) + ' GB'
    if s >= 1000 ** 4:
        s = round(s / (1000 ** 4), 2)
        return str(s) + ' TB'
    else:
        return str(s) + ' Bytes'


isfile = os.path.isfile
isdir = os.path.isdir


# Prompt for path to catalog
# Prints current directory path
while True:
    path = input('Enter a directory path or press RETURN for current directory: ')
    print()
    if path == '':
        path = os.getcwd()
        print(Format.underline + 'Current Directory:' + Format.end)
        print(path)
        print()
        break
    elif os.path.exists(path):
        print(Format.underline + 'Current Directory:' + Format.end)
        print(path)
        print()
        break
    else:
        print('Please enter a valid path: ')

# Adds files and directories recursively to dictionary file_dict
file_dict = {}
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if isfile(os.path.join(dirpath, filename)):
            file_size = size_convert(os.path.getsize(os.path.join(dirpath, filename)))
            file_created = time.ctime(os.path.getctime(os.path.join(dirpath, filename)))
            file_mod_time = time.ctime(os.path.getmtime(os.path.join(dirpath, filename)))
            file_dict[filename] = 'File', \
                f'Path: {dirpath}', \
                f'Size: {file_size}', \
                f'Created: {file_created}', \
                f'Last Modified: {file_mod_time} '
    for dirname in dirnames:
        if isdir(os.path.join(dirpath, dirname)):
            dir_size = size_convert(get_dir_size(os.path.join(dirpath, dirname)))
            dir_created = time.ctime(os.path.getctime(os.path.join(dirpath, dirname)))
            dir_mod_time = time.ctime(os.path.getmtime(os.path.join(dirpath, dirname)))
            file_dict[dirname] = 'Directory', \
                f'Path: {dirpath}', \
                f'Size: {dir_size}', \
                f'Created: {dir_created}', \
                f'Last Modified: {dir_mod_time} '

# Prints files and directories in current directory (non-recursive)
print('************ ' + Format.underline + 'Files and directories in current directory' + Format.end + ' ************')
print()
print(Format.underline + 'DIRECTORIES:' + Format.end)
for key in file_dict.keys():
    if isdir(os.path.join(path, key)):
        print(key)
print()
print(Format.underline + 'FILES:' + Format.end)
for key in file_dict.keys():
    if isfile(os.path.join(path, key)):
        print(key)
print()

# User prompt for more information about a given file or directory
# Will list key and values of file_dict based on user input and display various information
# Lists directories recursively
amended_path = path
while True:
    user_input = input('Enter a file or directory name to get information about it, or type ALL or EXIT: ')
    print()
    if user_input == 'EXIT':
        print('Goodbye for now!')
        break
    elif user_input in file_dict:
        if isdir(os.path.join(path, user_input)):
            print(Format.green + user_input + Format.end, ' : ', file_dict[user_input])
            print('Files and sub-directories: ', os.listdir(os.path.join(path, user_input)))
            amended_path = os.path.join(path, user_input)
            print()
        elif isdir(os.path.join(amended_path, user_input)):
            print(Format.green + user_input + Format.end, ' : ', file_dict[user_input])
            print('Files and sub-directories: ', os.listdir(os.path.join(amended_path, user_input)))
            amended_path = os.path.join(amended_path, user_input)
            print()
        else:
            print(Format.green + user_input + Format.end, ' : ', file_dict[user_input])
    elif user_input == 'ALL':
        for key, value in file_dict.items():
            print(Format.green + key + Format.end, ' : ', value)
    else:
        print('File not found!')
    print()
