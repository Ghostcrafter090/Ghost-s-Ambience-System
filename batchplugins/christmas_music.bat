:loop
if not exist on.derp goto off
del %1.dlst /f /s /q
set day=%date:~8,6%
set month=%date:~5,2%
set hour=%time:~0,2%
set min=%time:~3,2%
if %month% geq 11 goto maybe
nircmdc wait 10000
rem if not exist "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx" echo 0 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem set /p preval=< "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem if not %preval% equ 0 echo 0 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
goto loop

:maybe
if %month% geq 12 (
	if %day% geq 1 goto almost
)
if %month% geq 11 (
	if %day% geq 12 goto almost
)
nircmdc wait 1000
rem if not exist "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx" echo 0 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem set /p preval=< "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem if not %preval% equ 0 echo 0 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
goto loop

:almost
nircmdc wait 1000
if %hour% equ 11 goto loop
if %hour% equ 12 echo maybenot & if %min% leq 10 goto loop
if %hour% geq 9 echo sorta & if %hour% lss 10 goto yes
if %hour% geq 9 echo sorta & if %hour% lss 17 echo almost & if %min% leq 20 echo almostmaybe & if %min% geq 10 goto yes
goto loop

:yes
rem if not exist "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx" echo 0 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem set /p preval=< "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
rem if not %preval% equ 1 echo 1 > "C:\inetpub\wwwroot\GSWeather\data\ambience\holiday.cx"
@echo on
set rand=%RANDOM%
echo Christmas Music Active > %1.dlst
if %rand% geq 16385 start /wait "" "windown.exe" "ch_music_main.vbs"
if %rand% leq 16384 start /wait "" "windown.exe" "ch_music_main2.vbs"
goto loop

:off
timeout /t 10
if exist on.derp goto loop
goto off