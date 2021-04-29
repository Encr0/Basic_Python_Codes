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
    name = "", #esto se cambia al nombre que tu le quieras poner 
    options = options, #no tocar 
    version = "0.1", #numero de version
    description = '', #descripcion
    executables = executables #no tocar 
)
