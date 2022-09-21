def voltear(pal):
    salida = ""
    for letra in pal:
        salida = letra + salida
    return salida

def voltearV2(pal):
    salida = ""
    fin = len(pal) * -1
    for pos in range(-1,fin-1,-1):
        salida += pal[pos]
    return salida
