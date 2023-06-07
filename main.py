from manejadorEmpleados import ManejadorEmpleados
from menu import Menu

if __name__=='__main__':
    ME=ManejadorEmpleados(int(input('Ingrese dimensión del arreglo: ')))
    print("Arrgelo creado")
    ME.cargarEmpleados()
    ME.mostrarCarga()
    menu=Menu()
    menu.opciones(ME)
