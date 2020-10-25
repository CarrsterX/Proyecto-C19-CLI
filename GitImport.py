import subprocess
import os
aux = os.getcwd()
if os.path.isdir(aux+'/Documentos/Modulo/BaseDatos'):
    os.chdir(aux+'/Documentos/Modulo/BaseDatos');
else:
    os.mkdir(aux+'/Documentos/Modulo/BaseDatos')
    os.chdir(aux+'/Documentos/Modulo/BaseDatos');
print("Se encuentra en el directorio: "+aux)
#if ()
subprocess.call("svn export --force https://github.com/MinCiencia/Datos-COVID19/branches/master/output/producto1", shell=True)