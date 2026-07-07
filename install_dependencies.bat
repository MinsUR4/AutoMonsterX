@echo off
echo Installing AutoMonsterX dependencies...
echo.

echo Checking Python version...
python -c "import sys; v=sys.version_info; print(f'{v.major}.{v.minor}.{v.micro}'); sys.exit(0 if (v.major==3 and 9<=v.minor<=12) else 1)"
if errorlevel 1 (
    echo.
    echo WARNING: This project is verified on Python 3.9-3.12.
    echo If you have multiple Python versions installed and this script picked
    echo the wrong one, open a terminal where "python" resolves to 3.9-3.12
    echo (e.g. run "py -3.12 -m venv venv" and activate that venv first),
    echo then re-run this script.
    echo Continuing anyway, but installation may fail on unsupported versions.
    echo.
)

echo Step 1: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 2: Installing av (video processing library) with pre-built binary...
echo         (must happen before scrcpy-client, and before requirements.txt,
echo         so nothing pulls in an incompatible av version first)
python -m pip install av==16.0.1 --only-binary=:all:

echo.
echo Step 3: Installing scrcpy-client (without dependencies - requirements.txt
echo         already pins compatible versions of everything it needs)...
python -m pip install --no-deps -r requirements-scrcpy.txt

echo.
echo Step 4: Installing remaining dependencies (includes setuptools<81 for
echo         pkg_resources, and the adbutils version scrcpy-client needs)...
python -m pip install -r requirements.txt

echo.
echo Step 5: Verifying scrcpy imports correctly...
python -c "import scrcpy" 2>nul
if errorlevel 1 (
    echo.
    echo WARNING: "import scrcpy" failed. This usually means adbutils got
    echo upgraded past 0.15.0 by something after this script ran. Fix with:
    echo   python -m pip install "adbutils>=0.14.1,<0.15.0"
) else (
    echo OK.
)

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo You can now run the application!
pause