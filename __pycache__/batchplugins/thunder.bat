@echo on
set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
set strikedistance=1000
del thact.derp /f /s /q
set sys=%USERPROFILE%\Desktop\ambience\working
if not exist thunder_storm.vbs goto createthunderstorm
:2
if not exist thunder_heat.vbs goto createthunderheat
:3
if not exist thunder_storm.bat goto thunderstormbatcreate
:4
if not exist thunder_heat.bat goto thunderheatbatcreate
:5
start /wait /b /low "" XCOPY "sounds\thunder\*" "%CD%" /e /c /y
goto loop

:createthunderstorm
echo Set Sound = CreateObject("WMPlayer.OCX.7") > thunder_storm.vbs
echo Sound.URL = "thunder_storm.wav" >> thunder_storm.vbs
echo Sound.Controls.play >> thunder_storm.vbs
echo do while Sound.currentmedia.duration = 0 >> thunder_storm.vbs
echo wscript.sleep 100 >> thunder_storm.vbs
echo loop >> thunder_storm.vbs
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> thunder_storm.vbs
goto 2

:createthunderheat
echo Set Sound = CreateObject("WMPlayer.OCX.7") > thunder_heat.vbs
echo Sound.URL = "thunder_heat.wav" >> thunder_heat.vbs
echo Sound.Controls.play >> thunder_heat.vbs
echo do while Sound.currentmedia.duration = 0 >> thunder_heat.vbs
echo wscript.sleep 100 >> thunder_heat.vbs
echo loop >> thunder_heat.vbs
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> thunder_heat.vbs
goto 3

:thunderstormbatcreate
echo @echo on > thunder_storm.bat
echo @echo derp pipe1 thact.derp >> thunder_storm.bat
echo start /wait "" thunder_storm.vbs >> thunder_storm.bat
echo del thact.derp /f /s /q >> thunder_storm.bat
echo exit >> thunder_storm.bat
powershell -command "(Get-Content -path 'thunder_storm.bat' -Raw) -replace 'pipe1','>' | Set-Content -Path 'thunder_storm.bat'"
goto 4

:thunderheatbatcreate
echo @echo on > thunder_heat.bat
echo @echo derp pipe1 thact.derp >> thunder_heat.bat
echo start /wait "" thunder_heat.vbs >> thunder_heat.bat
echo del thact.derp /f /s /q >> thunder_heat.bat
echo exit >> thunder_heat.bat
powershell -command "(Get-Content -path 'thunder_heat.bat' -Raw) -replace 'pipe1','>' | Set-Content -Path 'thunder_heat.bat'"
goto 5

:loop
@echo on
if not exist on.derp goto null
call cond.cmd
call lightning.cmd
nircmdc wait 1009
if "$%temp:~2,1%"=="$\" goto err
goto errsk
:err
nircmdc wait 1009
@echo on
echo %date%-%time% - ### Conditions Error ### - temp=%temp% ;;; Value Not Possible. ;;;
@echo off
nircmdc wait 1009
set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
goto errsk
nircmdc wait 1009
:errsk
if exist thact.derp goto skip3
nircmdc wait 1009
if %strikedistance% leq 50 goto thunder_storm
if %weather%==thunder goto thunder_storm
nircmdc wait 1009
:skip3
nircmdc wait 1009
set tempc1=%tempc%
if %tempc% leq 15 set tempc1=16
nircmdc wait 1009
if %tempc% leq -8 set /a tempc1 /a = 16 + ((%tempc% * (0 - 1)) - 7)
set time2=%time:~0,2%
nircmdc wait 1009
set horrorindex=0
if exist horrorindex.cx (
	for /f "tokens=1 delims=." %%a in ('type horrorindex.cx') do (
		set horrorindex=%%a
	)
)
set /a temp2=%tempc1% - 15
set /a time3=%time2% * %time2%
rem set /a c1=%time3% * %temp2%
set /a c1 = (%time3% * %temp2%) + %horrorindex%
nircmdc wait 1009
if exist thact.derp goto skip4
if %RANDOM% leq %c1% goto thunder_heat1
nircmdc wait 1009
:skip4
set /a c2= %c1% * 100
set /a percent= %c2% / 32767
echo %percent% > thunder.list
nircmdc wait 1009
timeout /t 194
goto loop

:skip
set th2=0
goto skip2

:thunder_storm
@echo Thunder Storm Sounds Active >> Sounds.list
nircmdc wait 1009
if not exist thact.derp start /b /wait "" "thunder_storm.bat"
goto loop

:thunder_heat1
if %weather%==lightrain goto thunder_storm
nircmdc wait 1009
if %weather%==rain goto thunder_storm
goto thunder_heat

:thunder_heat
@echo Thunder Heat Sounds Active >> Sounds.list
nircmdc wait 1009
if not exist thact.derp start /b /wait "" "thunder_heat.bat"
goto loop

:null
@echo off
if exist on.derp goto loop
nircmdc wait 1000
goto null
