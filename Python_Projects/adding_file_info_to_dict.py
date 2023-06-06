import os
from pathlib import Path
path = '/Users/Kris/Dropbox/Git_Repos/Python/DailyLessons/Exercises'
counter = 1
file_info = {}
for dirpath, dir, filenames in os.walk(path):
    for filename in filenames:
        file_info[counter] = f'File name: {filename}', \
            f'Size: {os.stat(os.path.join(path, filename)).st_size / 10} KB'
        counter = counter + 1

print(file_info)

# On the right track, just need a method for entering full path for
# files in sub-directories
# As of now works with directories with no sub-directories












