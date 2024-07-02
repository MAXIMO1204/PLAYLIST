def ordenar_playlist(playlist, clave):
    if clave == 'cancion':
        playlist.sort(key=lambda x: x['cancion'])
    elif clave == 'artista':
        playlist.sort(key=lambda x: x['artista'])
    else:
        print("Clave de ordenamiento no válida.")