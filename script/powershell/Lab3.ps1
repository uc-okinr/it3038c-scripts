function getIP{
    (Get-NetIPAddress).IPv4address | 
Select-String "192*"
}

write-host (getIP)
$Version = $Host.Version.Major
$Name = hostname
$IP = getIP
$Date = (Date).DateTime

$Body = "This machine's IP is $IP. User is $env:username. Hostname is $Name. Powershell version $Version . Today's date is $Date"

Write-Host ($Body)
