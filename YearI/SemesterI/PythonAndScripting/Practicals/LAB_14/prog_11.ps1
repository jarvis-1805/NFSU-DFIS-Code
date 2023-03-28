# Text
New-item -Path "C:\Users\shubh\Desktop\powershell\file1.txt" -ItemType File -Force
$data="This is first line 1 "

Add-content -value $data -Path "C:\Users\shubh\Desktop\powershell\file1.txt"
Add-content -value "This is line number 2 "-Path "C:\Users\shubh\Desktop\powershell\file1.txt"

$data | add-content  -Path "C:\Users\shubh\Desktop\powershell\file1.txt"

clear-content -Path "C:\Users\shubh\Desktop\powershell\file1.txt"
Remove-item -Path "C:\Users\shubh\Desktop\powershell\file1.txt -Force"
