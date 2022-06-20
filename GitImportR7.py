import subprocess
import os

def instalador():
    
    aux = os.getcwd()

    print("\nSe encuentra en el directorio: "+aux)
    
    aux2 = subprocess.call('apt list --installed | grep subversion',shell=True)

    if aux2 == 1:
        print('El programa svn no se encuentra instalado')
        print('Desea instalarlo(S/N): ', end=''), 
        aux3= input()
        
        if aux3 == 's':
            subprocess.call("sudo apt install subversion", shell=True)
        elif aux3 == 'n':
            print("Terminando ejecucion")    
            exit()
        elif aux2 != 's' or aux2 != 'n':
            print("Opcion ingresada invalida")
            instalador()
    subprocess.call("svn list https://github.com/MinCiencia/Datos-COVID19/branches/master/output/producto4 > data.txt", shell=True)
    data=open("data.txt", "r")
    lines= data.readlines()
    file=lines[-2:]
    file=file[0].strip('\n')
    print(file)

    print("Importando Datos")
    subprocess.call("svn export --force https://github.com/MinCiencia/Datos-COVID19/branches/master/output/producto4/"+file, shell=True)
    return file

#instalador()