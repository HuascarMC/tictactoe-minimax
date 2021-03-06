import unittest
from models.abstracts.player import Player

class TestPlayer(unittest.TestCase):

    def test_cannot_instantiate(self):
        with self.assertRaises(TypeError):
            Player()


if __name__ == '__main__':
    unittest.main()
