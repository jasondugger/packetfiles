question: "Enter the directory do you want to copy the files FROM:"
src_dir: "K:\Divisions\Appraisal\Commercial\Shared\2023\Appeals\41.461\Packets for Agents\1 MASTER APPEAL PACKET"
src_dir + /

question: "Enter the directory do you want to copy the files TO:"
dst_dir: "c:\new_files"
dst_dir + /
dst_dir + $datetime + '\'

question: "Add the list of packet/file names you want to copy:"
files_list: "blah.pdf, blah2.pdf"
* should be able to copy and paste multiple files from an excel column
if files_list is a string:
  split by comma
else:
  no change

copylogfname: 'copylog_' + $datetime + '.log'
failed_logfname: 'failed_log_' + $datetime + '.log'

copylog: []
fail_log: []

for i in files_list:
  if not i:
    failed_log.append("File doesn't exist: $SrcDirName$fullFileName")
  else:
    copy the file from src to dst
    copy_log.append("Copied file: $SrcDirName$fullFileName")

open a new file called copy_files_log.csv
copy_files_log.writelines(copylog)

open a new file called failed_files_log.csv
failed_files_log.writelines(fail_log)

