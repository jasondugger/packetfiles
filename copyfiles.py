import csv
import os
import shutil
import sys
import time

fpath = "Enter the directory do you want to copy the files FROM: "
dpath = "Enter the directory do you want to copy the files TO: "

print("Add the list of packet/file names you want to copy:\n")

flist_in = []
while True:
    filen = input()
    if not filen:
        break
    flist_in.append(filen)
print(flist_in)

# if flist_in.count < 1:
#     sys.exit("No files to copy. Exiting.")