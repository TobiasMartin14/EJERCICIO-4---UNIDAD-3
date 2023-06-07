
class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, ME):
        indice = True
        while indice:
            print("\n") 
            print ("Opcion 1: Registrar horas.")
            print ("Opcion 2: Total $$ de tarea.")
            print ("Opcion 3: Ayuda Económica.")
            print ("Opcion 4: Calcular sueldo.")
            print ("Opcion 5: Salir")
            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                dni = str(input("Ingrese el DNI del empleado a registrar horas: "))
                pos = ME.buscarEmpleado(dni)
                if(pos < 12):
                    ME.registrarHoras(pos)
                else:
                    print("No se encontró el empleado")
            elif (self.__opcion == 2):
                tarea = str(input("Ingrese una tarea: "))
                pos = ME.buscarTarea(tarea)
                if(pos < 12):
                    ME.mostrarMonto(pos)
                else:
                    print("No se encontró el empleado")
                #REVISAR
            elif (self.__opcion == 3):
                ME.listarAyuda()
            elif (self.__opcion == 4):
                ME.listarEmpleados()
                '''4. Calcular sueldo: Mostrar nombre, teléfono y sueldo a cobrar de todos los empleados.'''
            elif (self.__opcion == 5):
                indice = False
            else:
                print("La opcion ingresada no es valida.")