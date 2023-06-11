# Gets size of directory

import os


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


dir_size = get_dir_size('/Users/Kris/Splice')
# Converts bytes to KB, MB, or GB


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


print(size_convert(dir_size))

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