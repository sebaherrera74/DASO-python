#2. Agregarle a la clase anterior un constructor que reciba nombre y edad.

from persona1 import Persona

print("hola mundo")

p=Persona("Ernesto",34)
g=Persona("Sebastian ",46)

#print(type(p))
#p.__edad=45
#p.set_edad(45)

#p.__nombre="sebastian "
#p.set_nombre("Sebastian")

#Dos formas de imprimir lo mismo
print("{}  {}" .format(p.get_nombre(),p.get_edad()))  
print("{}  {}" .format(g.get_nombre(),g.get_edad()))  

#print("%s  %d " % (p.nombre,p.edad))