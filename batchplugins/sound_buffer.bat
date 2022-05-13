:loop
if not exist buffer.derp goto skip
rem start "" "window.exe" "sound_buffer.vbs"
start "" "window.exe" "sound_buffer2.vbs"
:skip
nircmdc wait 92000
goto loop