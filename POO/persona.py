
class Persona:

    def __init__(self):
        self.__nombre=""
        self.__edad=0
    
    def set_nombre(self,nombre):
        if nombre!="":   #valido que el nombre no sea vacio
            self.__nombre=nombre

    def set_edad(self,edad):
        self.__edad=edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad


