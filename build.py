# build.py

import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--windowed',
    '--clean',
    '--upx-dir=upx/',
    '--distpath=.',
    '--hidden-import=flet',
    '--hidden-import=atexit',
])

print("Сборка завершена!")
