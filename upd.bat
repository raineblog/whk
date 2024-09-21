@echo off
ipconfig /flushdns
git config --unset http.proxy
git config --unset https.proxy
rem git config https.proxy http://127.0.0.1:10809
rem git config https.proxy https://127.0.0.1:10809
@REM git submodule add https://github.com/RainPPR/material
@REM git submodule add https://github.com/RainPPR/intro docs/intro/
echo.updating...
git submodule update --remote
pause