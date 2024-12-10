import unittest
from model.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_valid_file(self):
        df = load_data()
        self.assertIsNotNone(df)
        self.assertFalse(df.empty)

    def test_load_invalid_file(self):
        # Simulasikan file path yang salah
        global FILE_PATH
        FILE_PATH = './invalid_file.xlsx'
        df = load_data()
        self.assertIsNone(df)

if __name__ == '__main__':
    unittest.main()
