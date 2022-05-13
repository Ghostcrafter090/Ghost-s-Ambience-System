goto next

:loop
timeout /t 1
goto loop
for /f "tokens=*" %%a in ('tasklist /fi "STATUS eq NOT RESPONDING" /fi "IMAGENAME eq voicemeeter8.exe"') do (
	if not "$%%a"=="$INFO: No tasks are running which match the specified criteria." (
		goto resetloop
	)
)
timeout /t 1
goto loop

:resetloop
set n=0
taskkill /f /im voicemeeter8.exe
powershell -executionpolicy unrestricted -file bluetooth.ps1 off
powershell -executionpolicy unrestricted -file bluetooth.ps1 on
goto connectwait

:connectwait
for /f "tokens=*" %%a in ('BluetoothCL.exe -timeout 1 ^| bash -c "grep Audio" ^| bash -c "wc -l"') do (
	if %%a geq 4 goto next
)
set /a n = %n% + 1
if %n% geq 20 goto next
goto connectwait

:next
start "" "C:\Users\Administrator\Desktop\Voicemeeter.lnk"
goto loop
		