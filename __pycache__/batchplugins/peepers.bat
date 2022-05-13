:loop
if not exist on.derp goto off
set month=%date:~5,2%
set day=%date:~8,2%
call cond.cmd
if %month:~0,1% equ 0 set month=%month:~1,1%
if %day:~0,1% equ 0 set day=%day:~1,1%
set peepersmax=-1
goto date

:date
if %month% equ 4 (
	set peepersmax=1
	if %day% leq 15 (
		set peepersmax=0
	)
)
if %month% equ 5 (
	set peepersmax=3
	if %day% leq 15 (
		set peepersmax=2
	)
)
echo %peepersmax%
if %month% equ 6 (
	set peepersmax=4
)
if %month% equ 7 (
	set peepersmax=3
)
if %month% equ 8 (
	set peepersmax=2
)
if %month% equ 9 (
	set peepersmax=1
)
if %month% equ 10 (
	set peepersmax=0
)
set /a tempsub = 281 - %temp%
set /a windsub = %windgust% - 23
set /a humiditysub = -1 * ((((%humidity% * 10) - 650) / 100) - 1)
if %tempsub% leq 0 set tempsub=0
if %tempsub% geq 5 set tempsub=5
if %windsub% leq 0 set windsub=0
if %windsub% geq 5 set windsub=5
if %humiditysub% leq 0 set humiditysub=0
if %humiditysub% geq 5 set humiditysub=5
set rainsub=0
if "$%weather%"=="$lightrain" set rainsub=1
if "$%weather%"=="$rain" set rainsub=2
if "$%weather%"=="$snow" set rainsub=-2
set /a peepersmax = %peepersmax% - %tempsub%
set /a peepersmax = %peepersmax% - %windsub%
set /a peepersmax = %peepersmax% - %humiditysub%
set /a peepersmax = %peepersmax% - %snowsub%
goto time

:time
call daytimes.cmd
set /a pep0h = %cesth% - 2
set /a pep0m = %cestm% + 30
if %pep0m% geq 60 (
	set /a pep0h = %pep0h% + 1
	set /a pep0m = %pep0m% - 60
)
set /a pep1h = %cesth%
set /a pep1m = %cestm%
if %pep1m% geq 60 (
	set /a pep1h = %pep1h% + 1
	set /a pep1m = %pep1m% - 60
)
set /a cetl = (((%ceth% - %cesth%) * 60) + (%cetm% - %cestm%)) / 2
set /a pep2h = %cesth%
set /a pep2m = %cestm% + %cetl%
if %pep2m% geq 60 (
	set /a pep2h = %pep2h% + 1
	set /a pep2m = %pep2m% - 60
)
set /a pep3h = %ceth%
set /a pep3m = %cetm%
if %pep3m% geq 60 (
	set /a pep3h = %pep3h% + 1
	set /a pep3m = %pep3m% - 60
)
set /a netl = (((%ceth% - %neth%) * 60) + (%cetm% - %netm%)) / 2
set /a pep4h = %ceth%
set /a pep4m = %cetm% + %netl%
if %pep4m% geq 60 (
	set /a pep4h = %pep4h% + 1
	set /a pep4m = %pep4m% - 60
)
set /a psp0h = %csth% + 2
set /a psp0m = %cstm% - 30
if %psp0m% leq -1 (
	set /a psp0h = %psp0h% - 1
	set /a psp0m = %psp0m% + 60
)
set /a psp1h = %csth%
set /a psp1m = %cstm%
if %psp1m% leq -1 (
	set /a psp1h = %psp1h% - 1
	set /a psp1m = %psp1m% + 60
)
set /a cstl = (((%csth% - %nsth%) * 60) + (%cstm% - %nstm%)) / 2
set /a psp2h = %csth%
set /a psp2m = %cstm% + %cetl%
if %psp2m% leq -1 (
	set /a psp2h = %psp2h% - 1
	set /a psp2m = %psp2m% + 60
)
set /a psp3h = %nsth%
set /a psp3m = %nstm%
if %psp3m% leq -1 (
	set /a psp3h = %psp3h% - 1
	set /a psp3m = %psp3m% + 60
)
set /a nstl = (((%nsth% - %csth%) * 60) + (%nstm% - %cstm%)) / 2
set /a psp4h = %csth%
set /a psp4m = %cstm% + %nstl%
if %psp4m% leq -1 (
	set /a psp4h = %psp4h% - 1
	set /a psp4m = %psp4m% + 60
)
goto play

:play
set hour=%time:~0,2%
set min=%time:~3,2%
if "$%hour:~0,1%"=="$ " set hour=%hour:~1,1%
if %min:~0,1% equ 0 set min=%min:~1,1%
set pep0c=0
set pep1c=0
set pep2c=0
set pep3c=0
set pep4c=0
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_0
) else (
	start /min "" stopsound  peepers_0
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_1
) else (
	start /min "" stopsound  peepers_1
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_2
) else (
	start /min "" stopsound  peepers_2
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_3
) else (
	start /min "" stopsound  peepers_3
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_4
) else (
	start /min "" stopsound  peepers_4
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_0_fi
) else (
	start /min "" stopsound  peepers_0_fi
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_1_fi
) else (
	start /min "" stopsound  peepers_1_fi
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_2_fi
) else (
	start /min "" stopsound  peepers_2_fi
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_3_fi
) else (
	start /min "" stopsound  peepers_3_fi
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_4_fi
) else (
	start /min "" stopsound  peepers_4_fi
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_0_fo
) else (
	start /min "" stopsound  peepers_0_fo
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_1_fo
) else (
	start /min "" stopsound  peepers_1_fo
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_2_fo
) else (
	start /min "" stopsound  peepers_2_fo
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_3_fo
) else (
	start /min "" stopsound  peepers_3_fo
)
if exist nomufflewn.derp (
	start /min "" stopsound  m_peepers_4_fo
) else (
	start /min "" stopsound  peepers_4_fo
)
if %hour% equ %pep0h% (
	if %min% geq %pep0m% (
		if %peepersmax% geq 0 (
			set pep0c=1
			if not exist peepers_0.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0_fi.mp3 25
				)
				echo derp > peepers_0.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0.mp3 25
				)
			)
		)
	)
)
if %hour% gtr %pep0h% (
	if %peepersmax% geq 0 (
		if not exist peepers_1.derp (
			set pep0c=1
			if not exist peepers_0.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0_fi.mp3 25
				)
				echo derp > peepers_0.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0.mp3 25
				)
			)
		)
	)
)
if %hour% lss %psp0h% (
	if %peepersmax% geq 0 (
		if not exist peepers_1.derp (
			set pep0c=1
			if not exist peepers_0.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0_fi.mp3 25
				)
				echo derp > peepers_0.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0.mp3 25
				)
			)
		)
	)
)
if %hour% equ %psp0h% (
	if %min% leq %psp0m% (
		if %peepersmax% geq 0 (
			set pep0c=1
			if not exist peepers_0.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0_fi.mp3 25
				)
				echo derp > peepers_0.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_0.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_0.mp3 25
				)
			)
		)
	)
)
if %pep0c% equ 0 (
	if exist peepers_0.derp (
		del peepers_0.derp /f /s /q
		if exist nomufflewn.derp (
			start /min "" cmd.exe /c callaudio windown.exe peepers_0_fo.mp3 25
		) else (
			start /min "" cmd.exe /c callaudio window.exe m_peepers_0_fo.mp3 25
		)
	)
)
if %hour% equ %pep1h% (
	if %min% geq %pep1m% (
		if %peepersmax% geq 1 (
			set pep1c=1
			if not exist peepers_1.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1_fi.mp3 25
				)
				echo derp > peepers_1.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1.mp3 25
				)
			)
		)
	)
)
if %hour% gtr %pep1h% (
	if %peepersmax% geq 1 (
		if not exist peepers_2.derp (
			set pep1c=1
			if not exist peepers_1.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1_fi.mp3 25
				)
				echo derp > peepers_1.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1.mp3 25
				)
			)
		)
	)
)
if %hour% lss %psp1h% (
	if %peepersmax% geq 1 (
		if not exist peepers_2.derp (
			set pep1c=1
			if not exist peepers_1.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1_fi.mp3 25
				)
				echo derp > peepers_1.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1.mp3 25
				)
			)
		)
	)
)
if %hour% equ %psp1h% (
	if %min% leq %psp1m% (
		if %peepersmax% geq 1 (
			set pep1c=1
			if not exist peepers_1.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1_fi.mp3 25
				)
				echo derp > peepers_1.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_1.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_1.mp3 25
				)
			)
		)
	)
)
if %pep1c% equ 0 (
	if exist peepers_1.derp (
		del peepers_1.derp /f /s /q
		if exist nomufflewn.derp (
			start /min "" cmd.exe /c callaudio windown.exe peepers_1_fo.mp3 25
		) else (
			start /min "" cmd.exe /c callaudio window.exe m_peepers_1_fo.mp3 25
		)
	)
)
if %hour% equ %pep2h% (
	if %min% geq %pep2m% (
		if %peepersmax% geq 2 (
			set pep2c=1
			if not exist peepers_2.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2_fi.mp3 25
				)
				echo derp > peepers_2.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2.mp3 25
				)
			)
		)
	)
)
if %hour% gtr %pep2h% (
	if %peepersmax% geq 2 (
		if not exist peepers_3.derp (
			set pep2c=1
			if not exist peepers_2.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2_fi.mp3 25
				)
				echo derp > peepers_2.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2.mp3 25
				)
			)
		)
	)
)
if %hour% lss %psp2h% (
	if %peepersmax% geq 2 (
		if not exist peepers_3.derp (
			set pep2c=1
			if not exist peepers_2.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2_fi.mp3 25
				)
				echo derp > peepers_2.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2.mp3 25
				)
			)
		)
	)
)
if %hour% equ %psp2h% (
	if %min% leq %psp2m% (
		if %peepersmax% geq 2 (
			set pep2c=1
			if not exist peepers_2.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2_fi.mp3 25
				)
				echo derp > peepers_2.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_2.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_2.mp3 25
				)
			)
		)
	)
)
if %pep2c% equ 0 (
	if exist peepers_2.derp (
		del peepers_2.derp /f /s /q
		if exist nomufflewn.derp (
			start /min "" cmd.exe /c callaudio windown.exe peepers_2_fo.mp3 25
		) else (
			start /min "" cmd.exe /c callaudio window.exe m_peepers_2_fo.mp3 25
		)
	)
)
if %hour% equ %pep3h% (
	if %min% geq %pep3m% (
		if %peepersmax% geq 3 (
			set pep3c=1
			if not exist peepers_3.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3_fi.mp3 25
				)
				echo derp > peepers_3.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3.mp3 25
				)
			)
		)
	)
)
if %hour% gtr %pep3h% (
	if %peepersmax% geq 3 (
		if not exist peepers_4.derp (
			set pep3c=1
			if not exist peepers_3.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3_fi.mp3 25
				)
				echo derp > peepers_3.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3.mp3 25
				)
			)
		)
	)
)
if %hour% lss %psp3h% (
	if %peepersmax% geq 3 (
		if not exist peepers_4.derp (
			set pep3c=1
			if not exist peepers_3.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3_fi.mp3 25
				)
				echo derp > peepers_3.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3.mp3 25
				)
			)
		)
	)
)
if %hour% equ %psp3h% (
	if %min% leq %psp3m% (
		if %peepersmax% geq 3 (
			set pep3c=1
			if not exist peepers_3.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3_fi.mp3 25
				)
				echo derp > peepers_3.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_3.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_3.mp3 25
				)
			)
		)
	)
)
if %pep3c% equ 0 (
	if exist peepers_3.derp (
		del peepers_3.derp /f /s /q
		if exist nomufflewn.derp (
			start /min "" cmd.exe /c callaudio windown.exe peepers_3_fo.mp3 25
		) else (
			start /min "" cmd.exe /c callaudio window.exe m_peepers_3_fo.mp3 25
		)
	)
)
if %hour% equ %pep4h% (
	if %min% geq %pep4m% (
		if %peepersmax% geq 4 (
			set pep4c=1
			if not exist peepers_4.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_4_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_4_fi.mp3 25
				)
				echo derp > peepers_4.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_4.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_4.mp3 25
				)
			)
		)
	)
)
if %hour% gtr %pep4h% (
	if %peepersmax% geq 4 (
		set pep4c=1
		if not exist peepers_4.derp (
			if exist nomufflewn.derp (
				start /min "" cmd.exe /c callaudio windown.exe peepers_4_fi.mp3 25
			) else (
				start /min "" cmd.exe /c callaudio window.exe m_peepers_4_fi.mp3 25
			)
			echo derp > peepers_4.derp
		) else (
			if exist nomufflewn.derp (
				start /min "" cmd.exe /c callaudio windown.exe peepers_4.mp3 25
			) else (
				start /min "" cmd.exe /c callaudio window.exe m_peepers_4.mp3 25
			)
		)
	)
)
if %hour% lss %psp4h% (
	if %peepersmax% geq 4 (
		set pep4c=1
		if not exist peepers_4.derp (
			if exist nomufflewn.derp (
				start /min "" cmd.exe /c callaudio windown.exe peepers_4_fi.mp3 25
			) else (
				start /min "" cmd.exe /c callaudio window.exe m_peepers_4_fi.mp3 25
			)
			echo derp > peepers_4.derp
		) else (
			if exist nomufflewn.derp (
				start /min "" cmd.exe /c callaudio windown.exe peepers_4.mp3 25
			) else (
				start /min "" cmd.exe /c callaudio window.exe m_peepers_4.mp3 25
			)
		)
	)
)
if %hour% equ %psp4h% (
	if %min% leq %psp4m% (
		if %peepersmax% geq 4 (
			set pep4c=1
			if not exist peepers_4.derp (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_4_fi.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_4_fi.mp3 25
				)
				echo derp > peepers_4.derp
			) else (
				if exist nomufflewn.derp (
					start /min "" cmd.exe /c callaudio windown.exe peepers_4.mp3 25
				) else (
					start /min "" cmd.exe /c callaudio window.exe m_peepers_4.mp3 25
				)
			)
		)
	)
)
if %pep4c% equ 0 (
	if exist peepers_4.derp (
		del peepers_4.derp /f /s /q
		if exist nomufflewn.derp (
			start /min "" cmd.exe /c callaudio windown.exe peepers_4_fo.mp3 25
		) else (
			start /min "" cmd.exe /c callaudio window.exe m_peepers_4_fo.mp3 25
		)
	)
)
goto wait

:wait
wait wait 480000
goto loop

:off
if exists on.derp goto loop
timeout /t 10
goto off