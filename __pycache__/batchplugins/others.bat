del thloop.derp /f /s /q
goto wloop2
:loop
echo derp > halloweenmode.derp
set day=%date:~8,2%
set month=%date:~5,2%
if "$%day:~0,1%"=="$0" set day=%day:~1,1%
if "$%day:~0,1%"=="$" set day=%day:~1,1%
if "$%month:~0,1%"=="$0" set month=%month:~1,1%
if "$%month:~0,1%"=="$" set month=%month:~1,1%
if exist stophalloween.derp goto wloop
if not exist on.derp goto off
echo Death Night Sounds Active > %1.dlst
set hour=%time:~0,2%
set min=%time:~3,2%
if %hour% geq 10 echo maybe & if %hour% leq 12 goto wloop2
call daytimes.cmd
rem if %date:~5,2% geq 3 echo maybe & if %date:~5,2% leq 10 set /a cesth=%cesth% + 1
rem if %date:~5,2% geq 3 echo maybe & if %date:~5,2% leq 10 set /a ceth=%ceth% + 1
rem if exist thloop.derp goto skip
rem if %hour% geq %cesth% start /b "" "%USERPROFILE%\Desktop\ambience\thunder_storm.vbs"
rem if %hour% geq 18 @echo derp > thloop.derp
:skip
set /a d = %cesth% - 2
if %hour% equ %d% echo maybe & if %min% equ 0 start /b /wait "" "windown.exe" dnwbell1.vbs & timeout /t 60
findstr /c:"set strikedistance=1" "lightning.cmd" && (
	echo nope
)||(
	if %hour% geq %d% echo set strikedistance=1 >> lightning.cmd
)
if %hour% geq %cesth% goto mon
set /a wip = %cesth% - 4
set /a wip2 = %cesth% + 1
if %hour% geq %wip% goto whisper2
timeout /t 1
echo 0 > whisperintensity.cx
echo 0 > wolfhowlintensity.cx
goto loop

:mon
if not exist on.derp goto off
if %hour% geq %wip2% goto mon2
if %min% geq 15 goto wolf
:wloop
if %min% geq 0 goto whisper2
timeout /t 1 
goto loop

:mon2
set randf=%RANDOM%
if exist stophalloween.derp goto wloop
if not exist halloweenmode.derp (
	if %month% equ 10 (
		set randf = %RANDOM% / (32 - %day%)
	)
)
if not exist on.derp goto off
goto wolf2
:whisper
rem if %randf% geq 27768 start /b "" "clock.exe" "whisper.vbs
set fl=0
set clock=0
set window=0
set fire=0
:fl
set randh=%RANDOM%
if %randf% geq 27768 (if %randh% leq 10955 (if not %clock% equ 1 start /b "" "clock.exe" "whisper.vbs" & set clock=1))
if %randf% geq 27768 (if %randh% geq 10955 (if not %window% equ 1 echo maybe & if %randh% leq 21911 start /b "" "windown.exe" "whisper.vbs" & set window=1))
if %randf% geq 27768 (if %randh% geq 21911 (if not %fire% equ 1 start /b "" "fireplace.exe" "whisper.vbs" & set fire=1))
set /a fl=%fl% + 1
if %fl% leq 2 goto fl
goto loop

:whisper2
set day=%date:~8,2%
set month=%date:~5,2%
echo %hour%
echo %cesth%
set /a min = %min% + 1
if not exist on.derp goto off
set /a hourc = %hour% - %cesth%
if %hour% geq %cesth% (
	set /a d = %hour% - %cesth% + 2
	set /a fin = %min% * 50 * %d% + 100
)

set /a fin = %fin% / (%hourc% + 4)
if %hour% lss %cesth% (
	set /a fin = %min% * 100
)
set fin1=%fin%
rem if %hour% geq %cesth% set /a fin1 = %fin% + 1000
set /a minf = %min% - %cestm%
set /a find = %fin1% + ((%minf% + 5) * 1000)
set finc=%fin1%
if %minf% geq -4 echo maybe & if %hour% equ %cesth% (
	set finc=%find%
)
if %minf% geq 8 (
	set /a finc=8000 + %fin1%
)
set fin1=%finc%
if %hour% equ %cesth% (
	for /f "tokens=*" %%a in ('py othersfunc.py %minf% %fin1%') do (
		set fin1=%%a
	)
)
set /a cestj = %cesth% - 2
set /a cestk = %cesth% - 3
set /a cestl = %cesth% - 4
if %hour% lss %cestl% set /a fin1 = %fin1% / 8
if %hour% lss %cestk% set /a fin1 = %fin1% / 6
if %hour% lss %cestj% set /a fin1 = %fin1% / 4
if %hour% lss %cesth% set /a fin1 = %fin1% / 2
set fin=%fin1%
set rard=%RANDOM%
set fina=%fin%
if exist stophalloween.derp goto wloop
if %month% equ 10 set /a fina = %fin% / (32 - %day%)
set /a whispint = (%fina% * 100) / 32768
echo %whispint% > whisperintensity.cx
set fl=0
set clock=0
set window=0
set fire=0
:fl2
set randh=%RANDOM%
if %rard% leq %fina% (if %randh% leq 10955 (if not %clock% equ 1 start /b "" "clock.exe" "whisper.vbs" & set clock=1))
if %rard% leq %fina% (if %randh% geq 10955 (if not %window% equ 1 echo maybe & if %randh% leq 21911 start /b "" "windown.exe" "whisper.vbs" & set window=1))
if %rard% leq %fina% (if %randh% geq 21911 (if not %fire% equ 1 start /b "" "fireplace.exe" "whisper.vbs" & set fire=1))
set /a fl=%fl% + 1
if %fl% leq 2 goto fl2
rem if %rard% leq %fina% echo maybe & if %RANDOM% leq 10955 start /b "" "clock.exe" "whisper.vbs"
rem if %rard% leq %fina% echo maybe & if %RANDOM% geq 10955 echo maybe & if %RANDOM% leq 21911 start /b "" "windown.exe" "whisper.vbs"
rem if %rard% leq %fina% echo maybe & if %RANDOM% geq 21911 start /b "" "fireplace.exe" "whisper.vbs"
if %whispint% geq 10000 goto whispsk
timeout /t 2
:whispsk
timeout /t 1
:ws2
goto loop

:wolf
if not exist on.derp goto off
set /a fin2 = (%min% - 14) * 111 / 4
set /a rand = ((%RANDOM% + 100) / 500) + 1
if %month% equ 10 set /a fin2 = %fin2% / (((32 - %day%) * (32 - %day%)) + 3)
set /a wolfint = (%fin2% * 100) / 32768
echo %wolfint% > wolfhowlintensity.cx
set /a randInt = %RANDOM% / 5461
if exist nomufflewn.derp (
	if %RANDOM% leq %fin2% (
		start /b "" "cmd.exe" "/c windown.exe runaudio.vbs wolf_howl_%randInt%.mp3 & timeout /t %rand% /nobreak & exit "
	)
) else (
	if %RANDOM% leq %fin2% (
		start /b "" "cmd.exe" "/c windown.exe runaudio.vbs wolf_howl_%randInt%_m.mp3 & timeout /t %rand% /nobreak & exit "
	)
)
goto wloop

:wolf2
if not exist on.derp goto off
set /a rand = ((%RANDOM% + 100) / 500) + 1
if not exist halloweenmode.derp (
	if %month% EQU 10 (
		if not %day% equ 13 (
			set randf = %RANDOM% / (((32 - %day%) * (32 - %day%)) + 3)
		)
	)
)
set /a randInt = %RANDOM% / 5461
if exist nomufflewn.derp (
	if %randf% geq 27768 (
		start /b "" "cmd.exe" "/c windown.exe runaudio.vbs wolf_howl_%randInt%.mp3 & timeout /t %rand% /nobreak & exit "
	)
) else (
	if %randf% geq 27768 (
		start /b "" "cmd.exe" "/c windown.exe runaudio.vbs wolf_howl_%randInt%_m.mp3 & timeout /t %rand% /nobreak & exit "
	)
)
goto whisper2

:wloop2
if exist startahalloween.derp goto loop
del halloweenmode.derp /f /s /q
if not exist on.derp goto off
del %1.dlst /f /s /q
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
if %date:~8,2% equ 13 echo maybe & if %DayOfWeek% equ 5 echo maybe & if %time:~0,2% geq 13 goto loop
if %date:~8,2% geq 0 echo maybe & if %date:~5,2% equ 10 echo maybe & if %time:~0,2% geq 13 goto loop
if %date:~8,2% geq 0 echo maybe & if %date:~5,2% equ 10 echo maybe & if %time:~0,2% leq 10 goto loop
timeout /t 1
goto wloop2

:off
timeout /t 10
if exist on.derp goto wloop2
goto off