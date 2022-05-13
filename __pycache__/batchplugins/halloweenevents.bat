:loop
call daytimes.cmd
set datea=%date:~5,2%
set dateb=%date:~8,2%
if %dateb:~0,1% equ 0 set dateb=%dateb:~1,1%
set timea=%time:~0,2%
if "$%timea:~0,1%"=="$ " set timea=%timea:~1,1%
set timeb=%time:~3,2%
if %timeb:~0,1% equ 0 set timeb=%timeb:~1,1%
set /a cestj = %cesth% - 1
if not %datea% equ 10 goto sk
if %timea% equ %cesth% echo maybe & if %timeb% equ %cestm% (
		start "" "windown.exe" darkrumble.vbs
		start "" "clock.exe" darkrumble.vbs
		start "" "fireplace.exe" darkrumble.vbs
		timeout /t 60
)
if %timea% equ %cestj% (
	if %timeb% equ %cestm% (
		start "" "windown.exe" darkrumble.vbs
		start "" "clock.exe" darkrumble.vbs
		start "" "fireplace.exe" darkrumble.vbs
		timeout /t 60
	)
)
if %timea% equ %ceth% (
	if %timeb% equ %cetm% (
		start "" "windown.exe" darkrumble.vbs
		start "" "clock.exe" darkrumble.vbs
		start "" "fireplace.exe" darkrumble.vbs
		timeout /t 60
	)
)
if %timea% equ %neth% (
	if %timeb% equ %netm% (
		start "" "windown.exe" darkrumble.vbs
		start "" "clock.exe" darkrumble.vbs
		start "" "fireplace.exe" darkrumble.vbs
		timeout /t 60
	)
)
if %timea% equ %aeth% (
	if %timeb% equ %aetm% (
		start "" "windown.exe" darkrumble.vbs
		start "" "clock.exe" darkrumble.vbs
		start "" "fireplace.exe" darkrumble.vbs
		timeout /t 60
	)
)
if %dateb% equ 31 (
	if %timea% equ 23 (
		if %timeb% equ 45 (
			start "" "windown.exe" midnightonhalloween.vbs
			start "" "clock.exe" midnightonhalloween.vbs
			start "" "fireplace.exe" midnightonhalloween.vbs
			timeout /t 60
		)
	)
)
:sk
if %datea% equ 10 echo maybe & if %dateb% geq 25 echo maybe & if %timea% equ 11 echo maybe & if %timeb% equ 11 start "" "windown.exe" "draculasrevenge.vbs" & start "" "stream.exe" "draculasrevenge.vbs" & timeout /t 60 & goto loop
if %datea% equ 11 echo maybe & if %dateb% equ 1 echo maybe & if %timea% equ 3 echo maybe & if %timeb% equ 11 start "" "windown.exe" "comelittlechildren.vbs" & start "" "stream.exe" "comelittlechildren.vbs" & timeout /t 60 & goto loop
if %datea% equ 10 echo maybe & if %dateb% geq 20 echo maybe & if %timea% equ 3 echo maybe & if %timeb% equ 11 start "" "windown.exe" "comelittlechildren.vbs" & start "" "stream.exe" "comelittlechildren.vbs" & timeout /t 60 & goto loop
nircmdc wait 10000
goto loop