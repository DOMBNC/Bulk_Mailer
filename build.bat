@echo off
REM =========================================================
REM  BulkMailer Pro — Windows Build Script
REM  Run this on a Windows machine with Python 3.10+
REM =========================================================

echo.
echo ===================================
echo  BulkMailer Pro — Build Script
echo ===================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Install Python 3.10+ from python.org
    pause
    exit /b 1
)

echo [1/4] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo [2/4] Cleaning previous build...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

echo.
echo [3/4] Building executable...
pyinstaller bulkmailer.spec --clean
if %errorlevel% neq 0 (
    echo ERROR: Build failed.
    pause
    exit /b 1
)

echo.
echo [4/4] Build complete!
echo.
echo Output: dist\BulkMailerPro\BulkMailerPro.exe
echo.
echo ===================================
echo  SUCCESS! Application built.
echo ===================================
echo.
pause
