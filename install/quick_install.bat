@echo off
echo ================================================
echo   Style Transfer AI - Quick CLI Setup
echo ================================================
echo.

:: Change to project root directory
cd ..
if not exist "src\" (
    echo ERROR: Cannot find project source directory
    echo Running detailed installer instead...
    cd install
    call install_cli.bat
    exit /b %errorlevel%
)

:: Create and activate virtual environment if needed
if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

:: Quick installation without detailed checks
echo Installing Python dependencies...
pip install -e .

if %errorlevel% neq 0 (
    echo.
    echo Installation failed. Running detailed installer...
    cd install
    call install_cli.bat
    exit /b %errorlevel%
)

:: Add to PATH if not already there
for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "UserPath=%%B"
if not defined UserPath set "UserPath="

echo %UserPath% | findstr /C:"%CD%\.venv\Scripts" >nul
if %errorlevel% neq 0 (
    echo Adding to user PATH...
    if defined UserPath (
        setx PATH "%UserPath%;%CD%\.venv\Scripts" >nul
    ) else (
        setx PATH "%CD%\.venv\Scripts" >nul
    )
    echo ✓ PATH updated
)

echo.
echo ✓ Installation complete!
echo.
echo Quick test:
.venv\Scripts\style-transfer-ai.exe --help >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: CLI test failed - try restarting command prompt
) else (
    echo ✓ CLI working!
)

echo.
echo Usage examples:
echo   style-transfer-ai
echo   style-transfer-ai --analyze your_file.txt
echo.
echo NOTE: If 'style-transfer-ai' command not found, restart your command prompt
echo.
pause