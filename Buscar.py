def buscar_en_playlist(playlist, keyword):
    resultados = []
    for cancion in playlist:
        if keyword.lower() in cancion['cancion'].lower() or keyword.lower() in cancion['artista'].lower():
            resultados.append(cancion)
    return resultados