import json
from Utils import Utils

class Main:
    @staticmethod
    def iniciar():
        Utils.mostrar_artistas()
        numero_artista = int(input("Seleccione el número del artista a visualizar: "))
        Utils.mostrar_datos_artista(numero_artista)

if __name__ == "__main__":
    Main.iniciar()