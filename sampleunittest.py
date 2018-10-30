import unittest
from coin_toss import flip_coin

class FlipCoinTests(unittest.TestCase):
    def test_flip_coin(self):
        self.assertIn(flip_coin(), ("Heads", "Tails"))
    
    def test_failing_test(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()