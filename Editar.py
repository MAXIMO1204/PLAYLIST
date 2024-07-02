
def editar_cancion(playlist, index, nueva_cancion, nuevo_artista):
    if not playlist:
        print("La playlist está vacía.")
    elif 0 < index <= len(playlist):
        playlist[index - 1]['cancion'] = nueva_cancion
        playlist[index - 1]['artista'] = nuevo_artista
        print("Canción editada correctamente.")
    else:
        print("Número de canción no encontrado en la playlist.")