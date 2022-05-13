set da=0
:loop
if not exist on.derp goto off
call cond.cmd
call daytimes.cmd
set nmcond=0
if %temp% geq 285 echo maybe & if %windgust% leq 15 echo maybe & if not %weather%==rain echo maybe & if not %weather%==lightrain echo maybe & if not %weather%==thunder echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio "clock.exe" "openwindow1.mp3" & taskkill /f /im wait.exe
if %temp% geq 285 echo maybe & if %windgust% leq 15 echo maybe & if not %weather%==rain echo maybe & if not %weather%==thunder echo maybe & if not %weather%==lightrain echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio "window.exe" "openwindow2.mp3" & echo derp > nomufflewn.derp & taskkill /f /im wait.exe
if %temp% geq 285 echo maybe & if %windgust% leq 15 echo maybe & if not %weather%==rain echo maybe & if not %weather%==lightrain echo maybe & if not %weather%==thunder set nmcond=1 & taskkill /f /im wait.exe
if %nmcond% equ 0 echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio "clock.exe" "closewindow1.mp3" & taskkill /f /im wait.exe
if %nmcond% equ 0 echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio "window.exe" "closewindow1.mp3" & del nomufflewn.derp /f /s /q & taskkill /f /im wait.exe
if %temp% leq 284 echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio "clock.exe" "closewindow1.mp3" & taskkill /f /im wait.exe
if %temp% leq 284 echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio "window.exe" "closewindow1.mp3" & del nomufflewn.derp /f /s /q & taskkill /f /im wait.exe
set /a rand = 37 * (%windgust% - 22)
if %windgust% geq 23 echo maybe & if not exist windowbroke.derp echo maybe & if %RANDOM% leq %rand% goto breakwindow
:bwe
if exist windowbroke.derp echo derp > nomufflewn.derp
:fwe
rem if %date:~5,2% lss 4 echo maybe & if %date:~5,2% geq 2 set /a csth=%csth% + 1
rem if %date:~5,2% lss 4 echo maybe & if %date:~5,2% geq 2 set /a ceth=%ceth% + 1
rem if %date:~5,2% lss 4 echo maybe & if %date:~5,2% geq 2 set /a cesth=%cesth% + 1
rem if %date:~5,2% lss 4 echo maybe & if %date:~5,2% geq 2 set /a nsth=%nsth% + 1
rem if %date:~5,2% lss 4 echo maybe & if %date:~5,2% geq 2 set /a neth=%neth% + 1
rem if %date:~5,2% gtr 8 echo maybe & if %date:~5,2% leq 10 set /a csth=%csth% + 1
rem if %date:~5,2% gtr 8 echo maybe & if %date:~5,2% leq 10 set /a ceth=%ceth% + 1
rem if %date:~5,2% gtr 8 echo maybe & if %date:~5,2% leq 10 set /a cesth=%cesth% + 1
rem if %date:~5,2% gtr 8 echo maybe & if %date:~5,2% leq 10 set /a nsth=%nsth% + 1
rem if %date:~5,2% gtr 8 echo maybe & if %date:~5,2% leq 10 set /a neth=%neth% + 1
if %temp% geq 278 goto warm
if %temp% lss 278 goto warfo
:cont
if %temp% leq 283 goto cold
if %temp% gtr 283 goto colfo
:ed
set db=%date:~8,2%
if %db:~0,1% equ 0 set db=%db:~1,1%
if exist windowbroke.derp echo derp & set /p da=< windowbroke.derp
if exist windowbroke.derp echo derp & if %db% geq %da% goto fixwindow
del outwhite.dlst /f /s /q
if exist w_wn_d.derp echo Warm Daytime Outside Whitenoise Sounds Active >> outwhite.dlst
if exist w_wn_m.derp echo Warm Morning Outside Whitenoise Sounds Active >> outwhite.dlst
if exist w_wn_e.derp echo Warm Evening Outside Whitenoise Sounds Active >> outwhite.dlst
if exist w_wn_n.derp echo Warm Nighttime Outside Whitenoise Sounds Active >> outwhite.dlst
if exist c_wn_d.derp echo Cold Daytime Outside Whitenoise Sounds Active >> outwhite.dlst
if exist c_wn_n.derp echo Cold Nighttime Outside Whitenoise Sounds Active >> outwhite.dlst
timeout /t 194
goto loop

:warm
set /a cseth=%csth% + 3
if %cseth% geq 24 set /a cseth = %cseth% - 23
set /a cstm2=%cstm% + 20
if %cstm2% geq 60 set /a cstm2 = %cstm2% - 60
echo %csth%
echo %cstm%
echo %ceth%
echo %cetm%
echo %cesth%
echo %cestm%
echo %nsth%
echo %nstm%
echo %neth%
echo %netm%
echo %asth%
echo %astm%
echo %aeth%
echo %aetm%
echo %cseth%
echo %cstm2%
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi.mp3" & echo derp > w_wn_n.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi.mp3" & echo derp > w_wn_n.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm2% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi.mp3" & echo derp > w_wn_n.derp


if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %ceth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo.mp3" & del w_wn_n.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %ceth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo.mp3" & del w_wn_n.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %ceth% echo maybe & if %time:~3,2% lss %cetm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo.mp3" & del w_wn_n.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %cesth% echo maybe & if %time:~3,2% geq %cestm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% geq %netm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi.mp3" & echo derp > w_wn_e.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %cesth% echo maybe & if %time:~3,2% geq %cestm% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi.mp3" & echo derp > w_wn_e.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi.mp3" & echo derp > w_wn_e.derp

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo.mp3" & del w_wn_e.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo.mp3" & del w_wn_e.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cesth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo.mp3" & del w_wn_e.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %cesth% echo maybe & if %time:~3,2% lss %cestm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo.mp3" & del w_wn_e.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% lss %cseth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cseth% echo maybe & if %time:~0,2% geq %nsth% echo maybe & if %time:~3,2% geq %nstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% leq %cseth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% lss %cseth% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi.mp3" & echo derp > w_wn_m.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cseth% echo maybe & if %time:~0,2% geq %nsth% echo maybe & if %time:~3,2% geq %nstm% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi.mp3" & echo derp > w_wn_m.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% leq %cseth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi.mp3" & echo derp > w_wn_m.derp

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cseth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo.mp3" & del w_wn_m.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %cseth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo.mp3" & del w_wn_m.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %nsth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo.mp3" & del w_wn_m.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %nsth% echo maybe & if %time:~3,2% lss %nstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo.mp3" & del w_wn_m.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi.mp3" & echo derp > w_wn_d.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi.mp3" & echo derp > w_wn_d.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi.mp3" & echo derp > w_wn_d.derp

if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo.mp3" & del w_wn_d.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% lss %cstm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo.mp3" & del w_wn_d.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo.mp3" & del w_wn_d.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo.mp3" & del w_wn_d.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi_nm.mp3" & echo derp > w_wn_n.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi_nm.mp3" & echo derp > w_wn_n.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm2% echo maybe & if not exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fi_nm.mp3" & echo derp > w_wn_n.derp


if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %ceth% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo_nm.mp3" & del w_wn_n.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %ceth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo_nm.mp3" & del w_wn_n.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %ceth% echo maybe & if %time:~3,2% lss %cetm% echo maybe & if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo_nm.mp3" & del w_wn_n.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %cesth% echo maybe & if %time:~3,2% geq %cestm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% geq %netm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi_nm.mp3" & echo derp > w_wn_e.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %cesth% echo maybe & if %time:~3,2% geq %cestm% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi_nm.mp3" & echo derp > w_wn_e.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cesth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fi_nm.mp3" & echo derp > w_wn_e.derp

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo_nm.mp3" & del w_wn_e.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo_nm.mp3" & del w_wn_e.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cesth% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo_nm.mp3" & del w_wn_e.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %cesth% echo maybe & if %time:~3,2% lss %cestm% echo maybe & if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo_nm.mp3" & del w_wn_e.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% lss %cseth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cseth% echo maybe & if %time:~0,2% geq %nsth% echo maybe & if %time:~3,2% geq %nstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% leq %cseth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% lss %cseth% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi_nm.mp3" & echo derp > w_wn_m.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %cseth% echo maybe & if %time:~0,2% geq %nsth% echo maybe & if %time:~3,2% geq %nstm% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi_nm.mp3" & echo derp > w_wn_m.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %nsth% echo maybe & if %time:~0,2% leq %cseth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if not exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fi_nm.mp3" & echo derp > w_wn_m.derp

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %cseth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo_nm.mp3" & del w_wn_m.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %cseth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo_nm.mp3" & del w_wn_m.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %nsth% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo_nm.mp3" & del w_wn_m.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %nsth% echo maybe & if %time:~3,2% lss %nstm% echo maybe & if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo_nm.mp3" & del w_wn_m.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi_nm.mp3" & echo derp > w_wn_d.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi_nm.mp3" & echo derp > w_wn_d.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fi_nm.mp3" & echo derp > w_wn_d.derp

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo_nm.mp3" & del w_wn_d.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% lss %cstm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo_nm.mp3" & del w_wn_d.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo_nm.mp3" & del w_wn_d.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo_nm.mp3" & del w_wn_d.derp /f /s /q
goto cont

:warfo
if exist w_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_night_fo.mp3" & del w_wn_n.derp /f /s /q
if exist w_wn_e.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_evening_fo.mp3" & del w_wn_e.derp /f /s /q
if exist w_wn_m.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_morning_fo.mp3" & del w_wn_m.derp /f /s /q
if exist w_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "warm_wn_day_fo.mp3" & del w_wn_d.derp /f /s /q
goto cont

:cold
set /a cseth=%csth% + 3
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi.mp3" & echo derp > c_wn_n.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi.mp3" & echo derp > c_wn_n.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi.mp3" & echo derp > c_wn_n.derp


if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %ceth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo.mp3" & del c_wn_n.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %ceth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo.mp3" & del c_wn_n.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %ceth% echo maybe & if %time:~3,2% lss %cetm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo.mp3" & del c_wn_n.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day.mp3" 30
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day.mp3" 30
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day.mp3" 30

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi.mp3" 30 & echo derp > c_wn_d.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi.mp3" 30 & echo derp > c_wn_d.derp
if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi.mp3" 30 & echo derp > c_wn_d.derp

if not exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo.mp3" & del c_wn_d.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% lss %cstm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo.mp3" 30 & del c_wn_d.derp /f /s /q

if not exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo.mp3" & del c_wn_d.derp /f /s /q
if not exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo.mp3" 30 & del c_wn_d.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %ceth% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi_nm.mp3" & echo derp > c_wn_n.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %ceth% echo maybe & if %time:~3,2% geq %cetm% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi_nm.mp3" & echo derp > c_wn_n.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% leq %cstm% echo maybe & if not exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fi_nm.mp3" & echo derp > c_wn_n.derp

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %ceth% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo_nm.mp3" & del c_wn_n.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %ceth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% gtr %cstm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo_nm.mp3" & del c_wn_n.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %ceth% echo maybe & if %time:~3,2% lss %cetm% echo maybe & if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo_nm.mp3" & del c_wn_n.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_nm.mp3"
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_nm.mp3"

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% lss %neth% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi_nm.mp3" & echo derp > c_wn_d.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %neth% echo maybe & if %time:~0,2% geq %csth% echo maybe & if %time:~3,2% geq %cstm% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi_nm.mp3" & echo derp > c_wn_d.derp
if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %csth% echo maybe & if %time:~0,2% leq %neth% echo maybe & if %time:~3,2% leq %netm% echo maybe & if not exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fi_nm.mp3" & echo derp > c_wn_d.derp

if exist nomufflewn.derp echo maybe & if %time:~0,2% lss %csth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo_nm.mp3" & del c_wn_d.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% leq %csth% echo maybe & if %time:~3,2% lss %cstm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo_nm.mp3" & del c_wn_d.derp /f /s /q

if exist nomufflewn.derp echo maybe & if %time:~0,2% gtr %neth% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo_nm.mp3" & del c_wn_d.derp /f /s /q
if exist nomufflewn.derp echo maybe & if %time:~0,2% geq %neth% echo maybe & if %time:~3,2% gtr %netm% echo maybe & if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo_nm.mp3" & del c_wn_d.derp /f /s /q
goto ed

:colfo
if exist c_wn_n.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_night_fo.mp3" & del c_wn_n.derp /f /s /q
if exist c_wn_d.derp start /min "" cmd.exe /c callaudio "window.exe" "cold_wn_day_fo.mp3" 30 & del c_wn_d.derp /f /s /q
goto ed

:breakwindow
start "" "windown.exe" "windowsmash.mp3"
timeout /t 6
set /a da = %date:~8,2% + 2
if %da% geq 29 set da=1
echo %da% > windowbroke.derp
echo %da% > "%USERPROFILE%\Desktop\ambience\windowbroke.derp"
goto bwe

:fixwindow
start /min "" cmd.exe /c callaudio "window.exe" "windowrepair.mp3"
del windowbroke.derp /f /s /q
del "%USERPROFILE%\Desktop\ambience\windowbroke.derp" /f /s /q
echo timeout /t 510 > windowfix.bat
echo del nomufflewn.derp /f /s /q >> windowfix.bat
echo start /min "" cmd.exe /c callaudio "clock.exe" "closewindow1.mp3" >> windowfix.bat
echo start /min "" cmd.exe /c callaudio "window.exe" "closewindow2.mp3" >> windowfix.bat
start /b "" "windowfix.bat"
goto fwe

:off
timeout /t 10
if exist on.derp goto loop
goto off



