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
        
        
      