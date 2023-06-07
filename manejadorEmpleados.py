import numpy as np
from numpy import ndarray
import csv
#from datetime import datetime
from claseEmpleado import Empleado
from empleadoPlanta import EmpleadoPlanta
from empleadoContratado import EmpleadoContratado
from empleadoExterno import EmpleadoExterno

class ManejadorEmpleados:
    __arregloEmpleados = ndarray
    __dimension = int
    __indice = int

    def __init__(self, dimension, indice = 0):
        self.__arregloEmpleados=np.empty(dimension,dtype=Empleado)
        self.__dimension = dimension
        self.__indice = indice
    
    def cargarEmpleados(self):
        self.cargarPlanta()
        self.cargarContratados()
        EmpleadoContratado.setValorHora(5000)
        self.cargarExternos()
        print("Empleados cargados.")

    def cargarPlanta(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                instancia = EmpleadoPlanta(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]), int(fila[5]))
                self.__arregloEmpleados[self.__indice] = instancia
                self.__indice = self.__indice + 1
        archivo.close
        return


    def cargarContratados(self):
        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                instancia = EmpleadoContratado(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), int(fila[6]))
                self.__arregloEmpleados[self.__indice] = instancia
                self.__indice = self.__indice + 1
        archivo.close
        return


    def cargarExternos(self):
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                instancia = EmpleadoExterno(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), str(fila[6]), float(fila[7]), float(fila[8]), float(fila[9]))
                self.__arregloEmpleados[self.__indice] = instancia
                self.__indice = self.__indice + 1
        archivo.close
        return
    
    def mostrarCarga(self): #esta feo hecho, pero la idea es solo que muestre con el print arriba sin iterarlo, sé que estoy utilizando for demás
        print("\n")
        print("EMPLEADO DE PLANTA:")
        for emp in self.__arregloEmpleados:
            if isinstance(emp, EmpleadoPlanta):
                print(emp)
        
        print("\n")
        print("EMPLEADO CONTRATADO:")
        for emp in self.__arregloEmpleados:
            if isinstance(emp, EmpleadoContratado):
                print (emp)

        print("\n")
        print("EMPLEADO EXTERNO:")
        for emp in self.__arregloEmpleados:
            if isinstance(emp, EmpleadoExterno):
                print(emp)


    def buscarEmpleado(self, dni):
        indice = True
        i = 0
        while i < len(self.__arregloEmpleados) and indice:
            if self.__arregloEmpleados[i].getDNI() == dni:
                indice = False
                print("Lo encontramos! {}" .format(self.__arregloEmpleados[i].getDNI()))
            else:
                i = i + 1
        return i

    def registrarHoras(self, pos):
        #print("{}" .format(pos))
        if isinstance(self.__arregloEmpleados[pos], EmpleadoContratado):
            horas = int(input("Ingrese la cantidad de horas trabajadas: "))
            print("Horas trabajadas antes del registro: {}" .format(self.__arregloEmpleados[pos].getCantHTrabajadas()))
            self.__arregloEmpleados[pos].modificarHoras(horas)
            print("Horas trabajadas despues del registro: {}" .format(self.__arregloEmpleados[pos].getCantHTrabajadas()))
        else:
            print("El empleado no es contratado, por lo tanto no se puede realizar su registro de horas trabajadas.")

    def buscarTarea(self, tarea):
        indice = True
        i = 0
        while i < len(self.__arregloEmpleados) and indice:
            opcion = isinstance (self.__arregloEmpleados[i], EmpleadoExterno)
            if opcion:
                if self.__arregloEmpleados[i].getTarea() == tarea:
                    indice = False
                    print("Lo encontramos! {}" .format(self.__arregloEmpleados[i].getDNI()))
            else:
                i = i + 1
        return i
    
    def mostrarMonto(self, pos):
        fechaActual = str(input("Ingrese la fecha actual (formato: xx/xx/xxxx): "))
        if fechaActual > self.__arregloEmpleados[pos].getFechaFinalizacion():
            print("El monto a pagar por la tarea: {}, es: ${}" .format(self.__arregloEmpleados[pos].getTarea(), self.__arregloEmpleados[pos].getCostoObra()))
        else:
            print("Aun la tarea no finalizó.")


    def listarAyuda(self):
        print("LISTADO DE PERSONAS QUE LES CORRESPONDE LA AYUDA.")
        for emp in self.__arregloEmpleados:
            #print("SUELDO: {}" .format(emp.getSueldo()))
            if emp.getSueldo() < 150000:
                print("Nombre: {},  direccion: {}, DNI: {}" .format(emp.getNombre(), emp.getDireccion(), emp.getDNI()))

    def listarEmpleados(self):
        print("EMPLEADOS:")
        for emp in self.__arregloEmpleados:
            print("Nombre: {},  telefono: {}, sueldo: ${}" .format(emp.getNombre(), emp.getTelefono(), emp.getSueldo()))
