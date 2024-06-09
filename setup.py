# setup.py

import cx_Freeze
import sys

# Set base to None to avoid console opening in the background
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# The file to execute
executables = [cx_Freeze.Executable("main.py", base=base)]

# Setup
cx_Freeze.setup(
    name="BlockBlast",
    version="1.0",
    options={"build_exe": {"packages": ["pygame"]}},
    description="Block Blast Game",
    executables=executables
)
