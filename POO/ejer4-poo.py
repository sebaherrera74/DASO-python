#4. Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la
# del objeto actual.

from persona1 import Persona

print("hola mundo")

p=Persona("Ernesto",84)
g=Persona("Sebastian ",46)

#print(type(p))
#p.__edad=45
#p.set_edad(45)

#p.__nombre="sebastian "
#p.set_nombre("Sebastian")

#Dos formas de imprimir lo mismo
print("{}  {}" .format(p.get_nombre(),p.get_edad()))  
print("{}  {}" .format(g.get_nombre(),g.get_edad()))  

if Persona.es_mayor_que(p,g): #Verifico si la edad de la persona ingresada al ultimo es mayor que la prmera
    print("Es mayor ",g.get_nombre())
else:
    print("Es mayor ",p.get_nombre())


