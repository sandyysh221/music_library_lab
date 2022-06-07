from db.run_sql import run_sql
from models.album import Album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row["title"], row["genre"], row["artist"], row["id"])
        albums.append(album)
    return albums


def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)
