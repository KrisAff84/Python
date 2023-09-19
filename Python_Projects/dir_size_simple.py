import os


# Returns size of directory recursively in bytes
def get_dir_size(path):
    dirsize = 0
    for entry in os.scandir(path):
        if entry.is_dir():
            dirsize += get_dir_size(entry.path)
        else:
            dirsize += entry.stat().st_size
    
    return dirsize


# Converts Bytes to KB, MB, GB, and TB
def convert_size(s):
    units = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    idx = 0
    
    while s >= 1000 and idx < len(units) - 1:
        s /= 1000.0
        idx += 1
    
    return f"{s:.2f} {units[idx]}"


def main():
    path = "/Users/Kris/LUIT"
    print(convert_size(get_dir_size(path)))

    
if __name__ == '__main__':
    main()
