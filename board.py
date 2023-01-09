from square import Square, VALID_COLUMNS, VALID_ROWS
from piece import Color
import pawn

class Board(object):

    __squares = dict()

    def __create_board_squares(self):
        if not self.__squares:
            for row in VALID_ROWS:
                for col in VALID_COLUMNS:
                    key = col + str(row)
                    sq = Square(row=row, column=col)
                    self.__squares[key] = sq

    def __init_position_by_color(self, color):
        row = 1 if color == Color.White else 8
        self.squares()['A' + str(row)].set_piece(pawn.Rook(color))
        self.squares()['B' + str(row)].set_piece(pawn.Knight(color))
        self.squares()['C' + str(row)].set_piece(pawn.Bishop(color))
        self.squares()['D' + str(row)].set_piece(pawn.Queen(color))
        self.squares()['E' + str(row)].set_piece(pawn.King(color))
        self.squares()['F' + str(row)].set_piece(pawn.Bishop(color))
        self.squares()['G' + str(row)].set_piece(pawn.Knight(color))
        self.squares()['H' + str(row)].set_piece(pawn.Rook(color))
        for col in VALID_COLUMNS:
            row = 2 if color == Color.White else 7
            self.squares()[col + str(row)].set_piece(pawn.Pawn(color))

    def __init_positions(self):
        self.__init_position_by_color(Color.White)
        self.__init_position_by_color(Color.Black)

    def setup(self):
        self.__create_board_squares()
        self.__init_positions()
                
    def squares(self):
        return self.__squares

    def square(self, coordinate):
        assert coordinate in self.__squares.keys(), 'No such square {coordinate} on board'.format(coordinate=coordinate)
        return self.__squares[coordinate]

    def print_board(self):
        COLUUMN_SIZE = 13

        header = '   '
        body = ''

        for col in VALID_COLUMNS:
            header = header + col.ljust(COLUUMN_SIZE) + '|'
        header += '\n  '
        header += '=' * (len(VALID_COLUMNS) * (COLUUMN_SIZE + 1)) #+ '\n'

        for row in VALID_ROWS:
            body += str(row) + '| '

            for col in VALID_COLUMNS:
                key = '{col}{row}'.format(col=col, row=row)
                piece = self.__squares[key].piece()
                piece_name = piece.name() if piece else ' - '

                body += '{piece}'.format(piece=piece_name.ljust(COLUUMN_SIZE, ' ')) + '|'
            body += '\n  '
            body += '=' * (len(VALID_COLUMNS) * (COLUUMN_SIZE + 1)) + '\n'

        print(header)
        print(body)

    def make_move(self, from_square, to_square):
        from_square_obj = self.square(from_square)
        to_square_obj = self.square(to_square)

        piece_to_move = from_square_obj.piece()
        piece_taken = to_square_obj.piece()
        assert piece_to_move, 'No piece fond on square {square}. Can not make that move'.format(square=from_square_obj.name())
        to_square_obj.set_piece(piece_to_move)

        from_square_obj.set_piece(None)
        return piece_taken

if __name__ == '__main__':
    board = Board()
    board.setup()
    #board.print_board()
    board.make_move('E2', 'E4')
    board.print_board()