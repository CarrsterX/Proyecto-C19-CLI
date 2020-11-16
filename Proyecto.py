from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
from Copia_CSV import copia_csv # importe de la funcion que repara los datos 
from CalculoT import porcentual, calculot # importe de la funcion que calcula a futuro los porcentajes y datos totales
import pandas as pd
import subprocess

def existe_data_inicial():
    aux0=subprocess.call('find TotalesNacionales_T.csv',shell=True)
    return aux0

def existe_data_reparada():
    aux0=subprocess.call('find datosc19.csv',shell=True)
    return aux0

def lector_data():
    aux0=existe_data_inicial()
    aux1=existe_data_reparada()
    if aux1 == 1:
        if aux0 == 1:
            instalador()
        copia_csv()
    data = pd.read_csv('datosc19.csv',header=0) 
    return data

if __name__ == '__main__':
    data = lector_data()
    variaciones= porcentual(data)# formula = (actual - anterior)/anterior //// en caso de que anterior sea 0 ((anterior - actual)/actual)*-1
    print(variaciones)
    finald=calculot(variaciones)
    print(finald)
    #ahora resta aplicar los porcentajes de las variaciones en los datos de 'casos totales'
    
    
