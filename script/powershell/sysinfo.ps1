function getIP{
    (Get-NetIPAddress).ipv4IPAddress | 
Select-String "192*"
}
write-host (getIP)

$ip = getIP
Write-Host("This machine's IP is $ip")
Write-Host("This machine's IP is {0}")
-f $ip