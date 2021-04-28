#transforma archivos python a exe 
#instalar cx_freeze y idna en cmd 
#pip intall cx_freeze 
#pip install idna 

from cx_Freeze import setup, Executable

base = None
executables = [Executable("love_calc.py", base=base)] # donde dice love_calc.py reemplazar con el nombre de tu archivo .py 
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
