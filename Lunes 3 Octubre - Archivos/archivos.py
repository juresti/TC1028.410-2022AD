import os
print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\Desktop")
print(os.getcwd())

def leerArchivoRead(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.read()
    miArchivo.close()
    
    print(contenido)
    return contenido

def leerArchivoReadline(nombre):
    miArchivo = open(nombre + ".txt","r")
    
    contenido = miArchivo.readline()
    while (contenido != ""):
        print(contenido)
        contenido = miArchivo.readline()
    
    miArchivo.close()
    
    return contenido

def leerArchivoReadlines(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.readlines()
    miArchivo.close()
    
    print(contenido)
    return contenido

def escribirArchivoWrite(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.write("esta es una prueba")
    miArchivo.close()
    print("Archivo escrito a disco")
    
def escribirArchivoWritelines(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.writelines(["primera linea\n","segunda linea\n", "tercera linea\n"])
    miArchivo.close()
    print("Archivo escrito a disco")
