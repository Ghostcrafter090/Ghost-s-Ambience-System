:loop
if %date:~5,2% equ 10 echo maybe & if %date:~8,2% geq 20 goto trt
if exist "%2.dlst" del "%2.dlst" /f /s /q
nircmdc wait 10000
goto loop

:trt
if not exist "%2.dlst" echo Occasional Trick o' Treaters Stopping By > "%2.dlst"
set rand=32768
set timea=%time:~0,2%
if "$%timea:~0,1%"=="$ " set timea=%timea:~1,1%
set datea=%date:~8,2%
set /a rand2=%rand% * 1000
set /a rand3=%rand2% / 372
set /a rand4=(%rand3% * %timea%)
set /a rand4=(%rand4% / 100) / ((32 - %datea%) * (32 - %datea%))
if %random% leq %rand4% goto fin
nircmdc wait 300000
goto loop

:fin
start "" "clock.exe" "doorbell.vbs"
rem start "" "stream.exe" "doorbell.vbs"
nircmdc wait 10000
set rand=%RANDOM%
if %rand% geq 26215 start "" "clock.exe" "distanttrt5.vbs" & nircmdc wait 300000 & goto loop
if %rand% geq 19662 start "" "clock.exe" "distanttrt4.vbs" & nircmdc wait 300000 & goto loop
if %rand% geq 13109 start "" "clock.exe" "distanttrt3.vbs" & nircmdc wait 300000 & goto loop
if %rand% geq 6556 start "" "clock.exe" "distanttrt2.vbs" & nircmdc wait 300000 & goto loop
if %rand% geq 0 start "" "clock.exe" "distanttrt1.vbs" & nircmdc wait 300000 & goto loop
start "" "clock.exe" "distanttrt1.vbs"
nircmdc wait 300000
goto loop


