#3_Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.

from persona1 import Persona

print("hola mundo")

p=Persona("Ernesto",24)
g=Persona("Sebastian ",46)

#print(type(p))
#p.__edad=45
#p.set_edad(45)

#p.__nombre="sebastian "
#p.set_nombre("Sebastian")

#Dos formas de imprimir lo mismo
print("{}  {}" .format(p.get_nombre(),p.get_edad()))  
print("{}  {}" .format(g.get_nombre(),g.get_edad()))  

if p.es_mayor_de_edad():
     
     print(p.get_nombre(),",es mayor de Edad")
else:
     print(p.get_nombre(),",es menor de Edad")

