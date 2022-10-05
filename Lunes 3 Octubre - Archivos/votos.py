def leerVotos():
    archivo = open("votos.txt","r")
    contenido = archivo.readlines()
    archivo.close()
    print(contenido)
    
    #limpieza creando otra lista
    listaLimpia = []
    for voto in contenido:
        listaLimpia.append(voto.rstrip())
    print(listaLimpia)
    
    #limpieza sacando y volviendo a guardar
    for pos in range(len(contenido)):
        contenido[pos] = contenido[pos].rstrip()
    print(contenido)
    