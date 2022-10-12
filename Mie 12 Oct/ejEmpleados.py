def menu():
    print("1. Leer datos archivo")
    print("2. Escribir datos en archivo")
    print("3. Reporte de empleados")
    print("4. Alta empleado")
    print("5. Consulta de empleado")
    print("6. Salir")
    
    return int(input("Dime tu opcion: "))

def leeDatosArchivo():
    return [["Luis",99,3.14],["Sara",15,88.74],["Emilio",28,53.81]]

def escribeDatosArchivo(listaDatos):
    print("Escribiendo en archivo esto: ", listaDatos)

def reporteEmpleados(listaDatos):
    print("\n REPORTE DE EMPLEADOS \n")
    for empleado in listaDatos:
        print(f"Nombre: {empleado[0]}")
        print(f"Edad: {empleado[1]}")
        print(f"Salario: {empleado[2]}\n")
        
def altaEmpleado(datos):
    nombre = input("Dime el nombre: ")
    edad = int(input("Dime la edad: "))
    salario = float(input("Dime el salario: "))
    lista = [nombre, edad, salario]
    datos.append(lista)
    return datos

def consultaEmpleado(listaDatos,nom):
    encontrado = False
    for empleado in listaDatos:
        if (empleado[0] == nom):
            encontrado = True
            print(f"Nombre: {empleado[0]}")
            print(f"Edad: {empleado[1]}")
            print(f"Salario: {empleado[2]}\n")
            break
    
    if not(encontrado):
        print(f"La persona {nom} no es empleado")

def main():
    datos = []
    op = 0
    while(op != 6):
        op = menu()
        if (op == 1):
            datos = leeDatosArchivo()
            print("Datos leidos")
        elif (op == 2):
            escribeDatosArchivo(datos)
            print("Datos guardados en el archivo")
        elif (op == 3):
            reporteEmpleados(datos)
        elif (op == 4):
            datos = altaEmpleado(datos)
        elif (op == 5):
            nombre = input("Dime el nombre del empleado a consultar: ")
            consultaEmpleado(datos,nombre)
        elif (op == 6):
            print("Hasta luego")
        else:
            print("Opciones validas del 1 al 6.\nVuelve a intentar")
            
    
main()
