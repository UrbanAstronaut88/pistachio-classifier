@echo off
REM start.bat

REM
SET PORT=%PORT%
IF "%PORT%"=="" SET PORT=10000

REM
REM app:app
gunicorn app:app --bind 0.0.0.0:%PORT% --workers 1 --timeout 300
