
class ContarVocalesSerial():
    def __init__(self, ruta):
        self.ruta=ruta

    def contarVocala(self):
        a=0
        fichero=open(self.ruta, "r", encoding='UTF-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()=="a":
                        a+=1
            except UnicodeDecodeError:
                continue
        fichero.close()
        return a
    def contarVocale(self):
        e=0
        fichero=open(self.ruta, "r", encoding='utf-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()=="e":
                        e+=1
            except UnicodeDecodeError:
                continue
        fichero.close()
        return e
    def contarVocali(self):
        i=0
        fichero=open(self.ruta, "r", encoding='utf-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()=="i":
                        i+=1
            except UnicodeDecodeError:
                continue
        fichero.close()
        return i
    def contarVocalo(self):
        o=0
        fichero=open(self.ruta, "r", encoding='utf-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()=="o":
                        o+=1
            except UnicodeDecodeError:
                continue
        fichero.close()
        return o
    def contarVocalu(self):
        u=0
        fichero=open(self.ruta, "r", encoding='utf-8')
        while fichero:
            try:
                char=fichero.read(1)
                if not char:
                    break
                else:
                    if char.lower()=="u":
                        u+=1
            except UnicodeDecodeError:
                continue
        fichero.close()
        return u

