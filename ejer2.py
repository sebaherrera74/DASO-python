#Crear una lista vacía, imprimir el campo id, el tipo y el valor de la lista. Luego agregar un número
#a la lista y volver a imprimir id,tipo y valor. ¿Cuáles son las diferencias?
lista=[]
print(type(lista))   #imprime el tipo d ela lista 
print(lista)         #imprime los vaores de la lista   
print(id(lista))     #imprime el id  de la lista 

lista.append(23)

print(type(lista))   #imprime el tipo d ela lista 
print(lista)         #imprime los vaores de la lista   
print(id(lista))     #imprime el id  de la lista 

lista.append(89023)
print(type(lista))   #imprime el tipo d ela lista 
print(lista)         #imprime los vaores de la lista   
print(id(lista))     #imprime el id  de la lista 

