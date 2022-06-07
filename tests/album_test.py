import unittest
from models.album import Album


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Lemonade", "R&B", "Beyonce")

    def test_album_has_name(self):
        self.assertEqual("Lemonade", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("R&B", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Beyonce", self.album.artist)
