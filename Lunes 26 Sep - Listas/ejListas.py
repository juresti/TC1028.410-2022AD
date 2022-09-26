def listaPersonas(num):
    salida = []
    for veces in range(num):
        nombre = input(f"Dime el nombre de la persona {veces+1}: ")
        salida.append(nombre)
    return salida

def imprimePersona(lista):
    for persona in lista:
        print(persona)
        
def menu():
    print("\n1. Alta de personas")
    print("2. Impresion de personas registradas")
    print("3. Salir")
    op = int(input("Dime la opcion que deseas: "))
    return op

def main():
    lisPer = []
    opcion = 0
    while (opcion != 3):
        opcion = menu()
        if (opcion == 1):
            numPer = int(input("Dime cuantas personas quieres dar de alta: "))
            lisPer = listaPersonas(numPer)
        elif (opcion == 2):
            imprimePersona(lisPer)
        elif (opcion == 3):
            print("Hasta luego")
        else:
            print("Opcion no valida. Vuelve a intentarlo.")
        
main()