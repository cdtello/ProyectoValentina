# -*- mode: python -*-

block_cipher = None


a = Analysis(['pythonP.py'],
             pathex=['C:\\Users\\C.TELLO\\Desktop\\Univalle2018\\Por_hacer\\Proyecto_Valentina'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pythonP',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
