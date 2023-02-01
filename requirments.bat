@echo off
if "%1"=="fix" goto :a
echo Check addons?
CHOICE /C YN /t 5 /d y
if %errorlevel%==2 goto a

echo Checking for missing py addons
pip install SpeechRecognition>nul
pip install pyChatGPT>nul
pip install pyaudio>nul
pip install pyautogui>nul
pip install gkeepapi>nul
pip install keyring>nul
:a
echo Checking for missing core files
if not exist hal.cab echo hal.cab is missing
if not exist hal.cab if exist oldhal.cab ren oldhal.cab hal.cab
if not exist hal.cab if not exist oldhal.cab echo oldhal.cab is missing
call :checkandfix font.py
call :checkandfix data.json
call :checkandfix build.bat
call :checkandfix HALTEST.py
call :checkandfix ChromeSetup.exe
call :checkandfix HAL9000inputoutput.py
goto :EOF
:checkandfix
if not exist %1 echo %1 is missing
if not exist %1 ren %1.bak %1
if exist hal.cab if not exist %1 extrac32.exe /e hal.cab %1
exit /b
:EOF