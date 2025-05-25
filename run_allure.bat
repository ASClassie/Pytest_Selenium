
@echo off
echo =============================
echo Running Pytest with Allure...
echo =============================

pytest %* --alluredir=test-results/allure-results

IF %ERRORLEVEL% NEQ 0 (
    echo Pytest failed. Skipping report generation.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo =============================
echo Generating Allure Report...
echo =============================
allure generate test-results/allure-results --clean -o test-results/allure-report

IF %ERRORLEVEL% NEQ 0 (
    echo Allure report generation failed.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo =============================
echo Opening Allure Report in Chrome...
echo =============================
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files "D:\Pytest_Selenium\test-results\allure-report\index.html"


echo.
echo Report opened successfully!
pause
