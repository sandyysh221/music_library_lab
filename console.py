import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.music_repository as music_repository

# artist_repository.delete_all()
# music_repository.delete_all()

artist_1 = Artist("Bruno Mars")
artist_repository.save(artist_1)

artist_2 = Artist("My Bloody Valentine")
artist_repository.save(artist_2)

artist_3 = Artist("ODESZA")
artist_repository.save(artist_3)

artist_repository.select_all()

album_1 = Album("24K Magic", "R&B", artist_1)
music_repository.save(album_1)

album_2 = Album("Unorthodox Jukebox", "Pop", artist_1)
music_repository.save(album_1)

album_3 = Album("Loveless", "Shoegaze", artist_2)
music_repository.save(album_1)

music_repository.select_all()
music_repository.select(4)
artist_repository.select(7)

all_artists = artist_repository.select_all()
print(all_artists)

all_albums = music_repository.select_all()
print(all_albums)

pdb.set_trace()
