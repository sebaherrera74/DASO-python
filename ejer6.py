#Escribir una función que reciba una lista de tuplas, por ejemplo:
#[('George', '4312 Abbey Road',22), ('John','54 LoveAve', 21)]
#La función deberá generar un archivo CSV (separado por comas) en donde cada línea será un ítem
#de la lista, el archivo debera contener:
#name,address,age
#George,4312 Abbey Road,22
#John,54 Love Ave,21

import csv 


def funcion_lista_tuplas(list):
    myFile=open('ejemplo.csv','w')

    with myFile:
        writer=csv.writer(myFile)
        writer.writerows(list)

    print(list)


lista_tuplas=[('name  ','  addres  ','  age  '),('George', '4312 Abbey Road',22), ('John','54 LoveAve', 21)]

funcion_lista_tuplas(lista_tuplas)

#agrego otra Tupla para probar 
lista_tuplas.append(('seba','147 tarapaya', 1593))
funcion_lista_tuplas(lista_tuplas)


#funcion_lista_tuplas(lista_tuplas)


#print(lista_tuplas)

#lista_tuplas.append(('seba','147 tarapaya', 1593))
#print()
#print(lista_tuplas)
#lista_tuplas.insert(0,('seba','147 tarapaya', 1593))
#print()
#print(lista_tuplas)