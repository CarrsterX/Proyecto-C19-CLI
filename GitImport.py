import subprocess
import os

aux = os.getcwd()

print("Se encuentra en el directorio: "+aux)

if os.path.isdir(aux+'/BaseDatos'):
    os.chdir(aux+'/BaseDatos')
else:
    os.mkdir(aux+'/BaseDatos')
    os.chdir(aux+'/BaseDatos')

aux2 = subprocess.call('apt list --installed | grep subversion',shell=True)

if aux2 == 1:
    print('El programa svn no se encuentra instalado')
    print('Desea instalarlo(S/N): ' ,end=''), 
    aux3= input()
    if aux3 == 's':
        subprocess.call("sudo apt install subversion", shell=True)
    if aux3 == 'n':
        print("Terminando ejecucion")    
        exit()

print("Importando Datos")
subprocess.call("svn export --force https://github.com/MinCiencia/Datos-COVID19/branches/master/output/producto1", shell=True)