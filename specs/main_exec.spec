# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['..\\.\\srcs\\main_exec.py'],
             pathex=['..\\.\\srcs'],
             binaries=[],
             datas=[('..\\.\\srcs\\data', './data')],
             hiddenimports=['utils.pyTask', 
                            'utils.date', 
                            'GUI.dial', 
                            'GUI.mainWindow', 
                            'PyQt5.sip',
                            'GUI.timer',
                            'GUI.taskWidget',
                            'posix',
                            'resource',
                            'sip'],
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
          name='main_exec',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
