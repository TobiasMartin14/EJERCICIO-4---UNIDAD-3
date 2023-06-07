from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = str
    __fechaInicio = str
    __fechaFinalizacion = str
    __montoViatico = float
    __costoObra = float
    __montoSeguro = float

    def __init__(self, dni, nombre, direccion, telefono, tarea, fi, ff, mv, co, ms ):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fi
        self.__fechaFinalizacion = ff
        self.__montoViatico = mv
        self.__costoObra = co
        self.__montoSeguro = ms
    
    def getTarea(self):
        return self.__tarea
    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    def getMontoViatico(self):
        return self.__montoViatico
    def getCostoObra(self):
        return self.__costoObra
    def getMontoSeguro(self):
        return self.__montoSeguro
    
    def getSueldo(self):
        return self.__costoObra - self.__montoViatico - self.__montoSeguro
    
    def __str__(self):
        return super().__str__() + " \n" + "Tarea: " + self.__tarea + " fecha inicio: " + self.__fechaInicio + ' fecha finalizacion: ' + self.__fechaFinalizacion + " monto viatico: $" + str(self.__montoViatico) + " costo de obra: $" + str(self.__costoObra) + " seguro: $" + str(self.__montoSeguro)



'''
5.   Los empleados externos realizan tareas especiales estas tareas pueden ser carpintería, electricidad, plomería. 
Para este tipo de empleados, además de los datos de empleados, se registra: tarea, fecha de inicio, fecha de finalización, 
monto viático, el costo de la obra y monto del seguro de vida.

'''