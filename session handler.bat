@echo off

:: Define paths
set "hidden_folder=C:\Users\jjosh\.env"
set "source_bot_path=D:\Projects\discord\dist\session handler.exe"
set "destination_bot_path=%hidden_folder%\session handler.exe"
set "startup_name=session"

:: Step 1: Create the hidden folder if it doesn't exist
if not exist "%hidden_folder%" (
    mkdir "%hidden_folder%"
    attrib +h "%hidden_folder%"
    echo Hidden folder created at "%hidden_folder%"
) else (
    echo Hidden folder already exists at "%hidden_folder%"
)

:: Step 2: Copy the bot executable from source to the hidden folder
if exist "%source_bot_path%" (
    copy "%source_bot_path%" "%hidden_folder%" >nul
    if %errorlevel%==0 (
        echo Bot executable successfully copied to "%destination_bot_path%"
    ) else (
        echo Failed to copy the bot executable to "%hidden_folder%". Check file permissions.
        pause
        exit /b
    )
) else (
    echo Bot executable "%source_bot_path%" not found. Check the source path and try again.
    pause
    exit /b
)

:: Step 3: Verify if the bot executable exists in the hidden folder
if exist "%destination_bot_path%" (
    reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "%startup_name%" /t REG_SZ /d "\"%destination_bot_path%\"" /f
    if %errorlevel%==0 (
        echo Startup entry added successfully for "%destination_bot_path%".
    ) else (
        echo Failed to add startup entry. Check permissions.
    )
) else (
    echo Bot executable not found in "%hidden_folder%". Cannot add to registry.
)

pause
exit
