try:
    archivo = open("./Fundamentos/pruebaManejoArchivos.txt", "r")
    # #print(archivo.read()) ## * Puede recibir como parámetro cuantos caracteres va a leer. read(4)
    ## print(archivo.readline()) ## * Lee una línea del archivo
    ## lineas = archivo.readlines() ## * Devuelve una lista con cada línea del archivo
    print(archivo.readlines()[1]) ## * Accede al índice de la línea  que queremos
except Exception as e:
    print(e)
finally:
    archivo.close()