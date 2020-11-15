from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
from Copia_CSV import copia_csv # importe de la funcion que repara los datos 
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

def porcentual(data):

    lista_porcentajes= []
    for i in (range(len(data['Casos nuevos totales'])-1)):
        
        actual= data['Casos nuevos totales'][i+1]
        anterior= data['Casos nuevos totales'][i]

        if anterior == 0:
            lista_porcentajes.append(((anterior-actual)/actual)*-1)

        else:
            porcentual= ((actual-anterior)/anterior)

            lista_porcentajes.append(round(porcentual,4))
            
    variaciones= {'porcentajes': lista_porcentajes}
    return variaciones


if __name__ == '__main__':
    data = lector_data()
    variaciones= porcentual(data)# formula = (actual - anterior)/anterior //// en caso de que anterior sea 0 ((anterior - actual)/actual)*-1
    print(variaciones)
    
    #ahora resta aplicar los porcentajes de las variaciones en los datos de 'casos totales'
    
    
