[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing")
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

## create form object
$objForm = New-Object System.Windows.Forms.Form
$objForm.Text = "Data Entry Form"
$objForm.Size = New-Object System.Drawing.Size(600,500)
$objForm.StartPosition = "CenterScreen"

## create CANCEL button
$CancelButton = New-Object System.Windows.Forms.Button
$CancelButton.Location = New-Object System.Drawing.Size(300,425)
$CancelButton.Size = New-Object System.Drawing.Size(75,23)
$CancelButton.Text = "Cancel"
$CancelButton.Add_Click({$objForm.Close()})
$objForm.Controls.Add($CancelButton)

## create OK button
$OKButton = New-Object System.Windows.Forms.Button
$OKButton.Location = New-Object System.Drawing.Size(200,425)
$OKButton.Size = New-Object System.Drawing.Size(75,23)
$OKButton.Text = "OK"
$OKButton.Add_Click({$objSrcDir=$objSrcDirTextBox.Text;$objFiles=$objFilesTextBox.Text;$objDstDir=$objDstDirTextBox.Text;$objForm.Close()})
$objForm.Controls.Add($OKButton)

## create src dir label
$objDirLabel = New-Object System.Windows.Forms.Label
$objDirLabel.Location = New-Object System.Drawing.Size(10,20)
$objDirLabel.Size = New-Object System.Drawing.Size(400,20)
$objDirLabel.Text = "Enter the directory do you want to copy the files FROM:"
$objForm.Controls.Add($objDirLabel)

## create src dir textbox
$objSrcDirTextBox = New-Object System.Windows.Forms.TextBox
$objSrcDirTextBox.Location = New-Object System.Drawing.Size(10,45)
$objSrcDirTextBox.Size = New-Object System.Drawing.Size(400,20)
$objSrcDirTextBox.Text = "K:\Divisions\Appraisal\Commercial\Shared\2023\Appeals\41.461\Packets for Agents\1 MASTER APPEAL PACKET"
$objForm.Controls.Add($objSrcDirTextBox)

## create dst dir label
$objDirLabel = New-Object System.Windows.Forms.Label
$objDirLabel.Location = New-Object System.Drawing.Size(10,90)
$objDirLabel.Size = New-Object System.Drawing.Size(400,20)
$objDirLabel.Text = "Enter the directory do you want to copy the files TO:"
$objForm.Controls.Add($objDirLabel)

## create dst dir textbox
$objDstDirTextBox = New-Object System.Windows.Forms.TextBox
$objDstDirTextBox.Location = New-Object System.Drawing.Size(10,110)
$objDstDirTextBox.Size = New-Object System.Drawing.Size(400,20)
$objForm.Controls.Add($objDstDirTextBox)

## create files label
$objFileLabel = New-Object System.Windows.Forms.Label
$objFileLabel.Location = New-Object System.Drawing.Size(10,160)
$objFileLabel.Size = New-Object System.Drawing.Size(400,20)
$objFileLabel.Text = "Add the list of packet/file names you want to copy:"
$objForm.Controls.Add($objFileLabel)

## create files textbox
$objFilesTextBox = New-Object System.Windows.Forms.TextBox
$objFilesTextBox.Location = New-Object System.Drawing.Size(10,185)
$objFilesTextBox.Size = New-Object System.Drawing.Size(400,200)
$objFilesTextBox.Multiline = $True
$objFilesTextBox.WordWrap = $True
$objFilesTextBox.Scrollbars = "Vertical"
$objForm.Controls.Add($objFilesTextBox)

## focus form to front of screen
$objForm.Topmost = $True
$objForm.Add_Shown({$objForm.Activate()})
[void] $objForm.ShowDialog()

$SrcDirName = $($objSrcDirTextBox.Text).trim('\') + '\'
$DstDirName = $($objDstDirTextBox.Text).trim('\') + '\'

# create the new sub-directory the files will go into
[string]$folderDate = Get-Date -Format "MMddyyyy"
[string]$newDirName = 'NewFolder_' + $folderDate + '\'
New-Item -ItemType Directory -Force -Path $DstDirName$newDirName

# set up the log files
[string]$LogDirName = "c:\logs\"
New-Item -ItemType Directory -Force -Path $LogDirName
[string]$logtime = Get-Date -Format "MMddyyyyHHmm"
[string]$logfile = $LogDirName + 'copyfiles_' + $logtime + '.log'
Out-File -FilePath $logfile

$fileNames = $($objFilesTextBox.Text).Split([Environment]::NewLine, [StringSplitOptions]::RemoveEmptyEntries)
foreach ($fileName in $fileNames)
{
    [string]$fullFileName = $fileName.trim('.pdf') + '.pdf'
    if (-not(Test-Path -Path $SrcDirName$fullFileName -PathType Leaf)) {
        Write "File doesn't exist: $SrcDirName$fullFileName" -Verbose
        Write "File doesn't exist: $SrcDirName$fullFileName" >> $logfile
    } else {
        Copy-Item -Path $SrcDirName$fullFileName -Destination $DstDirName$newDirName$fullFileName
        Write "Copied $SrcDirName$fullFileName to $DstDirName$newDirName$fullFileName" -Verbose
        # Write "Copied $SrcDirName$fullFileName to $DstDirName$newDirName$fullFileName" >> $logfile
    }
}

Read-Host -Prompt "Press Enter to exit"
