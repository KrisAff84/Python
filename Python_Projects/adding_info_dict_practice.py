import os
import time


class Format:      # defines various text styles
    end = '\033[0m'
    underline = '\033[4m'
    green = '\033[92m'

# Prompt for path to catalog
# Prints current directory path
while True:
    path = input('Enter a directory path or press RETURN for current directory: ')
    print()
    if path == '':
        path = os.getcwd()
        print(Format.underline + 'Current Directory:' + Format.end)
        print(os.getcwd())
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
        if os.path.isfile(os.path.join(dirpath, filename)):
            file_size = os.stat(os.path.join(dirpath, filename)).st_size / 1024
            file_mod_time = time.ctime(os.path.getmtime(os.path.join(dirpath, filename)))
            file_dict[filename] = 'File', \
                f'Path: {dirpath}', \
                f'Size: {file_size} KB', \
                f'Last Modified: {file_mod_time} '
    for dirname in dirnames:
        if os.path.isdir(os.path.join(dirpath, dirname)):
            dir_size = os.stat(os.path.join(dirpath, dirname)).st_size / 1024
            dir_mod_time = time.ctime(os.path.getmtime(os.path.join(dirpath, dirname)))
            file_dict[dirname] = 'Directory', \
                f'Path: {dirpath}', \
                f'Size: {dir_size} KB', \
                f'Last Modified: {dir_mod_time} '

# for key in file_dict.keys():
#     if os.path.isdir(os.path.join(path, key)):
#         print(key, file_dict[key])
#         print('Files and sub-directories: ', os.listdir(os.path.join(path, key)))
#         print()

# Prints files and directories in current directory (non-recursive)
print('************ ' + Format.underline + 'Files and directories in current directory' + Format.end + ' ************')
print()
print(Format.underline + 'DIRECTORIES:' + Format.end)
for key in file_dict.keys():
    if os.path.isdir(os.path.join(path, key)):
        print(key)
print()
print(Format.underline + 'FILES:' + Format.end)
for key in file_dict.keys():
    if os.path.isfile(os.path.join(path, key)):
        print(key)
print()

# User prompt for more information about a given file or directory
# Will list key and values of file_dict based on user input and display various information
# Lists directories recursively
while True:
    user_input = input('Enter a file or directory name to get information about it, or type ALL or EXIT: ')
    print()
    if user_input == 'EXIT':
        print('Goodbye for now!')
        break
    # Fix to include all sub-directories and files
    # As of now only including up to path + user_input
    # Possibly need to ammend path variable
    elif user_input in file_dict:
        if os.path.isdir(os.path.join(path, user_input)):
            print(Format.green + user_input + Format.end, ' : ', file_dict[user_input])
            print('Files and sub-directories: ', os.listdir(os.path.join(path, user_input)))
            print()
        else:
            print(Format.green + user_input + Format.end, ' : ', file_dict[user_input])
    elif user_input == 'ALL':
        for key, value in file_dict.items():
            print(Format.green + key + Format.end, ' : ', value)
    else:
        print('File not found!')
    print()

