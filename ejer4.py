#Escribir la función “es_par()” la cual recibe un número entero y devuelve True si el número es
#par o False si es impar.

def  es_par(arg):
    resultado=int(arg)%2
    if (resultado==0):
        return True
        #print("Es par")   
    else:
        return False
        #print ("Es Impar")


numero=input("Ingrese un numero :" )
print( )
r=es_par(numero)
print(r)



    


