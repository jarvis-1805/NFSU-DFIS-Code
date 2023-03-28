# try and catch

Try {
 Get-Item rgtest
 Write-host 'still running'
} catch { 
  Write-host 'nt found'
}
 
Try {
  Get-Item rgtest -ErrorAction stop
  Write-host 'still running'
} catch { 
  Write-host 'not found'
  Write-host $_.Exception.message
}

$ErrorActionPreference='Stop'

Try {
  Get-Item rgtest
  Get-Item rgtest
  Write-host 'still running'
} catch { 
  Write-host 'not found'
  Write-host $_.Exception.message
} finally { 
  Write-host 'always execute'
}
