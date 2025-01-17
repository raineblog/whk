@echo off
ipconfig /flushdns
@REM git config --unset http.proxy
@REM git config --unset https.proxy
@REM git config https.proxy http://127.0.0.1:10809
@REM git config https.proxy https://127.0.0.1:10809
@REM git submodule add https://github.com/RainPPR/material
@REM git submodule add https://github.com/RainPPR/intro docs/intro/
echo Updating...
git submodule update --remote
pause