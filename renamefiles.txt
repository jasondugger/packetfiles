# enter target diretory
# rename only Rdigits_nondigits.pdf files

import time
import pathlib
import sys
import os
import re

spath = input("Enter the directory with the files to be renamed: ")
if not spath:
    sys.exit("no target folder entered\n")

myfiles = pathlib.Path(spath)

if len(f"{[i.name for i in myfiles.iterdir()]}") < 1:
    sys.exit("No files to rename\n")

for item in myfiles.iterdir():
    if item.is_file():
        regex_pattern = re.compile(r'^(R\d*).*(\.pdf)$')
        match = regex_pattern.match(item.name)
        if match:
            old_name = str(myfiles)+'/'+item.name
            new_name = str(myfiles)+'/'+match.group(1)+match.group(2)
            if old_name == new_name:
                print(f"{old_name} already renamed")
            else:
                os.rename(old_name, new_name)
                print(f"renamed old name: {old_name} to new name: {new_name}")
        time.sleep(.125)

print("\nDone!...Bye!\n")
