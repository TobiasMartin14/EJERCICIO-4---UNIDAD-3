
class Empleado: 
    __dni = str
    __nombre = str
    __direccion = str
    __telefono = str

    def __init__(self, nombre, dni, dir, tel):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = dir
        self.__telefono = tel
    
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    

    def getSueldo(self):
        pass
    def __str__(self):
        return "DNI: {} Nombre: {} Dirección: {} Teléfono:{} ".format(self.__dni, self.__nombre, self.__direccion, self.__telefono)

