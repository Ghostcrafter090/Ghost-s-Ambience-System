if exist "%USERPROFILE%\Desktop\ambience\thact.prev" start /b "" thunder_storm.bat
del "%USERPROFILE%\Desktop\ambience\thact.prev" /f /s /q

:loop
set day=%date:~8,2%
set month=%date:~5,2%
set hour=%time:~0,2%
set min=%time:~3,2%
if %day:~0,1% equ 0 set day=%day:~1,1%
if %month:~0,1% equ 0 set month=%month:~1,1%
if "$%hour:~0,1%"=="$ " set hour=%hour:~1,1%
if %min:~0,1% equ 0 set min=%min:~1,1%


if %min% equ 0 (
	del *.log /f /s /q
)

set no=0

if %day% equ 31 (
	if %month% equ 10 (
		set no=1
		if %hour% equ 3 (
			if %min% equ 5 (
				shutdown /t 1 /r
			)
		)
	)
)
if %day% equ 13 (
	set no=1
	if %hour% equ 3 (
		if %min% equ 5 (
			shutdown /r /t 1
		)
	)
)
if %day% geq 24 (
	if %day% leq 26 (
		if %month% equ 12 (
			set no=1
			if %hour% equ 3 (
				if %min% equ 5 (
					shutdown /r /t 1
				)
			)
		)
	)
)

for /f "tokens=3 delims= " %%a in ('dir Z:\') do (
        set fren=%%a
)
for /f "tokens=*" %%c in ('echo %fren% ^| bash -c "tr -d \" \""') do (
        set freb=%%c
)
for /f "tokens=*" %%c in ('bash -c "echo $((%freb% / 1000000))"') do (
        set free=%%c
)

if not exist "%USERPROFILE%\Desktop\ambience\%date%_res.cx" echo 0 > "%USERPROFILE%\Desktop\ambience\%date%_res.cx"
for /f "tokens=*" %%a in ('type %USERPROFILE%\Desktop\ambience\%date%_res.cx') do (
	set n=%%a
)


if %no% equ 0 (
	if not exist wcont.derp (
		if not exist gwcont.derp (
			if not exist halloweenmode.derp (
				if not exist emccs.derp (
					if %free% leq 205 (
						set /a n = %n% + 1
						if exist thact.derp echo 0 > "%USERPROFILE%\Desktop\ambience\thact.prev"
						if %n% leq 6 (
							shutdown /r /t 1
						) else (
							start "" nircmdc infobox "The ambience system has encountered a critical error and the entire system has crashed. This is likely due to an out of memmory error. Please expand memmory and restart the system to proceed." "System Critical Error"
							taskkill /f /im window.exe
							taskkill /f /im clock.exe
							taskkill /f /im fireplace.exe
							taskkill /f /im light.exe
							taskkill /f /im ambience_launch.exe
							taskkill /f /im pyexec.exe
							taskkill /f /im timeout.exe
							taskkill /f /im cmd.exe
						)
					)
				)
			)
		)
	)
)
echo %n% > "%USERPROFILE%\Desktop\ambience\%date%_res.cx"
timeout /t 20
goto loop