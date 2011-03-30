
param([string]$script)
$date = get-date -format MM/dd/yyyy
$time = [DateTime]::Now.AddSeconds(99)
$tt = get-date $time -format HH:mm:ss

Import-Csv c:\MyPy\qtprunner\schtsk.csv | Select 'Machine', 'User', 'Pwd', 'SC', 'TN', 'RU', 'RP' | 
ForEach-Object {schtasks /create /S $_.Machine /U $_.User /P $_.Pwd /SC $_.SC /TN $_.TN /ST $tt /SD $date /TR $script /RU $_.RU /RP $_.RP}