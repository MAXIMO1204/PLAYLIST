
def guardar_playlist(playlist, archivo):
    with open(archivo, 'w', encoding='utf-8') as file:
        file.write(" CANCIONES DE RAMIRO\n")
        file.write("*********************\n")
        for cancion in playlist:
            file.write(f"Canción: {cancion['cancion']}\n")
            file.write(f"Artista: {cancion['artista']}\n")
            file.write("\n")
