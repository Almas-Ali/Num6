@echo off
:: Installation for num6
echo installing Num6...
xcopy "num6" "C:\Windows\" >nul
(
echo @echo off
echo python num6
)>C:\Windows\num6.bat
echo installation of Num6 completed...
