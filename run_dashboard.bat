@echo off
echo =======================================
echo Enterprise Clickstream Analytics Setup
echo =======================================
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Installing dependencies...
    venv\Scripts\python -m pip install --upgrade pip
    venv\Scripts\pip install -r requirements.txt
)
echo Starting Dashboard...
cd dashboard
..\venv\Scripts\streamlit run app.py
pause
