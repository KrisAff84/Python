import os

def get_dir_size(path, directories_to_skip=[]):
    dirsize = 0
    entries_skipped = []
    files_not_found = 0
    for entry in os.scandir(path):
        if entry.is_symlink() or entry.name in directories_to_skip:
            continue
        elif entry.is_dir():
            try:
                sub_dirsize, sub_entries_skipped, sub_files_not_found = get_dir_size(entry.path)
                dirsize += sub_dirsize
                entries_skipped.extend(sub_entries_skipped)
                files_not_found += sub_files_not_found
            except FileNotFoundError:
                files_not_found += 1
            except PermissionError:
                entries_skipped.append(entry.path)
        else:
            try:
                dirsize += entry.stat().st_size
            except FileNotFoundError:
                files_not_found += 1
            except PermissionError:
                entries_skipped.append(entry.path)
    
    return dirsize, entries_skipped, files_not_found

# Rest of the code...

# Converts Bytes to KB, MB, GB, and TB
def convert_size(s):
    units = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    idx = 0
    
    while s >= 1000 and idx < len(units) - 1:
        s /= 1000.0
        idx += 1
    
    return f"{s:.2f} {units[idx]}"


def main():
    path = "/Users/Kris"
    directories_to_skip = ['proc']

    print()
    print(f'Path to scan:    {path}')
    dirsize, entries_skipped, files_not_found = get_dir_size(path, directories_to_skip) 
    if len(entries_skipped) > 0:
        print()
        print('The following files were ignored due to Permission Error:')
        print()
        for entry in entries_skipped:
            print(entry)
    if files_not_found > 0:
        print()
        print(f'{files_not_found} files could not be found.')
        print()
    print() 
    print(f'Total size of path:    {convert_size(dirsize)}')
    print()

if __name__ == '__main__':
    main()
