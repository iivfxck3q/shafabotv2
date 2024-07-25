# build.py

import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--windowed',
    '--upx-dir=upx/',
    '--hidden-import=flet',
])

print("Сборка завершена!")
