# Environment variable

[System.Environment]::SetEnvironmentVariable('firstname','billy' ) 

$env:firstname 

[System.Environment]::SetEnvironmentVariable('firstname','billy',[System.EnvironmentVariableTarget]::user)
