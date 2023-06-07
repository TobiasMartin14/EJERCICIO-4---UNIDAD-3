from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fechaInicio = str
    __fechaFinalizacion = str
    __cantHTrabajadas = int
    #atributo de clase
    __valorHora = float

    def __init__(self, dni, nombre, direccion, telefono, fi, ff, ch):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fi
        self.__fechaFinalizacion = ff
        self.__cantHTrabajadas = ch

    @classmethod
    def setValorHora(cls,valor):
        cls.__valorHora=valor
    
    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    def getCantHTrabajadas(self):
        return self.__cantHTrabajadas
    
    @classmethod
    def getValorHora(cls):
        return cls.__valorHora
    
    def modificarHoras(self, horas):
        self.__cantHTrabajadas = self.__cantHTrabajadas + horas

    def getSueldo(self):
        return self.__cantHTrabajadas * self.getValorHora()
    
    def __str__(self):
        return super().__str__() + "\nFI: " + str(self.__fechaInicio) + " FF: " + str(self.__fechaFinalizacion) + "  Cant HT: " + str(self.__cantHTrabajadas) + "  Valor HT: " + str(self.getValorHora())


