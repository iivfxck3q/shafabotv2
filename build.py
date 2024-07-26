# build.py

import PyInstaller.__main__
import os
import platform

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    # '--windowed',
    '--clean',
    '--upx-dir=upx/',
    '--distpath=.',
])


system = platform.system()
if system == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print("Сборка завершена!")
