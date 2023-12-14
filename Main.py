import json

class Main:
    @staticmethod
    def cargar_datos():
        try:
            with open('ejemplo.json') as file:
                datos = json.load(file)
                return datos
        except FileNotFoundError:
            print("El archivo no se encontró.")
            return None

    @staticmethod
    def iniciar():
        datos = Main.cargar_datos()
        if datos:
           
            print("Datos cargados correctamente:")
            print(datos)
            
        else:
            print("No se pudieron cargar los datos.")

    @staticmethod
    def mostrar_artistas():
        datos = Main.cargar_datos()
        if datos:
            artistas = []
            for sello in datos['sellos_discograficos']:
                for artista in sello['artistas']:
                    artistas.append(artista['nombre'])
            if artistas:
                print("Los artistas presentes en el JSON son:")
                for i, artista in enumerate(artistas, start=1):
                    print(f"{i}. {artista}")
                return artistas
            else:
                print("No se encontraron artistas.")
                return None
        else:
            print("No se pudieron cargar los datos.")
            return None

    @staticmethod
    def mostrar_albums():
        datos = Main.cargar_datos()
        if datos:
            albums = []
            for sello in datos['sellos_discograficos']:
                for artista in sello['artistas']:
                    for album in artista.get('albumes', []):
                        albums.append(album['nombre'])
            if albums:
                print("Los álbumes presentes en el JSON son:")
                for album in albums:
                    print(album)
            else:
                print("No se encontraron álbumes.")
        else:
            print("No se pudieron cargar los datos.")        

    @staticmethod
    def mostrar_datos_artista(numero_artista):
        datos = Main.cargar_datos()
        artistas = Main.mostrar_artistas()
        if datos and artistas:
            if 1 <= numero_artista <= len(artistas):
                artista_seleccionado = artistas[numero_artista - 1]
                for sello in datos['sellos_discograficos']:
                    for artista in sello['artistas']:
                        if artista['nombre'] == artista_seleccionado:
                            print(f"Datos del artista '{artista['nombre']}':")
                            print(f"ID: {artista['id']}")
                            print("Canciones:")
                            for cancion in artista['canciones']:
                                print(f"- {cancion['nombre']}")
                            print("Álbumes:")
                            for album in artista.get('albumes', []):
                                print(f"- {album['nombre']} ({album['fecha_publicacion']})")
                            return
                print("El artista seleccionado no fue encontrado.")
            else:
                print("El número del artista seleccionado es inválido.")
        else:
            print("No se pudieron cargar los datos o no hay artistas para seleccionar.")

if __name__ == "__main__":
    Main.iniciar()
    artistas = Main.mostrar_artistas()
    if artistas:
            numero_artista = int(input("Seleccione el número del artista a visualizar: "))
            Main.mostrar_datos_artista(numero_artista)