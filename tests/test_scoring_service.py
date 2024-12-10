import unittest
from service.scoring_service import calculate_score


class TestScoringService(unittest.TestCase):
    def test_calculate_score_high_spec(self):
        laptop = {"CPU": "i7", "RAM": "16GB", "Penyimpanan": "1TB"}
        score = calculate_score(laptop)
        self.assertEqual(score, 9)

    def test_calculate_score_low_spec(self):
        laptop = {"CPU": "i3", "RAM": "4GB", "Penyimpanan": "256GB"}
        score = calculate_score(laptop)
        self.assertEqual(score, 3)

    def test_calculate_score_missing_field(self):
        laptop = {"CPU": "i7", "RAM": "8GB"}
        score = calculate_score(laptop)
        self.assertEqual(score, 0)


if __name__ == "__main__":
    unittest.main()
