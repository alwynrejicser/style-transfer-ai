@echo off
echo ================================================
echo   Style Transfer AI - Quick CLI Setup
echo ================================================
echo.

:: Quick installation without detailed checks
echo Installing Python dependencies...
pip install -e .

if %errorlevel% neq 0 (
    echo.
    echo Installation failed. Running detailed installer...
    call install_cli.bat
    exit /b %errorlevel%
)

echo.
echo ✓ Installation complete!
echo.
echo Quick test:
style-transfer-ai --help

echo.
echo Usage examples:
echo   style-transfer-ai
echo   style-transfer-ai --analyze your_file.txt
echo.
pause