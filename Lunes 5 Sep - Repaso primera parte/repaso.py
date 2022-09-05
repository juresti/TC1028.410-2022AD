def lineaSolida(ancho):
    linea = ""
    for cont in range(ancho):
        linea += "#"
    return linea

def rectSolido(alto,ancho):
    salida = ""
    for veces in range(alto):
        salida += lineaSolida(ancho) + "\n"
    return salida

def main():
    #Ejercicio 1
    print("*** Ejercicio 1 ***")
    num = int(input("Dime el ancho de la linea: "))
    linea = lineaSolida(num)
    print(linea)
    
    #Ejercicio 2
    print("*** Ejercicio 2 ***")
    wide = int(input("Dime el ancho del rectangulo: "))
    height = int(input("Dime el alto del rectangulo: "))
    rec = rectSolido(height,wide)
    print(rec)
    