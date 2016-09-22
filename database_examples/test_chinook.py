import unittest
import sqlite3
import os.path

class Test_00_ChinkookDBPresence(unittest.TestCase):

    def test_00_is_db_present(self):
        self.assertTrue(os.path.isfile("chinook.db"))
        connection = sqlite3.connect("chinook.db")
        #cursor = connection.cursor()
        
class Test_01_ChinkookDB(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect("chinook.db")
            
    def test_00_has_tables(self):
        cursor = self.connection.cursor()
        for table in ['Artist','Playlist',
            'Album','PlaylistTrack','Track','MediaType','Genre']:
            cursor.execute('SELECT * FROM ' + table)

    def test_01_artist_has_correct_columns(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from artist")
        column_names = [item[0].lower() for item in list(cursor.description)]
        for column in ['ArtistId','Name']:
            self.assertTrue(column.lower() in column_names)

if __name__ == "__main__":
   unittest.main(verbosity=2)

