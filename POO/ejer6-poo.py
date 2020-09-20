#6. Agregar un método estático “dump_csv” que reciba el nombre de un archivo, una lista de
#personas y genere un archivo CSV separado por comas con los datos de cada persona.

from persona1 import Persona

print("Hola MUNDO")

p1=Persona("Sebastian",45)
p2=Persona("Belen",25)
p3=Persona("Paula",23)
p4=Persona("Felipe",5)

personas=[]  #creo lista de personas

#agrego las personas creadas a la lista 
personas.append(p1)
personas.append(p2)
personas.append(p3)
personas.append(p4)

#Imprimo la lista con metodo estatico 
#Persona.print_personas(personas)

#Guardo en un formato determinado .csv y la lista creada
Persona.dump_csv("personas.csv",personas)







