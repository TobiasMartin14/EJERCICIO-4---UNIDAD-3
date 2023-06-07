from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico = float
    __antiguedad = int

    def __init__(self, dni, nombre, direccion, telefono, sueldo, anti):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldo
        self.__antiguedad = anti


    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    
    def getSueldo(self):
        return self.__sueldoBasico + self.__sueldoBasico * (0.01 * self.__antiguedad)
    
    def __str__(self):
        return super().__str__() + "\nSueldo: $" + str(self.__sueldoBasico) + "  Antiguedad: " + str(self.__antiguedad)