class Persona:
    MAYORIA_EDAD=18 #define
      
    def __init__(self,nombre,edad):
        #self.__nombre=""
        #self.__edad=0
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_nombre(self,nombre):
        if nombre!="":   #valido que el nombre no sea vacio
            self.__nombre=nombre

    def set_edad(self,edad):
        self.__edad=edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad

    def es_mayor_de_edad(self):
        if self.get_edad()>=Persona.MAYORIA_EDAD:
            return True
        else:
            return False
    
    @staticmethod
    def es_mayor_que(p,g):
        if p.get_edad()<g.get_edad():
            return True
        else:
            return False
        
#metodo estatico para imprimir una lista de personas 
    @staticmethod
    def print_personas(personas):
        for p in personas:
            print(p.get_nombre()+ " edad:"+str(p.get_edad()))
    
#metodo estatico para agrgar en un archivo una lista de personas ejercicio 6
    @staticmethod
    def dump_csv(nombre_archivo,personas):
        with open(nombre_archivo,"w",encoding="utf-8") as f: #si pongo w, puedo pasarle un string
            line="Nombre ,Edad \n"
            f.write(line)
            for p in personas:
                line=(p.get_nombre()+ "," + str(p.get_edad())+"\n") #Imprimo en el formato "Nombre","edad"
                # line="{},{}\n".format(p.get_nombre(),p.get_edad()) otra forma de imprimir
                f.write(line)
    
        
        
      