from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
import pandas as pd
import subprocess

def existe_data():
    aux0=subprocess.call('find activos_vs_recuperados.csv',shell=True)
    return aux0

def lector_data():
    aux0=existe_data()
    if aux0 == 1:
        instalador()
        data = lector_data()
        return data
    data = pd.read_csv('activos_vs_recuperados.csv',header=0) 
    return data

if __name__ == '__main__':
    data = lector_data()
    print(data['activos'])
