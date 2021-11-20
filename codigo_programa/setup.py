from sys import executable, version
import cx_Freeze

executables = [cx_Freeze.Executable('fisica_game.py', base="Win32GUI", icon="img/icone_exe.ico", target_name="Física Game.exe")]


cx_Freeze.setup(
    name = "Física Game",
    version = "1.6",
    options = {"build_exe": {'packages':['pygame'],
    'include_files': ['arquivos', 'img', 'musicas']}},

    executables = executables    
    
)