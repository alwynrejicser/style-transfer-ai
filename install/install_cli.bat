@echo off
echo ================================================
echo   Style Transfer AI - CLI Installation Script
echo ================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python found: 
python --version

:: Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not available
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo ✓ pip found: 
pip --version
echo.

:: Upgrade pip to latest version
echo Upgrading pip to latest version...
python -m pip install --upgrade pip
echo.

:: Install dependencies from requirements.txt
echo Installing Python dependencies...
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo WARNING: Some dependencies failed to install
        echo You may need to install them manually:
        echo   pip install requests openai google-generativeai firebase-admin
        echo.
    ) else (
        echo ✓ Dependencies installed successfully
    )
) else (
    echo Installing core dependencies manually...
    pip install requests openai google-generativeai firebase-admin
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)
echo.

:: Install the CLI tool
echo Installing Style Transfer AI CLI...
pip install -e .
if %errorlevel% neq 0 (
    echo ERROR: Failed to install CLI tool
    echo Try running this script as Administrator
    pause
    exit /b 1
)

echo ✓ CLI tool installed successfully!
echo.

:: Test the installation
echo Testing CLI installation...
style-transfer-ai --help >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: CLI command not found in PATH
    echo You may need to add Python Scripts directory to your PATH
    echo.
    echo To find your Python Scripts directory:
    python -c "import site; print(site.getusersitepackages().replace('site-packages', 'Scripts'))"
    echo.
) else (
    echo ✓ CLI command working correctly!
    echo.
    echo You can now use: style-transfer-ai
)

:: Check for Ollama
echo Checking for Ollama installation...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo NOTICE: Ollama not found
    echo For local AI processing, install Ollama from:
    echo https://ollama.ai/download
    echo.
    echo After installing Ollama, run these commands:
    echo   ollama pull gpt-oss:20b
    echo   ollama pull gemma3:1b
    echo   ollama serve
    echo.
) else (
    echo ✓ Ollama found: 
    ollama --version
    echo.
    echo Checking for required AI models...
    
    ollama list | findstr "gpt-oss:20b" >nul 2>&1
    if %errorlevel% neq 0 (
        echo - gpt-oss:20b model not found
        echo   Run: ollama pull gpt-oss:20b
    ) else (
        echo ✓ gpt-oss:20b model available
    )
    
    ollama list | findstr "gemma3:1b" >nul 2>&1
    if %errorlevel% neq 0 (
        echo - gemma3:1b model not found
        echo   Run: ollama pull gemma3:1b
    ) else (
        echo ✓ gemma3:1b model available
    )
)

echo.
echo ================================================
echo            Installation Complete!
echo ================================================
echo.
echo Usage:
echo   style-transfer-ai                    (Interactive mode)
echo   style-transfer-ai --help             (Show all options)
echo   style-transfer-ai --analyze file.txt (Analyze a file)
echo.
echo Sample files provided:
if exist about_my_pet.txt echo   - about_my_pet.txt
if exist about_my_pet_1.txt echo   - about_my_pet_1.txt
echo.
echo Test the installation:
echo   style-transfer-ai --analyze about_my_pet.txt
echo.
echo For API keys setup, see README.md
echo.
pause