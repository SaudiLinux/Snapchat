@echo off
echo ====================================
echo Snapchat User Information Extractor
echo ====================================
echo.

:: Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed.
    echo Please install Python 3.6 or later from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%V in ('python --version 2^>^&1') do (
    echo Found Python version: %%V
)

:: Check if pip is installed
echo Checking pip installation...
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: pip is not installed or not in PATH.
    echo Please reinstall Python and make sure to check "Add Python to PATH".
    pause
    exit /b 1
)

:: Check internet connection
echo Checking internet connection...
ping -n 1 google.com >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    ping -n 1 cloudflare.com >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo Error: No internet connection detected.
        echo Please check your connection and try again.
        pause
        exit /b 1
    )
)

:: Install required packages
echo Installing required packages...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install required packages.
    echo Possible solutions:
    echo   1. Check your internet connection
    echo   2. Try running: pip install --upgrade pip
    echo   3. Try running this script as administrator
    pause
    exit /b 1
)

echo All required packages installed successfully.
echo.
echo Starting Snapchat User Information Extractor...
echo.

:: Run the tool
python snapchat_tool.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Tool execution failed. Please check the error messages above.
    pause
    exit /b 1
)

pause