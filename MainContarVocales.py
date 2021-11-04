import os
import time
from contarVocalesSerial import ContarVocalesSerial
from contarVocalesParalelo import ContarVocalesParalelo


if __name__ == "__main__":
    ruta_archivo=input("Introduzca la ruta completa del archivo")
    if os.path.exists(ruta_archivo):
        if os.path.isfile(ruta_archivo):
            inicioEjecucionS = time.perf_counter()
            contarvocalesserial = ContarVocalesSerial(ruta_archivo)
            print("El numero de vocales a que se encuentran en el documento son: " + str(contarvocalesserial.contarVocala()))
            print("El numero de vocales e que se encuentran en el documento son: " + str(contarvocalesserial.contarVocale()))
            print("El numero de vocales i que se encuentran en el documento son: " + str(contarvocalesserial.contarVocali()))
            print("El numero de vocales o que se encuentran en el documento son: " + str(contarvocalesserial.contarVocalo()))
            print("El numero de vocales u que se encuentran en el documento son: " + str(contarvocalesserial.contarVocalu()))
            finalEjecucionS = time.perf_counter() - inicioEjecucionS
            print("El tiempo de ejecucion del proceso contar vocales en Serial es:" + str(round(finalEjecucionS, 2)))

            inicioEjecucion= time.perf_counter()
            contarvocala = ContarVocalesParalelo(ruta_archivo, "a")
            contarvocale = ContarVocalesParalelo(ruta_archivo, "e")
            contarvocali = ContarVocalesParalelo(ruta_archivo, "i")
            contarvocalo = ContarVocalesParalelo(ruta_archivo, "o")
            contarvocalu = ContarVocalesParalelo(ruta_archivo, "u")
            contarvocala.start()
            contarvocale.start()
            contarvocali.start()
            contarvocalo.start()
            contarvocalu.start()
            contarvocala.join()
            contarvocale.join()
            contarvocali.join()
            contarvocalo.join()
            contarvocalu.join()
            finalEjecucion = time.perf_counter() - inicioEjecucion
            print("El tiempo de ejecucion del proceso contar vocales en paralelo es:" + str(round(finalEjecucion, 2)))
        else:
            print("El parametro debe ser un archivo")
    else:
        print("El archivo no existe")


        """"""