@echo off
color 80
mode con: cols=18 lines=1
pythonw "%cd%\calculadora.py" && exit
cls
color 0a
echo Se ha cerrado el programa correctamente
timeout 5
