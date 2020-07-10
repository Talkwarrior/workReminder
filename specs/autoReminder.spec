# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['..\\.\\srcs\\autoReminder.py'],
             pathex=['..\\.\\srcs',
                     r'C:\Users\user\Anaconda3\envs\workReminder\Lib\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=['win32com',
                            'termios',
                            'pyimod03_importers',
                            'pkg_resources',
                            'pkg_resources.py2_warn',
                            'resource'
                            ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='autoReminder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
          
