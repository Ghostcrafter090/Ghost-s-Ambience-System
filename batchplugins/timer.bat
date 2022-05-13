if not exist timer.cx echo 1000 > timer.cx
:loop
set min=%time:~3,2%
set hour=%time:~0,2%
dir /s /b "C:\Users\Jones\Documents\Snooper Professional\*.xml" && (
	del "C:\Users\Jones\Documents\Snooper Professional\*.xml" /f /s /q
	set hour=%time:~0,2%
	set /a h1 = %hour% - 12
	set /a h2 = %h1% * %h1%
	set /a h3 = %h2% * 100
	set /a h4 = %h3% / 2
	set /a h5 = %h4% + 600
	set min=%time:~3,2%
	rem if %min% leq 20 echo %h5% > timer.cx
	rem if %min% geq 30 echo maybe & if %min% leq 50 echo %h5% > timer.cx
	echo %h5% > timer.cx
	
)||(
	echo nope
)
nircmdc wait 1009
set /p tim=< timer.cx
set /a tim = %tim% - 1
nircmdc wait 1009
if exist dsound.derp echo maybe & if %tim% geq 0 echo maybe & if not exist on.derp echo %time% %date% - switch on >> "%USERPROFILE%\dlog.log"
if exist dsound.derp echo maybe & if %tim% leq 0 echo maybe & if exist on.derp echo %time% %date% - switch off >> "%USERPROFILE%\dlog.log"
nircmdc wait 1009
if exist dsound.derp echo maybe & if %tim% leq 0 del on.derp /f /s /q
nircmdc wait 1009
if exist dsound.derp echo maybe & if %tim% geq 0 echo derp > on.derp
timeout /t 1
echo %tim% > timer.cx
goto loop