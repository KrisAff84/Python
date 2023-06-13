import os
import time

# Variables for commonly used methods
isfile = os.path.isfile
isdir = os.path.isdir
join = os.path.join

# Defines various text styles
class Format:
    end = '\033[0m'
    underline = '\033[4m'
    green = '\033[92m'

# Gets size of directories recursively
def get_dir_size(path):
    dirsize = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if isfile(join(path, filename)):
                dirsize += os.path.getsize(join(path, filename))
        for dirname in dirnames:
            if isdir(join(path, dirname)):
                dirsize += get_dir_size(join(path, dirname))

    return dirsize

# Converts Bytes to KB, MB, GB, and TB
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


# The two functions below return created and modified time
def created(path1, path2):
    path = join(path1, path2)
    created = time.ctime(os.path.getctime(path))
    return created


def modified(path1, path2):
    path = join(path1, path2)
    modified = time.ctime(os.path.getmtime(path))
    return modified



def filedict(path=os.getcwd()):
    while True:
        print()
        if os.path.exists(path):
            print(Format.underline + 'Current Directory:' + Format.end)
            print(path)
            print()
            break
        else:
            print('Path not valid!')
            break

    # Adds files and directories recursively to dictionary file_dict
    file_dict = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if isfile(join(dirpath, filename)):
                file_size = size_convert(os.path.getsize(join(dirpath, filename)))
                file_created = created(dirpath, filename)
                file_mod_time = modified(dirpath, filename)
                file_dict[filename] = 'File', \
                    'Path: ' + dirpath, \
                    'Size: ' + file_size, \
                    'Created: ' + file_created, \
                    'Last Modified: ' + file_mod_time
        for dirname in dirnames:
            if isdir(join(dirpath, dirname)):
                dir_size = size_convert(get_dir_size(join(dirpath, dirname)))
                dir_created = created(dirpath, dirname)
                dir_mod_time = modified(dirpath, dirname)
                file_dict[dirname] = 'Directory', \
                    'Path: ' + dirpath, \
                    f'Size: {dir_size}', \
                    'Created: ' + dir_created, \
                    'Last Modified: ' + dir_mod_time

    print(f'Total Items: {len(file_dict)}')
    print()
    for key, value in file_dict.items():
        print(Format.green + key + Format.end, ' : ', value)

    return file_dict
