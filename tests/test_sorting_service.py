import unittest
from service.sorting_service import merge_sort

class TestSortingService(unittest.TestCase):
    def test_merge_sort(self):
        laptops = [
            {'Merek': 'LaptopA', 'Skor': 5},
            {'Merek': 'LaptopB', 'Skor': 7},
            {'Merek': 'LaptopC', 'Skor': 3}
        ]
        merge_sort(laptops, 0, len(laptops) - 1)
        self.assertEqual(laptops, [
            {'Merek': 'LaptopB', 'Skor': 7},
            {'Merek': 'LaptopA', 'Skor': 5},
            {'Merek': 'LaptopC', 'Skor': 3}
        ])

if __name__ == '__main__':
    unittest.main()
