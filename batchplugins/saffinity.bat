:loop
Powershell -command "ForEach($PROCESS in GET-PROCESS window) { $PROCESS.ProcessorAffinity=65534}"
Powershell -command "ForEach($PROCESS in GET-PROCESS clock) { $PROCESS.ProcessorAffinity=65534}"
Powershell -command "ForEach($PROCESS in GET-PROCESS fireplace) { $PROCESS.ProcessorAffinity=65534}"
goto loop