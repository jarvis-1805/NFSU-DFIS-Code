# CSV

Import-Csv -Path "C:\Users\shubh\Desktop\powershell\internals.csv"
Import-Csv -Path "C:\Users\shubh\Desktop\powershell\internals.csv" | Get-Member

Get-process | Select-Object object projectname, cpu, id -last 10 | sort-object id



# Get-process | Select-Object object projectname, cpu, id -last 10 | sort-object id | Import-Csv -Path "C:\Users\shubh\Desktop\powershell\internals.csv"
