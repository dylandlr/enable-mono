@echo off
REM Windows batch file to run FastAPI backend
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM Run FastAPI backend with uvicorn, loading .env automatically
cd /d %~dp0
setlocal
if exist ..\.env (
  for /f "usebackq delims=" %%a in (..\.env) do set "%%a"
)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
endlocal
