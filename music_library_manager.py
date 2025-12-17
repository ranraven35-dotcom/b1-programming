songs = []
genre_count = {}

print("Welcome to Music Library Manager!\n")

for i in range(1, 6):
    print(f"Enter Song {i}:")
    song_name = input("  Song name: ")
    genre = input("  Genre: ")
    print()
    
    song_tuple = (song_name, genre)
    songs.append(song_tuple)
    
    genre_count[genre] = genre_count.get(genre, 0) + 1

print("=== YOUR MUSIC LIBRARY ===")
for index, (name, genre) in enumerate(songs, 1):
    print(f"{index}. {name} ({genre})")

print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")

most_popular = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular}")
