def cuantos():
    contNeg = 0
    contPos = 0
    contCero = 0
    cont = 0
    while(cont < 5):
        num = int(input("Dime un numero: "))
        if (num < 0):
            contNeg += 1
        elif (num > 0):
            contPos += 1
        else:
            contCero += 1
        
        cont += 1
        
    
    return contPos,contNeg,contCero

def convertirNeg(cuantos):
    cont = cuantos
    while (cont > 0):
        num = int(input("Dime un numero negativo: "))
        while(num >= 0):
            num = int(input("Dime un numero negativo: "))    
        print(-1 * num)
        cont -= 1
    
    

def main():
    #Ejercicio 1
    print("*** Ejercicio 1 ***")
    pos,neg,cero = cuantos()
    print(f"Tuviste {pos} positivos, {neg} negativos y {cero} ceros")
    
    #Ejercicio 2
    print("\n*** Ejercicio 2 ***")
    veces = int(input("Dime cuantos convertir: "))
    convertirNeg(veces)

main()
