@echo off
REM Batch script to automatically add Python user Scripts to PATH
REM This ensures style-transfer-ai CLI is globally accessible

echo.
echo ========================================
echo  Style Transfer AI - PATH Setup
echo ========================================
echo.

set "USER_SCRIPTS=%APPDATA%\Python\Python313\Scripts"

REM Check if directory exists
if not exist "%USER_SCRIPTS%" (
    echo ❌ Python user Scripts directory not found!
    echo    Expected: %USER_SCRIPTS%
    echo    Please install style-transfer-ai first:
    echo    pip install style-transfer-ai
    pause
    exit /b 1
)

REM Add to PATH using PowerShell
echo 🔧 Adding Python user Scripts to PATH...
powershell -Command "& {$userPath = [Environment]::GetEnvironmentVariable('PATH', 'User'); if ($userPath -notlike '*%USER_SCRIPTS%*') { [Environment]::SetEnvironmentVariable('PATH', $userPath + ';%USER_SCRIPTS%', 'User'); Write-Host '✅ Successfully added to PATH!' -ForegroundColor Green } else { Write-Host '✅ Already in PATH!' -ForegroundColor Green }}"

echo.
echo ✅ PATH setup complete!
echo.
echo 🔄 To use immediately in this session, run:
echo    refreshenv
echo    OR restart your terminal
echo.
echo 🚀 Then you can run from anywhere:
echo    style-transfer-ai
echo.
pause