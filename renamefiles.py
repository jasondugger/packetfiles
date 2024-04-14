# enter target diretory
# rename only Rdigits_nondigits.pdf files

import time
import pathlib
import sys
import os
import re
from pathlib import Path

home_dir = Path.home()
change_log_path = str(home_dir)+"\\Documents\\rename_files_log.txt"
change_log = open(change_log_path, 'a+')

spath = input("Enter the directory with the files to be renamed: ")
if not spath:
    change_log.write("no target folder entered")
    input(f"No target folder entered!\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit("\n")

myfiles = pathlib.Path(spath)

if len(f"{[i.name for i in myfiles.iterdir()]}") < 1:
    change_log.write(f"No files to rename in {str(myfiles)}")
    input(f"No files to rename in {str(myfiles)}\nChanges logged in {change_log_path}\nPress Enter to exit")
    sys.exit("\n")

for item in myfiles.iterdir():
    if item.is_file():
        regex_pattern = re.compile(r'^(R\d*).*(\.pdf)$')
        match = regex_pattern.match(item.name)
        if match:
            old_name = item.name
            new_name = match.group(1)+match.group(2)
            if old_name == new_name:
                change_log.write(f"{old_name} already renamed")
                print(f"{old_name} already renamed")
            else:
                try:
                    os.rename(str(myfiles)+"\\"+old_name, str(myfiles)+"\\"+new_name)
                    print(f"renamed {old_name} to {new_name}")
                    change_log.write(f"renamed {old_name} to {new_name}")
                except Exception as e:
                    print(f"failed to rename {old_name} to: {new_name}: {e}")
                    change_log.write(f"failed to rename {old_name} to: {new_name}: {e}")

        time.sleep(.125)

change_log.close()

input(f"Done!\nChanges logged in {change_log_path}\nPress Enter to exit")
sys.exit("\n")
