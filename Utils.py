import json

class Utils:
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
    def mostrar_artistas():
        datos = Utils.cargar_datos()
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
    def mostrar_datos_artista(numero_artista):
        datos = Utils.cargar_datos()
        artistas = Utils.obtener_artistas()
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

    @staticmethod
    def mostrar_albums():
        datos = Utils.cargar_datos()
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
    def mostrar_canciones_artista(numero_artista):
        datos = Utils.cargar_datos()
        artistas = Utils.obtener_artistas()
        if datos and artistas:
            if 1 <= numero_artista <= len(artistas):
                artista_seleccionado = artistas[numero_artista - 1]
                for sello in datos['sellos_discograficos']:
                    for artista in sello['artistas']:
                        if artista['nombre'] == artista_seleccionado:
                            print(f"Canciones del artista '{artista['nombre']}':")
                            for cancion in artista['canciones']:
                                print(f"- {cancion['nombre']} ({cancion['fecha']}) - Duración: {cancion['duracion']}")
                            return
                print("El artista seleccionado no fue encontrado.")
            else:
                print("El número del artista seleccionado es inválido.")
        else:
            print("No se pudieron cargar los datos o no hay artistas para seleccionar.")    

    @staticmethod
    def mostrar_albums_artista(numero_artista):
        datos = Utils.cargar_datos()
        artistas = Utils.obtener_artistas()
        if datos and artistas:
            if 1 <= numero_artista <= len(artistas):
                artista_seleccionado = artistas[numero_artista - 1]
                for sello in datos['sellos_discograficos']:
                    for artista in sello['artistas']:
                        if artista['nombre'] == artista_seleccionado:
                            if 'albumes' in artista and artista['albumes']:
                                print(f"Álbumes del artista '{artista['nombre']}':")
                                for album in artista['albumes']:
                                    print(f"- {album['nombre']} ({album['fecha_publicacion']})")
                            else:
                                print(f"No se encontraron álbumes para el artista '{artista['nombre']}'.")
                            return
                print("El artista seleccionado no fue encontrado.")
            else:
                print("El número del artista seleccionado es inválido.")
        else:
            print("No se pudieron cargar los datos o no hay artistas para seleccionar.")   

    @staticmethod
    def obtener_artistas():
        datos = Utils.cargar_datos()
        if datos:
            artistas = []
            for sello in datos['sellos_discograficos']:
                for artista in sello['artistas']:
                    artistas.append(artista['nombre'])
            if artistas:
                return artistas
            else:
                print("No se encontraron artistas.")
                return None
        else:
            print("No se pudieron cargar los datos.")
            return None
        

    @staticmethod
    def menu():
        while True:
            print("HARMONY-LIB")
            print("Menú:")
            print("1. Ver las canciones de un artista")
            print("2. Ver los álbumes de un artista")
            print("3. Ver generos musicales")
            print("0. Salir")
            
            opcion = input("Ingrese el número de la opción que desea: ")
            
            if opcion == '1':
                Utils.mostrar_artistas()
                numero_artista = int(input("Seleccione el número del artista para ver sus canciones: "))
                Utils.mostrar_canciones_artista(numero_artista)
            elif opcion == '2':
                Utils.mostrar_artistas()
                num_artista = int(input("Seleccione el número para ver los álbumes del artista: "))
                Utils.mostrar_albums_artista(num_artista)
            elif opcion =='3':
                 Utils.listar_generos()
                    
            elif opcion == '0':
                print("Saliendo del menú.")
                break
            else:
                print("Opción no válida. Ingrese un número válido de opción.")

    @staticmethod
    def listar_generos():
        datos = Utils.cargar_datos()
        if datos:
            generos = set()  # Utilizamos un conjunto para almacenar géneros únicos
            for sello in datos['sellos_discograficos']:
                for artista in sello['artistas']:
                    for cancion in artista['canciones']:
                        generos.add(cancion['genero'])  # Agregamos el género al conjunto

            if generos:
                print("Géneros presentes en el JSON:")
                for genero in generos:
                    print(f"- {genero}")
            else:
                print("No se encontraron géneros.")
        else:
            print("No se pudieron cargar los datos.")                