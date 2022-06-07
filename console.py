import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository

artist_1 = Artist("Bruno Mars")
artist_repository.save(artist_1)
artist_repository.select_all()

pdb.set_trace()
