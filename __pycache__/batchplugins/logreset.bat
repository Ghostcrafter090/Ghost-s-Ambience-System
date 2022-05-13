@echo on

:loop
call system.cmd
set detd=%date:~8,6%
set /a deta = %detd% - 5
if exist "%USERPROFILE%\Desktop\%system%\logs\*-*-%deta%" del "%USERPROFILE%\Desktop\%system%\logs\*-*-%deta%" /f /s /q
set det=%date%
mkdir "%USERPROFILE%\Desktop\%system%\logs\%det%"
start /b /wait /low "" XCOPY "*.log" "%USERPROFILE%\Desktop\%system%\logs\%det%" /c /y
del "*.log" /f /q
nircmdc wait 86400000
goto loop