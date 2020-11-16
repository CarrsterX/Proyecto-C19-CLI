import pandas as pd

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
    
