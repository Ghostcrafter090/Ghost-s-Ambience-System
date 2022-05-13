set temp=281
set tempc=9
set windspeed=0
set windgust=0
set pressure=1001
set humidity=50
set weather=clear
:loop
@echo off
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
if not exist on.derp goto null
if %temp% leq 271 @echo on & goto yes
if "$%weather%"=="$snow " echo maybe & if %temp% leq 276 @echo on & goto yes2
nircmdc wait 1000
goto loop

:yes
set /a int = (%temp% - 200)
set /a max = %int% * 10
set /a min = (%max% / 3)
:rloop
set derp=%RANDOM%
set /a rand1=(%derp% / (32768 / %max%))
set int2=%rand1%
if %int% geq 68 set /a int2 = %rand1% * (%int% - 67) * (%int% - 67)
set rand1=%int2%
if %rand1% leq %min% goto rloop
set rand=%rand1%
timeout /t %rand%
:rep
set derp=%RANDOM%
set /a rand2=(%derp% / (32768 / 5))
if %rand2% leq 0 start /b /wait "" "windown.exe" "treecr1.vbs"
if %rand2% leq 0 goto rep
start /b /wait "" "windown.exe" "treeex%rand2%.vbs"
goto loop

:null
if exist on.derp goto loop
timeout /t 1
goto null

:yes2
set /a int = (%temp% - 204)
set /a max = %int% * 10
set /a min = (%max% / 3)
:rloop2
set derp=%RANDOM%
set /a rand1=(%derp% / (32768 / %max%))
set int2=%rand1%
if %int% geq 68 set /a int2 = %rand1% * (%int% - 67) * (%int% - 67)
set rand1=%int2%
if %rand1% leq %min% goto rloop2
set rand=%rand1%
timeout /t %rand%
:rep2
set derp=%RANDOM%
set /a rand2=(%derp% / (32768 / 3))
if %rand2% leq 0 start /b /wait "" "windown.exe" "treecr1.vbs"
if %rand2% leq 0 goto rep2
start /b /wait "" "treeex%rand2%.vbs"
goto loop

