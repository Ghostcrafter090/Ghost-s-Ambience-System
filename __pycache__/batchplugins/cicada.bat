set tempc=0
:loop
set month=%date:~5,2%
if %month:~0,1% equ 0 set month=%month:~1,1%
set /a day = (%month% * 30) + %date:~8,2%
call cond.cmd
echo 1 > cinum.cx
set /a num2 = %tempc% - 15
if %num2% leq 0 timeout /t 1 & goto loop
echo %num2% > cinum2.cx
for /l %%a in (1,1,%num2%) do (
	for /f "tokens=1" %%b in ('type cinum.cx') do (
		start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > cinum.cx
	)
)
set /p per=< cinum.cx
set /a per = %per% * 5
set /a per = %per% / ((((300 - %day%) * (300 - %day%) * (300 - %day%) * (300 - %day%)) + 1) / 4100625)
echo %per% > cicadaindex.cx
call daytimes.cmd
if %time:~0,2% geq %ceth% goto dsk
if %time:~0,2% lss %csth% goto dsk
if exist nomufflewn.derp (
	start /min "" stopsound  cicada_windowclosed
) else (
	start /min "" stopsound  cicada_windowopen
)
if %RANDOM% leq %per% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe cicada_windowopen.mp3 100 0
if %RANDOM% leq %per% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe cicada_windowclosed.mp3 100 0
:dsk
wait wait 194000
goto loop
