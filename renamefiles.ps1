
[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')
$title = 'Files Follder'
$msg   = 'Enter the folder where the files are:'
[string]$folderName = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
$folderName=$folderName.trim('\') + '\'
Write "Renaming files in folder $folderName" -Verbose
[string]$logtime=Get-Date -Format "MMddyyyy-HHmm"
[string]$logfile=$folderName + 'renamefiles-' + $logtime + '.log'
Out-File -FilePath $logfile
[string]$backoutfile=$folderName + 'unrenamefiles-' + $logtime + '.bat'
Out-File -FilePath $backoutfile
Get-ChildItem -Path $folderName | ForEach-Object {
  if ( $_.Extension -eq '.pdf' )
    {
        $newname = $_.BaseName.Split(' ')[0] + $_.Extension
        Write "File '$_.FullName' renamed to '$newName'" -Verbose
        Write "File '$_.FullName' renamed to '$newName'" >> $logfile
        Write "ren ""$newName"" ""$_""" >> $backoutfile
        Rename-Item -Path $_.FullName -NewName $newname
    }
}
Read-Host -Prompt "Press Enter to exit"

