# Importamos el módulo random para generar selecciones aleatorias
import random

# Lista de diccionarios que contiene información de canciones: 
# título, artista, marca de tiempo, usuario y país
songs = [
    {"song": "Vampire", "artist": "Olivia Rodrigo", "timestamp": 1590851957, "user": "Lorena", "country": "Spain"},
    {"song": "Cruel Summer", "artist": "Taylor Swift", "timestamp": 1590851960, "user": "Roberto", "country": "USA"},
    {"song": "What Was I Made For?", "artist": "Billie Eilish", "timestamp": 1590851961, "user": "Inés", "country": "Canada"},
    {"song": "Flowers", "artist": "Miley Cyrus", "timestamp": 1590851963, "user": "Miguel", "country": "Colombia"},
    {"song": "Paint The Town Red", "artist": "Doja Cat", "timestamp": 1590851965, "user": "Enrique", "country": "Germany"},
    {"song": "Calm Down", "artist": "Rema", "timestamp": 1590851966, "user": "Miriam", "country": "France"},
    {"song": "Bad Habit", "artist": "Ed Sheeran", "timestamp": 1590851967, "user": "Pablo", "country": "Canada"}
]

# Número total de líneas que queremos generar
total_lines = 100000

# Abrimos un archivo llamado 'song.txt' en modo escritura
with open('reduced_song_list.txt', 'w') as file:
    # Iteramos el número de veces especificado en total_lines
    for i in range(total_lines):
        # Seleccionamos una canción aleatoria de la lista
        song = random.choice(songs)
        # Escribimos la información de la canción en formato CSV
        file.write(f"{song['song']},{song['artist']},{song['timestamp']},{song['user']},{song['country']}\n")

        # Cada 1000 líneas, mostramos un mensaje de progreso
        if i % 1000 == 0:
            print(f'{i} lines written')

# Mostramos mensaje de finalización
print('Done!')