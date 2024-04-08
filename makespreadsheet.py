#enter target folder
#add all filenames in target folder to a spreadsheet



import csv
import time
import pathlib
import sys
import os
import re
import glob
import csv

spath = input("Enter the directory with the files to be renamed: ")
if not spath:
    spath = "C:/Users/Jason/packets"
    print(f"defaulting to directory {spath}")
else:
    print(f"using directory {spath}")

myfiles = pathlib.Path(spath)
print(f"myfiles {str(myfiles)}")

# csvfilename = "C:/Users/Jason/packets/packets.csv"
# csvfile = open(csvfilename, 'w', newline='')
# spamwriter = csv.writer(csvfile, delimiter=' ',
#                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
# spamwriter.writerow(['old name', 'new name'])

print()

if len(f"{[i.name for i in myfiles.iterdir()]}") < 1:
    sys.exit("No files to rename. Exiting.\n")

print(f"files {list(myfiles.iterdir())}")

for item in myfiles.iterdir():
    try:
        if item.is_file() and item.suffix == '.pdf' and item.name.startswith("R".upper()):

            regex_pattern = re.compile(r'^(R\d*).*(\.pdf)$')
            match = regex_pattern.match(item.name)
            if match:
                old_name = str(myfiles)+'/'+item.name
                new_name = str(myfiles)+'/'+match.group(1)+match.group(2)
                print(f"old name {old_name}")
                try:
                    os.rename(old_name, new_name)
                    print(f"new name {new_name}")
                except FileExistsError:
                    print(f"{old_name} already renamed")
            # spamwriter.writerow([item.name, item.name])
            time.sleep(.125)

    except FileNotFoundError as e:
        print(f"{e}")

print()
