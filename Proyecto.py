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
    temp = (len(data['Casos nuevos totales'])-1)
    i = temp - 20 # el numero son la cantidad de dias antes 
    while i < temp:
        
        actual= data['Casos nuevos totales'][i+1]
        anterior= data['Casos nuevos totales'][i]

        if anterior == 0:
            lista_porcentajes.append(((anterior-actual)/actual)*-1)

        else:
            porcentual= ((actual-anterior)/anterior)

            lista_porcentajes.append(round(porcentual,4))
        i = i+1
    variaciones= {'porcentajes': lista_porcentajes}
    return variaciones

def calculot(variaciones):
    
    print("A cuantos dias a futuro desea realizar el calculo: ", end="")
    d=input()
    d=int(d)
    
    data1=pd.read_csv('datosc19.csv',header=0)
    aux0=data1[["Casos totales"]]
    new_data = []
    res = []
    k=0
    diccionario0={}
    
    for i in (range(len(aux0["Casos totales"]))):
        diccionario = {}
        aux1=aux0["Casos totales"][i]
        
    for j in (range(len(variaciones["porcentajes"]))):
        aux3=variaciones["porcentajes"][j]
        new_data.append(aux3)
    
    res=[]
    
    while k < d:
        suma=sum(new_data)
        prom=suma/len(new_data)
        new_data.append(prom)
        aux1=int(aux1+(aux1*prom))
        res.append(aux1)
        k=k+1 
    d=str(d)
    diccionario0={"Casos a "+d+" dias a futuro":res}

    return diccionario0

if __name__ == '__main__':
    data = lector_data()
    variaciones= porcentual(data)# formula = (actual - anterior)/anterior //// en caso de que anterior sea 0 ((anterior - actual)/actual)*-1
    finald=calculot(variaciones)
    print(finald)
    #ahora resta aplicar los porcentajes de las variaciones en los datos de 'casos totales'
    
    
