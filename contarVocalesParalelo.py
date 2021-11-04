
from multiprocessing import Process


class ContarVocalesParalelo(Process):
    def __init__(self, ruta, vocal):
        Process.__init__(self)
        self.ruta=ruta
        self.vocal=vocal

    def run(self):
       print("El numero de vocales " +self.vocal+ " es:" +str(self.contarVocales()))

    def contarVocales(self):
        numeroVocales=0
        fichero=open(self.ruta, "r", encoding='utf-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()==self.vocal:
                        numeroVocales+=1
            except UnicodeDecodeError:
                continue
        return numeroVocales


