from Agregar import*
from Buscar import*
from Editar import*
from Eliminar import*
from Guardar import*
from Mostrar import*
from Ordenar import*
from Vaciar import*


def main():
    playlist = []
    archivo = 'Archivos\Playlist de Ramiro.txt'

    while True:
        print("\n1. AGREGAR CANCION")
        print("2. MOSTRAR PLAYLIST")
        print("3. EDITAR CANCION")
        print("4. ELIMINAR CANCION")
        print("5. VACIAR PLAYLIST")
        print("6. GUARDAR PLAYLIST")
        print("7. BUSCAR REGISTRO")
        print("8. ORDENAR PLAYLIST")
        print("9. SALIR")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cancion = input("Ingrese el nombre de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            agregar_cancion(playlist, cancion, artista)
        elif opcion == '2':
            print("\nPlaylist:")
            mostrar_playlist(playlist)
        elif opcion == '3':
            index = int(input("Ingrese el número de la canción que desea editar: "))
            nueva_cancion = input("Ingrese el nuevo nombre de la canción: ")
            nuevo_artista = input("Ingrese el nuevo nombre del artista: ")
            editar_cancion(playlist, index, nueva_cancion, nuevo_artista)
        elif opcion == '4':
            index = int(input("Ingrese el número de la canción que desea eliminar: "))
            eliminar_cancion(playlist, index)
        elif opcion == '5':
            vaciar_playlist(playlist)
        elif opcion == '6':
            guardar_playlist(playlist, archivo)
            print(f"Playlist guardada en {archivo}")
        elif opcion == '7':
            keyword = input("Ingrese la palabra clave a buscar: ")
            resultados = buscar_en_playlist(playlist, keyword)
            if resultados:
                print("Resultados de la búsqueda:")
                mostrar_playlist(resultados)
            else:
                print("No se encontraron resultados para la palabra clave ingresada.")
        elif opcion == '8':
            clave_orden = input("¿Como quieres ordenar la playlist? (Cancion / Artista): ").lower()
            ordenar_playlist(playlist, clave_orden)
            print("Playlist ordenada correctamente.")
            
        elif opcion == '9':
            print("UD SALIO DEL PROGRAMA.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
