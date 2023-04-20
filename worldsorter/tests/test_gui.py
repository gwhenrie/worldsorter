from unittest import TestCase 
from gui import ensure_file_type

class test_Main(TestCase):
    """Test functions contained in the Main class in gui."""
    def test_ensure_file_type(self):
        """Test the ensure_file_type function."""
        with self.subTest("Test with filePath not a string."):
            try:
                ensure_file_type(3, 'blah')
            except TypeError as e:
                error = e
            self.assertEqual('filePath must be a string.', str(error)) 

        with self.subTest("Test with fileType not a string."):
            try:
                ensure_file_type('blah', 3)
            except TypeError as e:
                error = e 
            self.assertEqual('fileType must be a string.', str(error)) 

        with self.subTest("Test if the file has no file type."):
            filePath = 'blah'
            fileType = 'db'
            self.assertEqual(f"{filePath}.{fileType}", ensure_file_type(filePath, fileType))

        with self.subTest("Test if the file has the wrong file type."):
            filePath = 'blah.txt'
            fileType = 'db'
            self.assertEqual("blah.db", ensure_file_type(filePath, fileType)) 

        with self.subTest("Test if file already has the correct type."):
            filePath = 'blah.db'
            fileType = 'db'
            self.assertEqual(filePath, ensure_file_type(filePath, fileType))
