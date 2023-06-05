import os
from datetime import datetime

print(os.getcwd()) # current working directory
os.chdir('/Users/Kris/Desktop/') # Change directory
print(os.stat('CDA Code').st_size)  # size
mod_time = os.stat('CDA Code').st_mtime  # mod time
print(os.stat('CDA Code').st_mtime)
print(datetime.fromtimestamp(mod_time))  # for mod time human readable
# Prints directories and files in current directory tree
for dirpath, dirnames, filenames in os.walk('/Users/Kris/Desktop/'):
    print('Current Path:', dirpath)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))







