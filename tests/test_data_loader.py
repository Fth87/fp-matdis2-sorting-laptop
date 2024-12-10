import unittest
from model.data_loader import load_data


class TestDataLoader(unittest.TestCase):
    def test_load_file(self):
        df = load_data()
        self.assertIsNotNone(df)
        self.assertFalse(df.empty)


if __name__ == "__main__":
    unittest.main()
