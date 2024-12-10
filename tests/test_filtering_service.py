import unittest
import pandas as pd
from service.filtering_service import get_price_range, filter_laptops


class TestFilteringService(unittest.TestCase):
    def setUp(self):
        data = {
            "Merek": ["LaptopA", "LaptopB"],
            "Model": ["Model1", "Model2"],
            "Harga": [3000000, 15000000],
            "CPU": ["i5", "i7"],
            "RAM": ["8GB", "16GB"],
            "Penyimpanan": ["512GB", "1TB"],
        }
        self.df = pd.DataFrame(data)

    def test_get_valid_price_range(self):
        price_range = get_price_range("2")
        self.assertEqual(price_range, (2500000, 5000000))

    def test_get_invalid_price_range(self):
        price_range = get_price_range("10")
        self.assertIsNone(price_range)

    def test_filter_laptops_valid_range(self):
        filtered = filter_laptops(self.df, (2500000, 5000000))
        self.assertEqual(len(filtered), 1)

    def test_filter_laptops_empty_range(self):
        filtered = filter_laptops(self.df, (0, 1000000))
        self.assertTrue(filtered.empty)


if __name__ == "__main__":
    unittest.main()
