#1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
#“print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos
#creo un modulo persona.py 

from persona import Persona 

print("hola mundo")

p=Persona()
print(type(p))
#p.__edad=45
p.set_edad(45)

#p.__nombre="sebastian "
p.set_nombre("Sebastian")

#Dos formas de imprimir lo mismo
print("{}  {}" .format(p.get_nombre(),p.get_edad()))  
#print("%s  %d " % (p.nombre,p.edad))

