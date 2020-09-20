#5. Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el 
#de edad mayor.


from persona1 import Persona

p1=Persona("Ernesto",54)
p2=Persona("Sebastian",46)
p3=Persona("paola",36)

personas=[]
personas.append(p1)
personas.append(p2)
personas.append(p3)

for p in personas:
    print("Nombre:",p.get_nombre(),"Edad:",p.get_edad())

if Persona.es_mayor_que(p1,p2): #Verifico si la edad de la persona ingresada al ultimo es mayor que la prmera
    print("Es mayor ",p2.get_nombre())
else:
    print("Es mayor ",p1.get_nombre())



