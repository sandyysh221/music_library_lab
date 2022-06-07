import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.music_repository as music_repository

artist_1 = Artist("Bruno Mars")
artist_repository.save(artist_1)
artist_repository.select_all()

album_1 = Album("24K Magic", "R&B", "Bruno Mars")
music_repository.save(album_1)
music_repository.select_all()

artist_repository.delete_all()
music_repository.delete_all()
pdb.set_trace()
