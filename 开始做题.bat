@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "CH=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%CH%" set "CH=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not exist "%CH%" set "CH=%LocalAppData%\Google\Chrome\Application\chrome.exe"
if exist "%CH%" ( start "" "%CH%" --new-window "%~dp017-在线练习系统.html" ) else start "" "%~dp017-在线练习系统.html"
