import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("Tomorrow", "Pop", "Gigi Yuri")
    
    def test_album_has_title(self):
        self.assertEqual("Tomorrow", self.album.title)
        
        
    def test_album_has_genre(self):
        self.assertEqual("Pop", self.album.genre)
       
        
    def test_task_has_artist(self):
        self.assertEqual("Gigi Yuri", self.album.artist)

    
    
   