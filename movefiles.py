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

home_dir = Path.home()
change_log_path = str(home_dir)+"\\movefiles_log.csv"

spath = input("Enter the directorywhere the files are: ")
if not spath:
    input(f"no source folder entered\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit()

dpath = input("Enter the directory where the files will go: ")
if not dpath:
    input(f"no target folder entered\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit()

filenames = []

print("enter all filesnames:")
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

for filename in filenames:
    source_file = spath+'\\'+filename
    dst_file = new_folder_path+'\\'+filename
    try:
        os.rename(source_file, dst_file)
        change_log.write(f"{filename} moved\n")
        print(f"{filename} moved")
    except FileNotFoundError:
        change_log.write(f"{filename} doesn't exist\n")
        print(f"{filename} doesn't exist")
    except OSError as e:
        change_log.write(f"failed to move {filename}: {e}\n")
        print(f"failed to move {filename}: {e}")
        continue

change_log.close()

input(f"Done!\nChanges logged in {change_log_path}\nPress Enter to exit")
sys.exit("\n")
