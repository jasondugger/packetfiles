import csv
import os
import pathlib
import sys
import shutil

# spath = input("Enter the directory do you want to copy the files FROM: ")
# dpath = input("Enter the directory do you want to copy the files TO: ")
spath = "c:/Users/jdugg/Documents"
dpath = "c:/Users/jdugg/Documents/testfiles"

print("Add the list of packet/file names you want to copy:\n")

flist_in = []
while True:
    filen = input()
    if not filen:
        break
    flist_in.append(filen)

if len(flist_in) == 0:
    sys.exit("No files to copy. Exiting.\n")

for item in flist_in:
    try:
        shutil.copyfile(f"{spath}/{item}", f"{dpath}/{item}")
        print(f"copied {spath}/{item} to {dpath}/{item}")
    except FileNotFoundError as e:
        print(f"{e}")


print()
