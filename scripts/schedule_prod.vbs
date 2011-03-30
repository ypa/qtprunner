Dim oShell
Set oShell = CreateObject ("WScript.shell")
oShell.Run "powershell c:\MyPy\qtprunner\run_tsk.ps1 c:\runscripts\runscript_prod.vbs"
'oShell.Run "python c:\MyPy\testtime.py"
Set oShell = Nothing