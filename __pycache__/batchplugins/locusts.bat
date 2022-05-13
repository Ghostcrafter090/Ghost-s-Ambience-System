set tempc=0
:loop
set month=%date:~5,2%
if %month:~0,1% equ 0 set month=%month:~1,1%
set dom=%date:~8,2%
if %dom:~0,1% equ 0 set dom=%dom:~1,1%
set /a day = (%month% * 30) + %dom%
call cond.cmd

// hot late summer
echo 1 > lonum.cx
set /a num2 = %tempc% - 15
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a pera = %per% / (((((300 - %day%) * (300 - %day%) * (300 - %day%) * (300 - %day%)) + 1) / 4100625) + 1)
echo %pera% > locustaindex.cx

// hot mid summer humid
echo 1 > lonum.cx
set /a num2 = %tempc% - 16
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perb = (%per% / (((((235 - %day%) * (235 - %day%) * (235 - %day%) * (235 - %day%)) + 1) / 4100625) + 1)) / (101 - %humidity%)
echo %perb% > locustbindex.cx

// warm mid summer humid
echo 1 > lonum.cx
set /a num2 = %tempc% - 12
if %tempc% geq 19 set /a num2 = %num2% - ((%tempc% - 18) * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perc = (%per% / (((((250 - %day%) * (250 - %day%) * (250 - %day%) * (250 - %day%)) + 1) / 4100625) + 1)) / (101 - %humidity%)
echo %perc% > locustcindex.cx

// wide range early fall
echo 1 > lonum.cx
set /a num2 = %tempc% - 3
if %tempc% geq 20 set /a num2 = %num2% - ((%tempc% - 19) * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 3
set /a perd = %per% / (((((320 - %day%) * (320 - %day%) * (320 - %day%) * (320 - %day%)) + 1) / 4100625) + 1)
echo %perd% > locustdindex.cx

// low range warm mid summer
echo 1 > lonum.cx
set /a num2 = %tempc% - 15
if %tempc% geq 21 set /a num2 = %num2% - ((%tempc% - 20) * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a pere = %per% / (((((240 - %day%) * (240 - %day%) * (240 - %day%) * (240 - %day%)) + 1) / 4100625) + 1)
echo %pere% > locusteindex.cx

// hot afternoon mid summer
echo 1 > lonum.cx
set /a num2 = %tempc% - 16 - (16 - %time:~0,2%)
if %time:~0,2% geq 16 set /a num2 = %num2% - (%time:~0,2% * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perf = %per% / (((((230 - %day%) * (230 - %day%) * (230 - %day%) * (230 - %day%)) + 1) / 4100625) + 1)
echo %perf% > locustfindex.cx

// low range warm night humid
echo 1 > lonum.cx
set /a num2 = %tempc% - 16 - (23 - %time:~0,2%)
if %tempc% leq 20 set /a num2 = %num2% - ((%tempc% - 19) * 2)
if %time:~0,2% leq 6 set /a num2 = %num2% - (%time:~0,2% * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perg = (%per% / (((((260 - %day%) * (260 - %day%) * (260 - %day%) * (260 - %day%)) + 1) / 4100625) + 1)) / (101 - %humidity%)
echo %perg% > locustgindex.cx

// all day dry evenings late summer
echo 1 > lonum.cx
set /a num2 = %tempc% - 16 - (23 - %time:~0,2%)
if %tempc% leq 20 set /a num2 = %num2% - ((%tempc% - 19) * 2)
if %time:~0,2% leq 18 set /a num2 = %num2% - ((19 - %time:~0,2%) * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perh = (%per% / (((((260 - %day%) * (260 - %day%) * (280 - %day%) * (280 - %day%)) + 1) / 4100625) + 1)) / (50 - humidity)
echo %perh% > locusthindex.cx

// low range warm night
echo 1 > lonum.cx
set /a num2 = %tempc% - 16 - (23 - %time:~0,2%)
if %tempc% leq 20 set /a num2 = %num2% - ((%tempc% - 19) * 2)
if %time:~0,2% leq 6 set /a num2 = %num2% - (%time:~0,2% * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a peri = %per% / (((((300 - %day%) * (260 - %day%) * (260 - %day%) * (260 - %day%)) + 1) / 4100625) + 1)
echo %peri% > locustiindex.cx

// cool day spring
echo 1 > lonum.cx
set /a num2 = %tempc% - 8
if %tempc% leq 17 set /a num2 = %num2% - ((%tempc% - 16) * 2)
if %num2% leq 0 set num2 = 1
echo %num2% > lonum2.cx
for /l %%a in (1,1,%num2%) do (
        for /f "tokens=1" %%b in ('type lonum.cx') do (
                start /wait /b "" "cmd.exe" /c set /a num = %%b * 2 > lonum.cx
        )
)
set /p per=< lonum.cx
set /a per = %per% * 5
set /a perj = %per% / (((((190 - %day%) * (190 - %day%) * (190 - %day%) * (190 - %day%)) + 1) / 4100625) + 1)
echo %perj% > locustjindex.cx

for /f "tokens=*" %%a in ('powershell -command %tempc% / 20') do (
	set speed=%%a
)

if "$%speed:~0,1%"=="$-" set speed=0.01

rem for /f "tokens=*" %%a in ('type locust_effect_list.cxl') do (
rem 	pyexec -executescript "file = open(\"%%a\", \"r\"); f = file.read(); f = f.replace(\"Sound.Settings.Rate = \", \"Sound.Settings.Rate = %speed% \' \"); file.close(); file = open(\"%%a\", \"w\"); file.write(f); file.close(); "
rem )

set hour=%time:~0,2%
if "$%hour:~0,1% "=="$ " set hour=%hour:~1,1%

call daytimes.cmd

if exist nomufflewn.derp (
	start /min "" stopsound  slender_me_ka_m
) else (
	start /min "" stopsound  slender_me_ka
)
if exist nomufflewn.derp (
	start /min "" stopsound  spahgnum_gr_cr_m
) else (
	start /min "" stopsound  spahgnum_gr_cr
)
if exist nomufflewn.derp (
	start /min "" stopsound  striped_gr_cr_m
) else (
	start /min "" stopsound  striped_gr_cr
)
if exist nomufflewn.derp (
	start /min "" stopsound  carolina_gr_cr_m
) else (
	start /min "" stopsound  carolina_gr_cr
)
if exist nomufflewn.derp (
	start /min "" stopsound  allards_gr_cr_m
) else (
	start /min "" stopsound  allards_gr_cr
)

if %RANDOM% leq %perf% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "slender_me_ka.mp3" 50 0 %speed%
if %RANDOM% leq %perf% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "slender_me_ka_m.mp3" 50 0 %speed%
if %RANDOM% leq %perb% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "spahgnum_gr_cr.mp3" 50 0 %speed%
if %RANDOM% leq %perb% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "spahgnum_gr_cr_m.mp3" 50 0 %speed%
if %RANDOM% leq %perc% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "striped_gr_cr.mp3" 50 0 %speed%
if %RANDOM% leq %perc% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "striped_gr_cr_m.mp3" 50 0 %speed%
if %RANDOM% leq %perd% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "carolina_gr_cr.mp3" 50 0 %speed%
if %RANDOM% leq %perd% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "carolina_gr_cr_m.mp3" 50 0 %speed%
if %RANDOM% leq %pere% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "allards_gr_cr.mp3" 50 0 %speed%
if %RANDOM% leq %pere% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "allards_gr_cr_m.mp3" 50 0 %speed%

if "$%perg%"=="$" set perg=0

if exist nomufflewn.derp (
	start /min "" stopsound  broadwinged_bu_ka_d_m
) else (
	start /min "" stopsound  broadwinged_bu_ka_d
)
if exist nomufflewn.derp (
	start /min "" stopsound  broadwinged_bu_ka_n_m
) else (
	start /min "" stopsound  broadwinged_bu_ka_n
)

if %RANDOM% leq %perg% echo maybe & (
	if exist nomufflewn.derp (
		if %hour% geq %nsth% (
			if %hour% leq %neth% (
				start /min "" cmd.exe /c callaudio windown.exe "broadwinged_bu_ka_d.mp3" 50 0 %speed%
			)
		)
	)
)
if %RANDOM% leq %perg% echo maybe & (
	if not exist nomufflewn.derp (
        if %hour% geq %nsth% (
            if %hour% leq %neth% (
                start /min "" cmd.exe /c callaudio window.exe "broadwinged_bu_ka_d_m.mp3" 50 0 %speed%
            )
		)
    )
)

if %RANDOM% leq %perg% echo maybe & (
	if exist nomufflewn.derp (
		if %hour% geq %ceth% (
			if %hour% leq %csth% (
				start /min "" cmd.exe /c callaudio windown.exe "broadwinged_bu_ka_n.mp3" 50 0 %speed%
			)
		)
	)
)
if %RANDOM% leq %perg% echo maybe & (
	if not exist nomufflewn.derp (
        if %hour% geq %ceth% (
            if %hour% leq %csth% (
                start /min "" cmd.exe /c callaudio window.exe "broadwinged_bu_ka_n_m.mp3" 50 0 %speed%
			)
        )
    )
)
if exist nomufflewn.derp (
	start /min "" stopsound curvetail_bu_ka_m
) else (
	start /min "" stopsound curvetail_bu_ka
)
if exist nomufflewn.derp (
	start /min "" stopsound forktail_bu_ka_m
) else (
	start /min "" stopsound forktail_bu_ka
)
if exist nomufflewn.derp (
	start /min "" stopsound marsh_me_gr_m
) else (
	start /min "" stopsound marsh_me_gr
)
if exist nomufflewn.derp (
	start /min "" stopsound says_ci_m
) else (
	start /min "" stopsound says_ci
)
if %RANDOM% leq %perh% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "curvetail_bu_ka.mp3" 50 0 %speed%
if %RANDOM% leq %perh% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "curvetail_bu_ka_m.mp3" 50 0 %speed%
if %RANDOM% leq %peri% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "forktail_bu_ka.mp3" 50 0 %speed%
if %RANDOM% leq %peri% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "forktail_bu_ka_m.mp3" 50 0 %speed%
if %RANDOM% leq %pera% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "marsh_me_gr.mp3" 50 0 %speed%
if %RANDOM% leq %pera% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "marsh_me_gr_m.mp3" 50 0 %speed%
if %RANDOM% leq %perj% echo maybe & if exist nomufflewn.derp start /min "" cmd.exe /c callaudio windown.exe "says_ci.mp3" 50 0 %speed%
if %RANDOM% leq %perj% echo maybe & if not exist nomufflewn.derp start /min "" cmd.exe /c callaudio window.exe "says_ci_m.mp3" 50 0 %speed%

:dsk
wait wait 30
goto loop