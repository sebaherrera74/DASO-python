#Escribir una función que reciba un string y reemplace los espacios por un 
# caracter que reciba por argumento. 
# La función debera devolver el nuevo string.

def remplaza_espacio(caract,cad):
    nueva_cadena=cad.replace(" ",caract)   #Se usa ".replace" para remplazar 
    print(nueva_cadena)


cadena=str(input("ingrese un string :"))

print(cadena)
print()
caract=str(input("Ingrese caracter a reemplazar:"))
#print(caract)

remplaza_espacio(caract,cadena)




