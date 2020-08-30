#Crear una lista vacia y agregarle 5 nombres. Ordenar la lista.

lista_nombre=[]
print(lista_nombre)
print("ingresar 5 nombres")

for i in range(5):
   nom=input("ingrese el nombre : ")
   lista_nombre.append(nom)

print(lista_nombre)
print( )

lista_nombre.sort()
print( )
print(lista_nombre)
