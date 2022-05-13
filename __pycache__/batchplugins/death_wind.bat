@echo on
XCOPY "sounds\outside\graveyard\*" "%CD%" /e /c /y
goto wloop

:loop
if exist stophalloween.derp goto wloop
if not exist on.derp goto off
set hour=%time:~0,2%
set min=%time:~3,2%
call daytimes.cmd
rem if %date:~5,2% geq 3 echo maybe & if %date:~5,2% leq 10 set /a cesth=%cesth% + 1
set /a m = %cestm% + 11
if %m% geq 60 set /a cesth=%cesth% + 1
if %m% geq 60 set /a m=%m% - 60
if %hour% geq %cesth% goto derp1
timeout /t 1
goto loop

:derp1
if %min% geq %m% goto yes
timeout /t 1
goto loop

:yes
@echo derp > death_wind.derp
timeout /t 1
goto playsound2



:playsound2
echo Death Wind Sounds Active > %1.dlst
if exist stophalloween.derp goto wloop
start /b "" "windown.exe" dnwbell2.vbs
start /b "" "windown.exe" death_wind_fi.vbs
timeout /t 500
if exist stophalloween.derp goto wloop
:playsounda
if exist stophalloween.derp goto wloop
if not exist on.derp goto off
set hour=%time:~0,2%
set min=%time:~3,2%
echo Death Wind Sounds Active > %1.dlst
start /b "" "windown.exe" death_wind.vbs
timeout /t 150
call daytimes.cmd
set /a m2 = %cstm% - 11
if %m2% leq 0 set m2=0
if %hour% leq 12 echo maybe & if %hour% geq %csth% echo maybe & if %min% geq %m2% goto playsounde
goto playsounda

:playsounde
start /b /wait "" "windown.exe" death_wind_fo.vbs
goto wloop

:wloop
if exist starthalloween.derp goto loop
del death_wind.derp /f /s /q
del "%1.dlst" /f /s /q
if not exist on.derp goto off
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
if %date:~8,2% equ 13 echo maybe & if %DayOfWeek% equ 5 echo maybe & if %time:~0,2% geq 13 goto loop
if %date:~8,2% geq 29 echo maybe & if %date:~5,2% equ 10 echo maybe & if %time:~0,2% geq 13 goto loop
timeout /t 1
goto wloop

:off
timeout /t 10
if exist on.derp goto wloop
goto off