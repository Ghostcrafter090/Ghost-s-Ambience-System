@echo on
set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
if not exist rain.mp3 goto createrain
:2
if not exist lightrain.mp3 goto createlightrain
:3
start /wait /b /low "" XCOPY "sounds\rain\*" "%CD%" /e /c /y
goto loop

:createrain
echo Set Sound = CreateObject("WMPlayer.OCX.7") > rain.mp3
echo Sound.URL = "rain.wav" >> rain.mp3
echo Sound.Controls.play >> rain.mp3
echo do while Sound.currentmedia.duration = 0 >> rain.mp3
echo wscript.sleep 100 >> rain.mp3
echo loop >> rain.mp3
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> rain.mp3
goto 2

:createlightrain
echo Set Sound = CreateObject("WMPlayer.OCX.7") > lightrain.mp3
echo Sound.URL = "lightrain.wav" >> lightrain.mp3
echo Sound.Controls.play >> lightrain.mp3
echo do while Sound.currentmedia.duration = 0 >> lightrain.mp3
echo wscript.sleep 100 >> lightrain.mp3
echo loop >> lightrain.mp3
echo wscript.sleep (int(Sound.currentmedia.duration)+1)*1000 >> lightrain.mp3
goto 3

:loop
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
if %weather%==rain @echo on & goto rain
if %weather%==lightrain @echo on & goto lightrain
if %weather%==mist goto mist
if %weather%==thunder @echo on & goto rain
del %1.dlst /f /s /q
@echo off
goto loop
:end
wait wait 194000
del %1.dlst /f /s /q
goto loop

:rain
@echo Rain Sounds Active >> %1.dlst
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio "window.exe" rain_nm.mp3 30
) else (
	start /min "" cmd.exe /c callaudio "window.exe" rain.mp3 20
)
start /min "" cmd.exe /c callaudio "outside.exe" rain_nm.mp3 50
if exist nomufflewn.derp (
	start /min "" stopsound  rain
) else (
	start /min "" stopsound  rain_nm
)
start /min "" cmd.exe /c callaudio "clock.exe" lightrain_wall.mp3 50
start /min "" cmd.exe /c callaudio "fireplace.exe" lightrain_wall.mp3 50
goto end

:lightrain
@echo Light Rain Sounds Active >> %1.dlst
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio "window.exe" lightrain_nm.mp3 50
) else (
	start /min "" cmd.exe /c callaudio "window.exe" lightrain.mp3 50
)
start /min "" cmd.exe /c callaudio "outside.exe" lightrain_nm.mp3 50
if exist nomufflewn.derp (
	start /min "" stopsound  lightrain
) else (
	start /min "" stopsound  lightrain_nm
)
start /min "" cmd.exe /c callaudio "clock.exe" lightrain_wall.mp3 50
start /min "" cmd.exe /c callaudio "fireplace.exe" lightrain_wall.mp3 50
goto end

:mist
@echo Light Rain Sounds Active >> %1.dlst
if exist nomufflewn.derp (
	start /min "" cmd.exe /c callaudio "window.exe" mist_nm.mp3 50
) else (
	start /min "" cmd.exe /c callaudio "window.exe" lightrain.mp3 25
)
start /min "" cmd.exe /c callaudio "outside.exe" mist_nm.mp3 50
if exist nomufflewn.derp (
	start /min "" stopsound  lightrain
) else (
	start /min "" stopsound  mist_nm
)
goto end

:null
if exist on.derp goto loop
timeout /t 1
goto null