import cx_Freeze
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

executables = [cx_Freeze.Executable("src\main.py", base = base)]

cx_Freeze.setup(
    name = "Tetris",
    version = "0.2"
    options = {"build.exe": {"packages": ["pygame"]}},
    description = "Tetris Game",
    executables = executables
    )

