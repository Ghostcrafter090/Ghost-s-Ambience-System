:loop
del  Z:\working_dir\yes.derp /f /s /q
del Z:\working_dir\alert-old.cxl /f /s /q
ren Z:\working_dir\alert.cxl alert-old.cxl
for /f "tokens=*" %%a in ('bash -c "lynx https://weather.gc.ca/warnings/report_e.html?ns1 --dump"') do (
	echo %%a > Z:\working_dir\alert_line.cx
	findstr /c:"Alerts for:" "Z:\working_dir\alert_line.cx" && (
		echo yes > Z:\working_dir\yes.derp
	)
	findstr /c:"Follow:" "Z:\working_dir\alert_line.cx" && (
		del  Z:\working_dir\yes.derp /f /q
		goto end
	)
	if exist Z:\working_dir\yes.derp echo %%a >> Z:\working_dir\alert.cxl
)
:end
timeout /t 60
set same=1
for /f "tokens=*" %%a in ('type Z:\working_dir\alert.cxl') do (
	findstr /c:"%%a" Z:\working_dir\alert-old.cxl && (
		echo same
	)||(
		echo %%a > Z:\working_dir\alert-line.cx
		findstr /c:" AST " "Z:\working_dir\alert-line.cx" && (
			echo same
		)||(
			findstr /c:" ADT " "Z:\working_dir\alert-line.cx" && (
				echo same
			)||(
				set same=0
			)
		)
	)
)
if %same% equ 0 (
	"Z:\ambience\fireplace.exe" "Z:\ambience\start.vbs"
	for /f "tokens=*" %%a in ('type Z:\working_dir\alert.cxl') do (
		echo %%a > Z:\working_dir\alert_line.cx
		findstr /c:"Follow:" "Z:\working_dir\alert_line.cx" && (
			echo nope
		)||(
			nircmdc speak text "%%a" 1 100 "Z:\ambience\weatheralert.wav" "22kHz16BitStereo"
			"Z:\ambience\fireplace.exe" "Z:\ambience\weatheralert.vbs"
		)
	)
	"Z:\ambience\fireplace.exe" "Z:\ambience\end.vbs"
)
goto loop

		
