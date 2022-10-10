def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor) #renglon += [valor]
        matriz.append(renglon)
    return matriz

def imprimirMatriz(matriz):
    salida = ""
    for renglon in matriz:
        for val in renglon:
            salida += str(val) + " "
        salida += "\n"
        
    print(salida)
    
def tamanoMatriz(matriz):
    """Regresa una tupla con el el numero de renglones
        y el numero de columnas que tiene la matriz que recibio """
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        if (numCol != len(renglon)):
            print("Error en el tamaño de las columnas")
            return -1,-1 #Codigo de error
    
    return numRen,numCol

def mismoTamano(mat1,mat2):
    """Regresa True si las dos matrices tienen las mismas dimensiones """
    numRen1,numCol1 = tamanoMatriz(mat1)
    numRen2,numCol2 = tamanoMatriz(mat2)
    
    renglones = False #bandera mismo numero de renglones
    columnas = False #bandera mismo numero de columnas
    if(numRen1 == numRen2):
        renglones = True
    else:
        print("Numero de renglones diferente")
        
    if(numCol1 == numCol2):
        columnas = True
    else:
        print("Numero de columnas diferente")
        
    return (renglones and columnas)

            