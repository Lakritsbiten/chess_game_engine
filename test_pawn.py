import unittest
from pawn import Pawn, Queen
from piece import Color

class TestPieces(unittest.TestCase):

    def test_pawn(self):
        self.assertEqual('Black Pawn', Pawn(color=Color.Black).name())

    def test_queen(self):
        self.assertEqual('White Queen', Queen(color=Color.White).name())

if __name__ == '__main__':
    unittest.main()