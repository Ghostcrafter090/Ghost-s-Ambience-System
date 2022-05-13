set weather=clear
set temp=273
set windgust=0
:loop
del blowingsnow.dlst /f /s /q
call cond.cmd
set snowdepth=0
bash -c "lynx \"https://www.snow-forecast.com/resorts/Ski-Martock/6day/bot\" --dump" > snowfall.cxl
for /f "tokens=4 delims=: " %%a in ('findstr /c:"Fresh snowfall depth:" snowfall.cxl') do (
	set snowdepth=%%a
)
if "$%weather%"=="$snow " goto sound
if "$%weather%"=="$snow" goto sound
set chance=0
if %temp% geq 275 goto sk
set /a chance = (5 - (%temp% - 273)) * (5 - (%temp% - 273)) * (5 - (%temp% - 273)) * (5 - (%temp% - 273)) * (%snowdepth% + 1)
:sk
if %RANDOM% leq %chance% goto sound
wait wait 194000
goto loop

:sound
set /a volume = (((2500 / 30) * %windgust%) / 100) + 25 + %snowdepth%
echo Blowing Snow Level: %chance% > blowingsnow.dlst
echo Blowing Snow Volume: %volume% >> blowingsnow.dlst
if "$%weather%"=="$snow" (
	set /a volume = %volume% * 2
)
rem pyexec -executescript "file = open(\"snowonwindow.vbs\", \"r+\"); f = file.read(); f = f.replace(\"Sound.Settings.Volume = \", \"Sound.Settings.Volume = %volume% \' \"); print(f);"> snowonwindowa.vbs
rem type snowonwindowa.vbs > snowonwindow.vbs
if not exist nomuffle.derp start /min "" stopaudio snowonwindow
if not exist nomuffle.derp start /min "" cmd.exe /c callaudio window.exe "snowonwindow.mp3" %volume% 0
if not exist nomuffle.derp start /min "" cmd.exe /c callaudio outside.exe "snowwindow.mp3" %volume% 0
if exist nomuffle.derp (
	if "$%weather%"=="$snow " (
		start /min "" stopaudio snowonwindow
		start /min "" cmd.exe /c callaudio windown.exe snowwindow.mp3 %volume% 0
	)
)
wait wait 194000
goto loop
