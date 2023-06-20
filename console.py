import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository  



album_repository.delete_all()
artist_repository.delete_all()



artist1 = Artist("Gigi Yuri")
artist_repository.save(artist1)

album1 = Album("Tomorrow", "Pop", artist1)
album_repository.save(album1)

album2 =Album("Never", "Rock", artist1)
album_repository.save(album2)

result = album_repository.select_all()
for task in result:
    print(task.__dict__)

pdb.set_trace()