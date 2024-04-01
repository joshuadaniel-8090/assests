@echo off

REM Check if script is already running with administrative privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run_as_admin
)

REM If not running with admin privileges, re-run the script with elevated privileges
powershell -Command "Start-Process '%comspec%' -Verb RunAs -ArgumentList '/c %~nx0 %*'"
exit /b

:run_as_admin

REM Install OpenSSH feature
echo Installing OpenSSH feature...
powershell -Command "Add-WindowsCapability -Online -Name OpenSSH.Server"

REM Start SSH server service
echo Starting SSH server service...
net start sshd

REM Enable SSH server service to start automatically on boot
echo Enabling SSH server service to start automatically on boot...
sc config sshd start=auto

REM Display completion message
echo SSH setup completed successfully.
