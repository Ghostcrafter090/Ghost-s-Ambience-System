goto wloop
:l
call cond.cmd
set tempe=%tempc%
set windguste=%windgust%
:loop
set hour=%time:~0,2%
set min=%time:~3,2%
if %hour% geq 10 echo maybe & if %hour% leq 12 goto wloop
call daytimes.cmd
set /a windp = %hour% - %cesth%
if %windp% leq 0 set windp=0
set /a windp2 = (((%windp% * (%min% - 30)) * (%windp% * (%min% - 30))) / 30) + 10
call cond.cmd
set /a windgust=(%windp2%/5) + %windgust%
rem echo set windgust=%windgust% >> cond.cmd
set hour=%time:~0,2%
set min=%time:~3,2%
call daytimes.cmd
set /a tempp = %hour% - %cesth%
if %tempp% leq 0 set tempp=0
set /a tempp2 = (((%tempp% * (%min%+20)) * (%tempp% * (%min%+20))) / 300)
if %tempp2% geq 40 set tempp2=40
call cond.cmd
set /a tempc=(%tempp2%) + %tempc%
set /a temp=(%tempp2%) + %tempc% + 273
rem echo set temp=%temp% >> cond.cmd
rem echo set tempc=%tempc% >> cond.cmd
timeout /t 20
goto loop

:wloop
for /f %%a in ('wmic path win32_localtime get dayofweek /format:list ^| findstr "="') do (
	set %%a
)
if %date:~8,2% equ 13 echo maybe & if %DayOfWeek% equ 5 echo maybe & if %time:~0,2% geq 13 goto l
if %date:~8,2% equ 31 echo maybe & if %date:~5,2% equ 10 echo maybe & if %time:~0,2% geq 13 goto l
timeout /t 1
goto wloop