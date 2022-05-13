:loop
if not exist swyh.derp goto stop
nircmdc wait 1009
start /b /wait /affinity 7FBF "" "swyh\SWYH.exe"
goto loop

:stop
timeout /t 1
if exist swyh.derp goto loop
goto stop