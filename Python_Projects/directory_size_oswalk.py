import os


def get_dir_size(path):
    dirsize = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                dirsize += os.path.getsize(file_path)
        for dirname in dirnames:
            dir_path = os.path.join(path, dirname)
            if os.path.isdir(dir_path):
                dirsize += get_dir_size(dir_path)

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
    path = "/Users/Kris/Music"
    print(path)
    print(convert_size(get_dir_size(path)))


if __name__ == '__main__':
    main()
    

