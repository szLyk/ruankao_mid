@echo off
cd /d "%~dp0"
rem find the practice page (name starts with 17-) without hardcoding non-ASCII
set "PAGE="
for /f "delims=" %%f in ('dir /b "17-*.html" 2^>nul') do if not defined PAGE set "PAGE=%%f"
if not defined PAGE (
  echo [X] 17-*.html not found in this folder.
  pause
  exit /b 1
)
set "CH=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%CH%" set "CH=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not exist "%CH%" set "CH=%LocalAppData%\Google\Chrome\Application\chrome.exe"
if not exist "%CH%" set "CH=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not exist "%CH%" set "CH=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if exist "%CH%" (
  start "" "%CH%" --new-window "%~dp0%PAGE%"
) else (
  start "" "%~dp0%PAGE%"
)
