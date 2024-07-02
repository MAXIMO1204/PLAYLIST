def eliminar_cancion(playlist, index):
    if not playlist:
        print("La playlist está vacía.")
    elif 0 < index <= len(playlist):
        deleted_song = playlist.pop(index - 1)
        print(f"La canción '{deleted_song['cancion']}' ha sido eliminada de la playlist.")
    else:
        print("Número de canción no encontrado en la playlist.")