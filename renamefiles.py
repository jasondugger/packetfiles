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
    spath = "c:/Users/jdugg/Documents"
    print(f"defaulting to directory {spath}")
else:
    print(f"using directory {spath}")

csvfilename = "c:/Users/jdugg/Documents/testfiles/packets.csv"
myfiles = pathlib.Path(spath)
print(f"myfiles {myfiles}")
csvfile = open(csvfilename, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(['old name', 'new name'])

print()

if len(f"{[i.name for i in myfiles.iterdir()]}") < 1:
    sys.exit("No files to rename. Exiting.\n")

for item in myfiles.iterdir():
    try:
        if item.is_file() and item.suffix == '.pdf' and item.name.startswith("R".upper()):
            print(f"file date {dir(myfiles)}")

            print(f"renaming {item.name}")
            # os.rename('old_name.txt', 'new_name.txt')
            regex_pattern = re.compile(r'^IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})\.jpg$')
            match = regex_pattern.match(filename)
            if match:
                year, month, day, hour, minute, second = match.groups()

            spamwriter.writerow([item.name, item.name])
            time.sleep(.125)

    except FileNotFoundError as e:
        print(f"{e}")

print()
