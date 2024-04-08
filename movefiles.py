# enter target folder
# enter list of filenames
# enter dst folder
# new folder in dst folder (as today date)
# move files from target folder to dst folder
# if file not found add to log

import time
import pathlib
import sys
import os
import re
from pathlib import Path

# spath = input("Enter the directorywhere the files are: ")
# if not spath:
#     sys.exit("no source folder entered\n")

# dpath = input("Enter the directory where the files will go: ")
# if not dpath:
#     sys.exit("no target folder entered\n")

home_dir = Path.home()
spath = "C:\\Users\\Jason\\packets"
dpath = "C:\\Users\\Jason\\movedfiles"
log_path = str(home_dir)+"\\movefiles_error.log"

filenames = []

print("enter all filesnames:")
while True:
    f = input()
    if f == '':
        break
    filenames.append(f)

if not filenames:
    sys.exit("no files entered\n")

new_folder = str(time.strftime("%m%d%Y"))
if not os.path.exists(dpath+'\\'+new_folder):
    os.makedirs(dpath+'\\'+new_folder)

lf = open(log_path, 'a+')

for filename in filenames:
    source_file = spath+'\\'+filename
    dst_file = dpath+'\\'+new_folder+'\\'+filename
    try:
        os.rename(source_file, dst_file)
    except FileNotFoundError:
        lf.write(f"{source_file} didn't exist\n")
        print(f"{source_file} didn't exist")
    except OSError:
        continue

lf.close()
