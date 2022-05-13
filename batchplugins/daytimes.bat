:loop
del "json@lat=44.847075&lng=-63.604849" /f /s /q
del "daytimes.cxl" /f /s /q
wget "https://api.sunrise-sunset.org/json?lat=44.847075&lng=-63.604849"
ren "json@lat=44.847075&lng=-63.604849" "daytimes.cxl"
powershell -executionpolicy unrestricted -file linday.ps1
type daytimes.cxl > dayderp.cxl
type dayderp.cxl > daytimes.cxl
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"sunset" "daytimes.cxl"') do (
	set cesth=%%b
	set cestm=%%c
	set cestf=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"civil_twilight_begin" "daytimes.cxl"') do (
	set csth=%%b
	set cstm=%%c
	set cstf=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"civil_twilight_end" "daytimes.cxl"') do (
	set ceth=%%b
	set cetm=%%c
	set cetf=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"nautical_twilight_begin" "daytimes.cxl"') do (
	set nsth=%%b
	set nstm=%%c
	set nst=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"nautical_twilight_end" "daytimes.cxl"') do (
	set neth=%%b
	set netm=%%c
	set netf=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"astronomical_twilight_begin" "daytimes.cxl"') do (
	set asth=%%b
	set astm=%%c
	set astf=%%e
)
for /f "tokens=1,2,3,4,5 delims=: " %%a in ('findstr /c:"astronomical_twilight_end" "daytimes.cxl"') do (
	set aeth=%%b
	set aetm=%%c
	set aetf=%%e
)
if %csth% equ 12 echo maybe & if "$%cstf%"=="$AM" set csth=0
if %ceth% equ 12 echo maybe & if "$%cetf%"=="$AM" set ceth=0
if %cesth% equ 12 echo maybe & if "$%cestf%"=="$AM" set cesth=0
if %nsth% equ 12 echo maybe & if "$%nstf%"=="$AM" set nsth=0
if %neth% equ 12 echo maybe & if "$%netf%"=="$AM" set neth=0
if %asth% equ 12 echo maybe & if "$%astf%"=="$AM" set asth=0
if %aeth% equ 12 echo maybe & if "$%aetf%"=="$AM" set aeth=0
if "$%cstf%"=="$PM" set csth=%csth% + 12
if "$%cetf%"=="$PM" set ceth=%ceth% + 12
if "$%cestf%"=="$PM" set cesth=%cesth% + 12
if "$%nstf%"=="$PM" set nsth=%nsth% + 12
if "$%netf%"=="$PM" set neth=%neth% + 12
if "$%astf%"=="$PM" set asth=%asth% + 12
if "$%aetf%"=="$PM" set aeth=%aeth% + 12
set /a csth=%csth% - 3
set /a ceth=%ceth% - 3
set /a cesth=%cesth% - 3
set /a nsth=%nsth% - 3
set /a neth=%neth% - 3
set /a asth=%asth% - 3
set /a aeth=%aeth% - 3
if %csth% lss 0 set /a csth=%csth% + 24
if %ceth% lss 0 set /a ceth=%ceth% + 24
if %cesth% lss 0 set /a cesth=%cesth% + 24
if %nsth% lss 0 set /a nsth=%nsth% + 24
if %neth% lss 0 set /a neth=%neth% + 24
if %asth% lss 0 set /a asth=%asth% + 24
if %aeth% lss 0 set /a aeth=%aeth% + 24
if %cstm:~0,1% equ 0 set cstm=%cstm:~1,1%
if %cetm:~0,1% equ 0 set cetm=%cetm:~1,1%
if %cestm:~0,1% equ 0 set cestm=%cestm:~1,1%
if %nstm:~0,1% equ 0 set nstm=%nstm:~1,1%
if %netm:~0,1% equ 0 set netm=%netm:~1,1%
if %astm:~0,1% equ 0 set astm=%astm:~1,1%
if %aetm:~0,1% equ 0 set aetm=%aetm:~1,1%
echo set csth=%csth% > daytimes.cmd
echo set cstm=%cstm% >> daytimes.cmd
echo set ceth=%ceth% >> daytimes.cmd
echo set cetm=%cetm% >> daytimes.cmd
echo set cesth=%cesth% >> daytimes.cmd
echo set cestm=%cestm% >> daytimes.cmd
echo set nsth=%nsth% >> daytimes.cmd
echo set nstm=%nstm% >> daytimes.cmd
echo set neth=%neth% >> daytimes.cmd
echo set netm=%netm% >> daytimes.cmd
echo set asth=%asth% >> daytimes.cmd
echo set astm=%astm% >> daytimes.cmd
echo set aeth=%aeth% >> daytimes.cmd
echo set aetm=%aetm% >> daytimes.cmd
timeout /t 1000
goto loop


