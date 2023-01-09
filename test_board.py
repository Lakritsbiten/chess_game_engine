import unittest
from board import Board

class TestBoard(unittest.TestCase):
    __default_board = None
    __squares = None

    def setUp(self) -> None:
        self.__board = Board()
        self.__board.setup()
        self.__squares = self.__board.squares()  

    def test_setup_board_with_64_squares(self):
        self.assertEqual(64, len(self.__squares))

    def test_squares(self):
        self.assertTrue('B6' in self.__squares)
        self.assertFalse('A9' in self.__squares)
        self.assertIsNotNone(self.__squares['H7'])

    def test_white_rook(self):
        self.assertEqual('White Rook', self.__squares['A1'].piece().name())

    def test_black_king(self):
        self.assertEqual('Black King', self.__squares['E8'].piece().name())

    def test_make_move(self):
        piece_taken = self.__board.make_move('E2', 'E4')
        self.assertIsNone(piece_taken)
        self.assertEqual(self.__board.square('E4').piece().name(), 'White Pawn')

if __name__ == '__main__':
    unittest.main()