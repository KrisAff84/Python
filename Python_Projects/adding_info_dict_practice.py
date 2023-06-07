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
for dirpath, dirnames, filenames in os.walk(path):
    print('Directory path:', dirpath)
    print('Sub-directories:', dirnames)
    print('Files:', filenames)
    print()
    print()

