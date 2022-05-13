set min=%time:~3,2%
if %min:~0,1% equ 0 set min=%min:~1,1%
set /a mina = %min% + 2
set /a minb = %mina% - 30
if %minb% lss 0 set /a minb = %minb% + 60

:loop
set min=%time:~3,2%
if %min:~0,1% equ 0 set min=%min:~1,1%
if %min% equ %mina% (start "" clock.exe ticking.vbs) & timeout /t 60
if %min% equ %minb% (start "" clock.exe ticking.vbs) & timeout /t 60
nircmdc wait 300
goto loop
