#Dado el archivo de configuración “config.txt” el cual tiene el formato clave=valor 
#en cada una de sus líneas, escribir una función que reciba el nombre del archivo
#y devuelva un diccionario con los valores especificados en el archivo.
#NOTA: Utilizar las funciones split() y strip()

def dicc_list(archivo):
    f=open(archivo,'r')
    listaraw=f.read()
    listaraw=listaraw.strip()
    lista=listaraw.split('\n')
    #print(lista)

    dicc={}
    for i in lista:
        aux=i.split('=')
        dicc[aux[0]]=aux[1]
    
    print(dicc)

dicc_list('config.txt')
    