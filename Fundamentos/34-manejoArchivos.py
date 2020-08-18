'''
    El primer parámetro es la ruta del archivo que vamos a utilizar.
    Como segundo parámetro indicaremos el modo en que se utilizará el archivo:
    - "r" (Read), es el valor por default y abre el archivo para lectura. Lanza error si el archivo no existe.
    - "a" (Append), abre un archivo para agregar información, si no existe el archivo, lo crea.
    - "w" (Write), abre un archivo para escritura, crea el archivo si no existe.
    - "x" (Create), crea un archivo, si el archivo ya existe, lanza un error.
    - "w+" o "r+", abre el archivo para modificarlo o leerlo.
'''
try:
    archivo = open("./Fundamentos/pruebaManejoArchivos.txt", "w")
    archivo.write("Agregando texto al archivo")
    archivo.write("\nAdíos")
except Exception as e:
    print(e)
finally:
    archivo.close() ## ! Después de close, no se puede trabajar con el archivo.