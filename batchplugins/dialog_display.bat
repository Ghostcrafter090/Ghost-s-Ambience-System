@echo on
if not exist dialog.bat goto dialogcreate
:2
if not exist dialog_disp.bat goto dialogdispcreate
:3
goto loop

:dialogcreate
echo if not exist dialog_config.cmd @echo set dstate=on pipe1 dialog_config.cmd > dialog.bat
echo @echo off >> dialog.bat
echo :start >> dialog.bat
echo call dialog_config.cmd >> dialog.bat
echo @echo off >> dialog.bat
echo if %%dstate%%==on goto onderp >> dialog.bat
echo if %%dstate%%==off del on.derp /f /s /q >> dialog.bat
echo goto skip >> dialog.bat
echo :onderp >> dialog.bat
echo echo on pipe1 on.derp >> dialog.bat
echo :skip >> dialog.bat
echo color 21 >> dialog.bat
echo @echo off >> dialog.bat
echo echo DATA Ambience System (C) Phantom Bros 2019 >> dialog.bat
echo echo Note - this dialog is for switching the system on / off >> dialog.bat
echo echo (type help for ambience commands) >> dialog.bat
echo pause >> dialog.bat
echo start /b "" "dialog_disp.bat" >> dialog.bat
echo :loop >> dialog.bat
echo pause >> dialog.bat
echo cls >> dialog.bat
echo set /p com=command: >> dialog.bat
echo if %%com%%==help goto help >> dialog.bat
echo if %%com%%==on goto on >> dialog.bat
echo if %%com%%==off goto off >> dialog.bat
echo if %%com%%==restart goto restart >> dialog.bat
echo if %%com%%==setdefault goto setdefault >> dialog.bat
echo if %%com%%==bufferon goto bufferon >> dialog.bat
echo if %%com%%==bufferoff goto bufferoff >> dialog.bat
echo goto error >> dialog.bat
echo. >> dialog.bat
echo :help >> dialog.bat
echo echo -- HELP -- >> dialog.bat
echo echo on - turns system on with a volume of 22 >> dialog.bat
echo echo off - turns system off >> dialog.bat
echo echo restart - reinitializes system. >> dialog.bat
echo echo help - shows this dialog. >> dialog.bat
echo echo setdefault - allows you to set default settings. (IE: on/off state) >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :on >> dialog.bat
echo @echo System_On pipe1 on.derp >> dialog.bat
echo echo System Is now on. (note the off command will have to be ran to turn it off again.) >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :off >> dialog.bat
echo del on.derp /f /s /q >> dialog.bat
echo echo System Is now off. (note the on command will have to be ran to turn it on again.) >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :restart  >> dialog.bat
echo @echo pipe1 restart re.derp >> dialog.bat
echo set derp=194 >> dialog.bat
echo :loop2 >> dialog.bat
echo timeout /1 1 /nobreak >> dialog.bat
echo if exist re1.derp goto f1 >> dialog.bat
echo :f2 >> dialog.bat
echo set /a derp1=%%derp%% - 1 >> dialog.bat
echo set derp=%%derp1%% >> dialog.bat
echo if %%derp%%==0 goto re1 >> dialog.bat
echo goto loop2 >> dialog.bat
echo. >> dialog.bat
echo :f1 >> dialog.bat
echo if exist re2.derp goto re1 >> dialog.bat
echo goto f2 >> dialog.bat
echo. >> dialog.bat
echo :re1 >> dialog.bat
echo del /f /s /q re.derp >> dialog.bat
echo del /f /s /q thact.derp >> dialog.bat
echo del /f /s /q gwcont.derp >> dialog.bat
echo del /f /s /q wcont.derp >> dialog.bat
echo del /f /s /q fire.txt >> dialog.bat
echo start "" "%%USERPROFILE%%\Documents\Shortcut Stuff\Startup\ambience.vbs" >> dialog.bat
echo exit >> dialog.bat
echo. >> dialog.bat
echo. >> dialog.bat
echo :setdefault >> dialog.bat
echo set /p OP=Please select default on/off state (on / off): >> dialog.bat
echo if not %%OP%%==on goto off >> dialog.bat
echo @echo @echo off pipe1 dialog_config.cmd >> dialog.bat
echo @echo set dstate=on pipe1 dialog_config.cmd >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :off >> dialog.bat
echo if not %%OP%%==off goto error >> dialog.bat
echo @echo @echo off pipe1 dialog_config.cmd >> dialog.bat
echo @echo set dstate=off pipe1 dialog_config.cmd >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :error >> dialog.bat
echo echo ERROR - Invalid Option (type help for list of GAMB dialog commands) >> dialog.bat
echo timeout /t 1 /nobreak pipe1null >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :bufferon
echo @echo bufferon pipe1 buffer.derp >> dialog.bat
echo echo Buffer Active. >> dialog.bat
echo goto loop >> dialog.bat
echo. >> dialog.bat
echo :bufferoff >> dialog.bat
echo del buffer.derp /f /s /q >> dialog.bat
echo echo Buffer Deactivated. >> dialog.bat
echo goto loop >> dialog.bat
powershell -command "(Get-Content -path 'dialog.bat' -Raw) -replace 'pipe1','>' | Set-Content -Path 'dialog.bat'"
powershell -command "(Get-Content -path 'dialog.bat' -Raw) -replace 'pipe2','>>' | Set-Content -Path 'dialog.bat'"
goto 2

:dialogdispcreate
echo @echo off > dialog_disp.bat
echo :loop >> dialog_disp.bat
echo set thunder=pipe3 thunder.list >> dialog_disp.bat
echo cls >> dialog_disp.bat
echo echo --- Active Weather Sounds --- >> dialog_disp.bat
echo echo ----------------------------- >> dialog_disp.bat
echo if exist on.derp echo Clock System Active >> dialog_disp.bat
echo echo Thunder Storm Chance: %%thunder%%%%%% >> dialog_disp.bat
echo type sounds.list >> dialog_disp.bat
echo echo ----------------------------- >> dialog_disp.bat
echo echo Note: type help for list of commands (command box is bellow, just type and click enter) >> dialog_disp.bat
echo timeout /t 15 /nobreak pipe1null >> dialog_disp.bat
echo goto loop >> dialog_disp.bat
powershell -command "(Get-Content -path 'dialog_disp.bat' -Raw) -replace 'pipe1','>' | Set-Content -Path 'dialog_disp.bat'"
powershell -command "(Get-Content -path 'dialog_disp.bat' -Raw) -replace 'pipe3','<' | Set-Content -Path 'dialog_disp.bat'"
goto 3

:loop
start /max /wait "" cmd.exe /c dialog.bat
goto loop