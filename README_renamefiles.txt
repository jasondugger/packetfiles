in requested folder x, rename all files ending in .pdf to remove the non-packetID (Rxxxx)
for example R123456-tellercheck.pdf will become R123456.pdf

question: "Enter the folder where the files are:"
src_dir: "K:\Divisions\Appraisal\Commercial\Shared\2023\Appeals\41.461\Packets for Agents\1 MASTER APPEAL PACKET"
src_dir + /

file_list = all files in src_dir

rename_logfname: 'renamefiles_' + $datetime + '.log'
backout_logfname: 'backout_log_' + $datetime + '.log'

renamelog: []
backoutlog: []

for i in files_list:
  if i matches '\w\d?-.*\.pdf'
    n = i.Split('-')[0] + .pdf
    n is done in-line
    renamelog.append("renamed file i to n")
  elif file matches '\w\d? .*\.pdf'
    n = i.Split(' ')[0] + .pdf
    n is done in-line
    renamelog.append("renamed file i to n")
  else:
    renamelog.append("did not to rename i")


open a new file called rename_logfname.csv
rename_logfname.writelines(renamelog)

open a new file called backout_logfname.csv
backout_logfname.writelines(backoutlog)

