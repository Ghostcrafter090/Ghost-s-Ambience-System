set strikedistance=1000
:loop
if not exist on.derp goto off
set 
call lightning.cmd
call cond.cmd
if %strikedistance% leq 41 goto sound
if "$%weather%"=="$thunder" goto sound
set day=%date:~8,2%
if %date:~8,1% equ 0 set day=%date:~9,1%
if %day% equ 1 echo maybe & if %time:~0,2% equ 12 echo maybe & if %time:~3,2% equ 20 goto test
if %day% equ 15 echo maybe & if %time:~0,2% equ 12 echo maybe & if %time:~3,2% equ 20 goto test
del sthunder.derp /f /s /q
if exist ethunder.derp start "" "radio_thunder_end.vbs" & del ethunder.derp /f /s /q
timeout /t 10
goto loop

:sound
if "$%st1_lightning_strike_count_last_1hr%"=="$ " goto sn
if "$%st2_lightning_strike_count_last_1hr%"=="$ " goto sn
if %st1_lightning_strike_count_last_1hr% equ 0 goto dsk
if %st2_lightning_strike_count_last_1hr% equ 0 goto dsk
:sn
rem if not exist ethunder.derp set windgusta=%windgust%
rem set /a windgustb = %windgusta%+ (35 - %strikedistance%)
rem echo set windgust=%windgustb% >> cond.cmd
if exist sthunder.derp echo maybe & if not exist ethunder.derp start "" "clock.exe" "radio_thunder_start.vbs" & echo derp > ethunder.derp
start "" "window.exe" "tornado_sirens.vbs"
start "" "clock.exe" "tornado_sirens.vbs"
start "" "fireplace.exe" "tornado_sirens.vbs"
:dsk
timeout /t 114
echo derp > sthunder.derp
goto loop

:test
start "" "window.exe" tornado_sirens_test.vbs"
start "" "clock.exe" tornado_sirens_test.vbs"
start "" "fireplace.exe" tornado_sirens_test.vbs"
timeout /t 65
goto loop

:off
timeout /t 10
if exist on.derp goto loop
goto off
