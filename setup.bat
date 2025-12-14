@echo off
echo Setting up Portfolio Website...
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Initializing database...
python populate_db.py

echo.
echo Setup complete!
echo.
echo To run the application, use: python app.py
echo Or double-click run.bat
echo.
echo Admin credentials:
echo Username: admin
echo Password: admin123
echo.
pause