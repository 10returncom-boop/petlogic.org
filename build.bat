@echo off
chcp 65001 >nul
echo ========================================
echo   PetLogic 網站一鍵构建
echo ========================================
echo.

echo [1/4] 產生分類頁面...
python scripts\generate_categories.py
if errorlevel 1 goto error

echo.
echo [2/4] 產生文章頁面...
python scripts\generate_posts.py
if errorlevel 1 goto error

echo.
echo [3/4] 產生佔位圖片（如已存在可跳過）...
python scripts\generate_placeholders.py
if errorlevel 1 goto error

echo.
echo [4/4] 產生 sitemap 與 RSS...
python scripts\generate_sitemap.py
if errorlevel 1 goto error

echo.
echo ========================================
echo   构建完成！
echo ========================================
echo.
echo 預覽網站: python -m http.server 8080
echo 然後瀏覽器打開 http://localhost:8080
echo.
pause
exit /b 0

:error
echo.
echo ========================================
echo   构建失敗，請檢查上方錯誤訊息
echo ========================================
pause
exit /b 1
