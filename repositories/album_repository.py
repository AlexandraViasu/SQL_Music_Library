from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = """INSERT INTO album (title, genre, artist_id) 
            VALUES (%s, %s, %s)
            RETURNING id"""
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    first_result = results[0]
    id = first_result["id"]
    album.id =id

def select(id):
    album = None
    sql = """SELECT * FROM album 
          WHERE id = %s"""
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result["title"], result["genre"], artist, result["id"])
    return album    

def select_all():  
    albums = [] 

    sql = "SELECT * FROM album"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)


