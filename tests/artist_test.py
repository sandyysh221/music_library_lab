import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Beyonce")

    def test_artist_has_name(self):
        self.assertEquals("Beyonce", self.artist.name)
