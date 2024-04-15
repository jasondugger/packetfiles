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
import shutil

home_dir = Path.home()
change_log_path = str(home_dir)+"\\Documents\\copyfiles_log.txt"

spath = input("Enter the directory where the files are: ")
if not spath:
    input(f"no source folder entered\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit()

dpath = input("Enter the directory where the files will be copied to: ")
if not dpath:
    input(f"no target folder entered\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit()

filenames = []

print("Enter all file names:")
while True:
    f = input()
    if f == '':
        break
    filenames.append(f)

if not filenames:
    input(f"no files entered\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit()

new_folder = str(time.strftime("%m%d%Y"))
new_folder_path = dpath+'\\'+new_folder
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

change_log = open(change_log_path, 'a+')

for f in filenames:
    if not f.endswith('.pdf'):
        filename = f+'.pdf'
    else:
        filename = f
    source_file = spath+'\\'+filename
    dst_file = new_folder_path+'\\'+filename
    try:
        shutil.copyfile(source_file, dst_file)
        change_log.write(f"{filename} copied\n")
        print(f"{filename} copied")
    except FileNotFoundError:
        change_log.write(f"{filename} doesn't exist\n")
        print(f"{filename} doesn't exist")
    except OSError as e:
        change_log.write(f"failed to copy {filename}: {e}\n")
        print(f"failed to copy {filename}: {e}")
        continue

change_log.close()

input(f"Done!\nChanges logged in {change_log_path}\nPress Enter to exit")
sys.exit("\n")
