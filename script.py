from hashlib import new
import socket
from datetime import date
class MainScript:
    def __init__(self, iter):
        self.iteracion = iter

    def fecha(self):
        fecha = date.today()
        fecha = fecha.strftime("%d/%m/%Y")
        print("Hoy es:", fecha)

    def hostname(self):
        print("Mi nombre de host es: ", socket.gethostname())

    def loop(self):
        print("Voy a iterar " + str(self.iteracion) + " veces")
        for x in range(self.iteracion):
            print("Iteracion: ", x)

if __name__== "__main__":
    main = MainScript(10)
    main.fecha()
    main.hostname()
    main.loop()