# -*- mode: python ; coding: utf-8 -*-
# BulkMailer Pro — PyInstaller spec file
# Build: pyinstaller bulkmailer.spec

import sys
import os
from pathlib import Path

block_cipher = None

# Collect all data files
datas = []

# Include templates dir if it exists
templates_dir = Path('templates')
if templates_dir.exists():
    datas.append(('templates', 'templates'))

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[
        # PyQt5
        'PyQt5.QtWebEngineWidgets',
        'PyQt5.QtWebEngineCore',
        'PyQt5.QtWebChannel',
        'PyQt5.QtPrintSupport',
        # Data
        'pandas',
        'pandas._libs.tslibs.base',
        'openpyxl',
        'openpyxl.cell._writer',
        # Google OAuth
        'google.oauth2.credentials',
        'google.auth.transport.requests',
        'google_auth_oauthlib.flow',
        'googleapiclient.discovery',
        'googleapiclient.errors',
        # Email
        'email.mime.multipart',
        'email.mime.text',
        'smtplib',
        'ssl',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'scipy',
        'numpy.testing',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BulkMailerPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # No console window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.ico',  # Uncomment if you have an icon
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BulkMailerPro',
)
