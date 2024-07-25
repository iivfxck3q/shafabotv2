# build.py

import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--clean',
    '--upx-dir=upx/',
    '--hidden-import=flet',
    '--distpath=.',
])

print("Сборка завершена!")
