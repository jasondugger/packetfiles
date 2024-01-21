import csv
import os
import sys
import time

flist_in = []

print("")
print("Add the origin folder to find the files you want to copy:")
folder = input()

if not folder:
    sys.exit("No origin directory entered. Exiting.\n")

print("")
print("Add the list of packet/file names you want to copy")
print("Enter filenames either one at a time or a comma separated list")
print("When done, press ENTER:\n")

# /Users/jd02g5/gitrepos/packetfiles/packets
# customer1.pdf

while True:
    filen = input().split(',')
    if filen[0] == "":
        break
    flist_in += filen

if not flist_in:
    sys.exit("No files to copy. Exiting.\n")

with open('files_copied.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['File Name', 'Origin Folder'])
    for file in flist_in:
        if os.path.isfile(folder + "/" + file):
            print('File found: ' + folder + "/" + file)
            writer.writerow([file, folder])
        else:
            print('File not found: ' + folder + "/" + file)
            writer.writerow([file, folder, 'File not found'])
print("")
