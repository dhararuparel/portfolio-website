@echo off
echo Starting Portfolio Website...
echo.
echo Make sure PostgreSQL is running and the database 'portfolio_db' exists.
echo.
echo Admin Login:
echo URL: http://localhost:5000/admin
echo Username: admin
echo Password: admin123
echo.
echo Portfolio URL: http://localhost:5000
echo.
python app.py
pause