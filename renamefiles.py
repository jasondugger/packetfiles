import csv
import time
import pathlib
import sys
import csv

# spath = input("Enter the directory do you want to copy the files FROM: ")
# dpath = input("Enter the directory do you want to copy the files TO: ")
spath = "c:/Users/jdugg/Documents"
dpath = "c:/Users/jdugg/Documents/testfiles"
csvfilename = "c:/Users/jdugg/Documents/testfiles/packets.csv"

myfiles = pathlib.Path(spath)
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
            print(f"renaming {item.name}")
            spamwriter.writerow([item.name, item.name])
            time.sleep(.125)

    except FileNotFoundError as e:
        print(f"{e}")

print()
