from cx_Freeze import setup, Executable

base = None
executables = [Executable("love_calc.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<Html_Code>",
    options = options,
    version = "0.1",
    description = '<Get html structure from any site>',
    executables = executables
)