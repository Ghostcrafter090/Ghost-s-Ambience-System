:loop
if exist dsound.derp taskkill /f /im snpr.exe
if exist dsound.derp start /b "" snpr\snpr.exe
if not exist dsound.derp goto lloop1
timeout /t 194
goto loop

:lloop1
taskkill /f /im dsound.derp
goto lloop
:lloop
if exist dsound.derp goto loop
timeout /t 1
goto lloop