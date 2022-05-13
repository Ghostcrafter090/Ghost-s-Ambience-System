:loop
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
if %date:~8,2% equ 13 echo maybe & if %DayOfWeek% equ 5 echo maybe & if %time:~0,2% geq 13 goto dloop
if %date:~8,2% equ 31 echo maybe & if %date:~5,2% equ 10 echo maybe & if %time:~0,2% geq 13 goto dloop
if exist halloweenmode.derp goto dloop
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
set hour=%time:~0,2%
set min=%time:~3,2%
if %hour% equ 9 echo maybe & if %min% equ 5 start "" "outside.exe" "cb1_out.vbs" & start /wait "" "window.exe" "cb1.vbs" & timeout /t 60
if %hour% equ 10 echo maybe & if %min% equ 35 echo maybe & if %DayOfWeek% equ 0 start "" "outside.exe" "cb2_out.vbs" & start /wait "" "window.exe" "cb2.vbs" & timeout /t 60
if %hour% equ 11 echo maybe & if %min% equ 50 echo maybe & if %DayOfWeek% equ 0 start "" "outside.exe" "cb3_out.vbs" & start /wait "" "window.exe" "cb3.vbs" & timeout /t 60
if %hour% equ 14 echo maybe & if %min% equ 5 start "" "outside.exe" "cb4_out.vbs" & start /wait "" "window.exe" "cb4.vbs" & timeout /t 60
if %hour% equ 18 echo maybe & if %min% equ 5 start "" "outside.exe" "cb5_out.vbs" & start /wait "" "window.exe" "cb5.vbs" & timeout /t 60
timeout /t 1
if not exist on.derp goto null
goto loop

:null
if exist on.derp goto loop
timeout /t 1
goto null

:dloop
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
set hour=%time:~0,2%
set min=%time:~3,2%
if %hour% equ 9 echo maybe & if %min% equ 5 start "" "outside.exe" "cb1_out.vbs" & start /wait "" "window.exe" "cb1.vbs" & start /b /wait "" "windown.exe" "dnwbella.vbs" & timeout /t 60
if %hour% equ 10 echo maybe & if %min% equ 35 echo maybe & if %DayOfWeek% equ 0 start "" "outside.exe" "cb2_out.vbs" & start /wait "" "window.exe" "cb2.vbs" & start /b /wait "" "windown.exe" "dnwbella.vbs" & timeout /t 60
if %hour% equ 11 echo maybe & if %min% equ 50 echo maybe & if %DayOfWeek% equ 0 start "" "outside.exe" "cb3_out.vbs" & start /wait "" "window.exe" "cb3.vbs" & start /b /wait "" "windown.exe" "dnwbella.vbs" & timeout /t 60
if %hour% equ 14 echo maybe & if %min% equ 5 start "" "outside.exe" "cb4_out.vbs" & start /wait "" "window.exe" "cb4.vbs" & start /b /wait "" "windown.exe" "dnwbella.vbs" & timeout /t 60
if %hour% equ 18 echo maybe & if %min% equ 5 start "" "outside.exe" "cb5_out.vbs" & start /wait "" "window.exe" "cb5.vbs" & start /b /wait "" "windown.exe" "dnwbella.vbs" & timeout /t 60
timeout /t 1
if not exist on.derp goto null
goto loop