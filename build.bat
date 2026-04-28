@echo off

python -m PyInstaller -F -n ssb -w --uac-admin -i assets\app.ico --add-data "assets/app.ico;assets" ssb.py