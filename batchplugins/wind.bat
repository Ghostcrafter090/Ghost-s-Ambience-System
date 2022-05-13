@echo on
set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
if not exist wind.mp3 goto windcreate
:2
if not exist hurricane_wail.mp3 goto hurricane_wailcreate
:3
start /wait /b /low "" XCOPY "sounds\wind\*" "%CD%" /e /c /y
goto loop



:windcreate
echo Set Sound = CreateObject("WMPlayer.OCX.7") > wind.mp3
echo Sound.URL = "wind.wav" >> wind.mp3
echo Sound.Controls.play >> wind.mp3
echo do while Sound.currentmedia.duration = 0 >> wind.mp3
echo wscript.sleep 100 >> wind.mp3
echo loop >> wind.mp3
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> wind.mp3
goto 2

:hurricane_wailcreate
echo Set Sound = CreateObject("WMPlayer.OCX.7") > hurricane_wail.mp3
echo Sound.URL = "hurricane_wail.wav" >> hurricane_wail.mp3
echo Sound.Controls.play >> hurricane_wail.mp3
echo do while Sound.currentmedia.duration = 0 >> hurricane_wail.mp3
echo wscript.sleep 100 >> hurricane_wail.mp3
echo loop >> hurricane_wail.mp3
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> hurricane_wail.mp3
goto 3

:loop
wait wait 194000
del %1*.dlst /f /s /q
if not exist on.derp goto null
call cond.cmd
if "$%temp:~2,1%"=="$\" goto err
goto errsk
:err
@echo on
echo %date%-%time% - ### Conditions Error ### - temp=%temp% ;;; Value Not Possible. ;;;
@echo off
set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
goto errsk
:errsk
rem if %windspeed% geq 7 goto wind
if %windgust% geq 14 goto lcw
if %windspeed% geq 12 goto lcw
:c1
if %windgust% geq 16 goto lw
if %windspeed% geq 10 goto lw
:c2
if %windgust% geq 20 goto w
if %windspeed% geq 18 goto w
:c3
if %windgust% geq 27 goto cw
if %windspeed% geq 23 goto cw
:c4
:cont1
if %windspeed% geq 30 goto hurricane_wail1
:cont2
if %windgust% geq 30 goto hurricane_wail2
:cont3
rem if %windspeed% geq 12 goto end
:cont6
rem if %windspeed% geq 30 goto end
:cont4
rem if %windgust% geq 15 goto end
:cont5
timeout /t 1
goto loop
:end
del %1*.dlst /f /s /q
goto loop

:wind
@echo Wind Sounds Active >> sounds.list
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio windown.exe wind_nm.mp3
) else (
	start /min "" cmd.exe /c callaudio window.exe wind.mp3
)
if exist nomufflewn.derp (
	start /min "" stopsound  wind
) else (
	start /min "" stopsound  wind_nm
)
goto cont1

:hurricane_wail1
@echo Hurricane Wail Sounds Active > %1d.dlst
start "" fireplace.exe hurricane_wail.vbs
start "" clock.exe hurricane_wail.vbs
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio windown.exe hurricane_wail_nm.mp3
) else (
	start /min "" cmd.exe /c callaudio window.exe hurricane_wail.mp3
)
if exist nomufflewn.derp (
	start /min "" stopsound  hurricane_wail
) else (
	start /min "" stopsound  hurricane_wail_nm
)
goto cont2

:hurricane_wail2
@echo Hurricane Wail Sounds Active > %1d.dlst
start "" fireplace.exe hurricane_wail.vbs
start "" clock.exe hurricane_wail.vbs
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio windown.exe hurricane_wail_nm.mp3
) else (
	start /min "" cmd.exe /c callaudio window.exe hurricane_wail.mp3
)
if exist nomufflewn.derp (
	start /min "" stopsound  hurricane_wail
) else (
	start /min "" stopsound  hurricane_wail_nm
)
goto cont3

:null
if exist on.derp goto loop
timeout /t 1
goto null

:lcw
@echo Light Chimney Wind Sounds Active > %1a.dlst
start "" "fireplace.exe" "light_chimney_wind.vbs"
goto c1

:lw
@echo Light Wind Sounds Active > %1b.dlst
start "" "clock.exe" "light_wind.vbs"
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio "windown.exe" "light_wind_nm.mp3"
) else (
	start /min "" cmd.exe /c callaudio "window.exe" "light_wind.mp3"
)
if exist nomufflewn.derp (
	start /min "" stopsound  light_wind
) else (
	start /min "" stopsound  light_wind_nm
)
start "" "fireplace.exe" "light_wind.vbs"
goto c2

:w
@echo Wind Sounds Active > %1c.dlst
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio "windown.exe" "wind_nm.mp3"
) else (
	start /min "" cmd.exe /c callaudio "window.exe" "wind.mp3"
)
if exist nomufflewn.derp (
	start /min "" stopsound  wind
) else (
	start /min "" stopsound  wind_nm
)
goto c3

:cw
@echo Chimney Wind Sounds Active >> %1.dlst
start "" "fireplace.exe" "chimney_wind.vbs"
goto c4



