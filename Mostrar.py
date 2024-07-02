
def mostrar_playlist(playlist):
    for i, cancion in enumerate(playlist, 1):
        print(f"{i}. {cancion['cancion']} - {cancion['artista']}")