""" Estos son ejercicios de repaso
del tema de for
"""
def cuenta4en4(inicio,fin):
    for cuenta in range(inicio,fin+1,4):
        print(cuenta)
    
def divisibles7(inicio,fin):
    cont = 0
    for numero in range(fin,inicio-1,-1):
        res = numero % 7
        if (res == 0):
            print(numero)
            cont += 1
    return cont
