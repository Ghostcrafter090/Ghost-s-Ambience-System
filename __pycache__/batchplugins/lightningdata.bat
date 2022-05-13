set n=0
set count=0

:loopn
bash -c "lynx --dump http://gsweathermore.ddns.net:226/danger.txt" && (
	echo yes
) || (
	goto loop
)
set nf=%n%
for /f "tokens=*" %%a in ('bash -c "lynx --dump http://gsweathermore.ddns.net:226/danger.txt"') do (
	set n=%%a
)
set /a count = %count% - 1
set /a sd = 1000 - (%n% * 100)
if %n% leq 3 (
	echo set strikedistance=%sd% >> lightning.cmd
	if %count% leq -1 goto sk
	echo set st1_lightning_strike_count_last_3hr=%count% >> lightning.cmd
	echo set st1_lightning_strike_count_last_1hr=%count% >> lightning.cmd
	echo set st2_lightning_strike_count_last_3hr=%count% >> lightning.cmd
	echo set st2_lightning_strike_count_last_1hr=%count% >> lightning.cmd
	echo set st1_lightning_strike_last_distance=1000 >> lightning.cmd
	echo set st2_lightning_strike_last_distance=1000 >> lightning.cmd
) else (
	set count=10
	echo set strikedistance=5 >> lightning.cmd
	echo set st1_lightning_strike_count_last_3hr=%count% >> lightning.cmd
	echo set st1_lightning_strike_count_last_1hr=%count% >> lightning.cmd
	echo set st2_lightning_strike_count_last_3hr=%count% >> lightning.cmd
	echo set st2_lightning_strike_count_last_1hr=%count% >> lightning.cmd
	echo set st1_lightning_strike_last_distance=1000 >> lightning.cmd
	echo set st2_lightning_strike_last_distance=1000 >> lightning.cmd
)
:sk
if %count% leq 0 set count = 0
timeout /t 10
goto loopn

:loop
bash -c "lynx --dump http://gsweathermore.ddns.net:226/danger.txt" && (
	goto loopn
) || (
	echo no
)
set st2_lightning_strike_last_distance=derp
del "station1data.cmd" /f /s /q
del "station2data.cmd" /f /s /q
del "station1data.cxl" /f /s /q
del "station2data.cxl" /f /s /q
wget "https://swd.weatherflow.com/swd/rest/observations/station/7489?api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8"
ren "7489@api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8" "station1data.cxl"
wget "https://swd.weatherflow.com/swd/rest/observations/station/5980?api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8"
ren "5980@api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8" "station2data.cxl"
powershell -executionpolicy unrestricted -file llin1.ps1
powershell -executionpolicy unrestricted -file llin2.ps1
ren station1data.cxl station1data.cmd
ren station2data.cxl station2data.cmd
type station1data.cmd > station1data.derp
type station2data.cmd > station2data.derp
type station1data.derp > station1data.cmd
type station2data.derp > station2data.cmd
call station1data.cmd
call station2data.cmd
if %st2_lightning_strike_last_distance%==derp goto new2
powershell -command [Math]::acos((1310.44-((%st1_lightning_strike_last_distance%)*(%st1_lightning_strike_last_distance%))-((%st2_lightning_strike_last_distance%)*(%st2_lightning_strike_last_distance%)))/((0-2)*(%st1_lightning_strike_last_distance%)*(%st2_lightning_strike_last_distance%))) > lnum1.txt
set /p theta=< lnum1.txt
powershell -command [Math]::asin((([Math]::sin(%theta%))/36.2)*(%st1_lightning_strike_last_distance%)) > lnum2.txt
set /p atheta=< lnum2.txt
powershell -command [Math]::sqrt(((21.8)*(21.8))+((%st2_lightning_strike_last_distance%)*(%st2_lightning_strike_last_distance%))-((43.6)*(%st2_lightning_strike_last_distance%)*([Math]::cos(%atheta%)))) > lnum3.txt
set /p strikedistance=< lnum3.txt
echo %strikedistance%
for /f "tokens=1 delims=." %%a in ('echo %strikedistance%') do (
	set strikedistance=%%a
)
if %st1_lightning_strike_count_last_3hr% equ 0 echo maybe & if %st2_lightning_strike_count_last_3hr% equ 0 set strikedistance=1000
echo. > lightning.cmd
echo set strikedistance=%strikedistance% >> lightning.cmd
echo set st1_lightning_strike_count_last_3hr=%st1_lightning_strike_count_last_3hr% >> lightning.cmd
echo set st1_lightning_strike_count_last_1hr=%st1_lightning_strike_count_last_1hr% >> lightning.cmd
echo set st2_lightning_strike_count_last_3hr=%st2_lightning_strike_count_last_3hr% >> lightning.cmd
echo set st2_lightning_strike_count_last_1hr=%st2_lightning_strike_count_last_1hr% >> lightning.cmd
echo set st1_lightning_strike_last_distance=%st1_lightning_strike_last_distance% >> lightning.cmd
echo set st2_lightning_strike_last_distance=%st2_lightning_strike_last_distance% >> lightning.cmd
timeout /t 194
goto loop

:new
echo. > lightning.cmd
set strikedistance=%st1_lightning_strike_last_distance%
if "$%st1_lightning_strike_count_last_3hr%"=="$" set st1_lightning_strike_count_last_3hr=0
if %st1_lightning_strike_count_last_3hr% leq 0 set strikedistance=1000
echo set strikedistance=%strikedistance% >> lightning.cmd
echo set st1_lightning_strike_count_last_3hr=%st1_lightning_strike_count_last_3hr% >> lightning.cmd
echo set st1_lightning_strike_count_last_1hr=%st1_lightning_strike_count_last_1hr% >> lightning.cmd
echo set st2_lightning_strike_count_last_3hr=0 >> lightning.cmd
echo set st2_lightning_strike_count_last_1hr=0 >> lightning.cmd
echo set st1_lightning_strike_last_distance=%st1_lightning_strike_last_distance% >> lightning.cmd
echo set st2_lightning_strike_last_distance=1000 >> lightning.cmd
timeout /t 194
goto loop

:new2
del "station2data.cmd" /f /s /q
del "station2data.cxl" /f /s /q
wget "https://swd.weatherflow.com/swd/rest/observations/station/8994?api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8"
ren "8994@api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8" "station2data.cxl"
powershell -executionpolicy unrestricted -file llin2.ps1
ren station2data.cxl station2data.cmd
type station2data.cmd > station2data.derp
type station2data.derp > station2data.cmd
call station2data.cmd
if "$%st1_lightning_strike_count_last_3hr%"=="$" goto new
if %st1_lightning_strike_count_last_3hr% geq 1 echo maybe & if %st2_lightning_strike_count_last_3hr% leq 0 goto new
set /a d=%st2_lightning_strike_last_distance% + %st1_lightning_strike_last_distance%
if %d% leq 42 set /a st1_lightning_strike_last_distance=%st1_lightning_strike_last_distance% + (41 - %d%)
powershell -command [Math]::acos((((%st2_lightning_strike_last_distance%)*(%st2_lightning_strike_last_distance%))-((%st1_lightning_strike_last_distance%)*(%st1_lightning_strike_last_distance%))-1730)/((0-2)*(%st1_lightning_strike_last_distance%)*(41.6))) > lnum1.txt
set /p atheta=< lnum1.txt
powershell -command (180 - %atheta%) > lnum2.txt
set /p btheta=< lnum2.txt
powershell -command [Math]::sqrt(((12.5)*(12.5))+((%st1_lightning_strike_last_distance%)*(%st1_lightning_strike_last_distance%))-(2*(12.5)*(%st1_lightning_strike_last_distance%)*([Math]::cos(%btheta%)))) > lnum3.txt
set /p strikedistance=< lnum3.txt
echo %strikedistance%
for /f "tokens=1 delims=." %%a in ('echo %strikedistance%') do (
	set strikedistance=%%a
)
if %st1_lightning_strike_count_last_3hr% equ 0 echo maybe & if %st2_lightning_strike_count_last_3hr% equ 0 set strikedistance=1000
echo. > lightning.cmd
echo set strikedistance=%strikedistance% >> lightning.cmd
echo set st1_lightning_strike_count_last_3hr=%st1_lightning_strike_count_last_3hr% >> lightning.cmd
echo set st1_lightning_strike_count_last_1hr=%st1_lightning_strike_count_last_1hr% >> lightning.cmd
echo set st2_lightning_strike_count_last_3hr=%st2_lightning_strike_count_last_3hr% >> lightning.cmd
echo set st2_lightning_strike_count_last_1hr=%st2_lightning_strike_count_last_1hr% >> lightning.cmd
echo set st1_lightning_strike_last_distance=%st1_lightning_strike_last_distance% >> lightning.cmd
echo set st2_lightning_strike_last_distance=%st2_lightning_strike_last_distance% >> lightning.cmd
timeout /t 194
goto loop







