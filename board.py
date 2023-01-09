from square import Square, VALID_COLUMNS, VALID_ROWS
from piece import Color
from board_configs import default_board, puzzle_2
from pawn import Rook, Pawn, King, Knight, Queen, Bishop

class Board(object):

    __squares = dict()

    def __init__(self, board_config=None):
        self.__create_board_squares()
        self.__board_from_config(board_config if board_config else default_board)

    def __create_board_squares(self):
        if not self.__squares:
            for row in VALID_ROWS:
                for col in VALID_COLUMNS:
                    key = col + str(row)
                    sq = Square(row=row, column=col)
                    self.__squares[key] = sq

    def __board_from_config(self, board_config):
        for sqr, piece_name in board_config.items():
            square_obj = self.square(sqr)
            color = Color[piece_name.split(' ')[0]]
            cls = eval(piece_name.split(' ')[1])
            piece = cls(color)
            square_obj.set_piece(piece)
    
    def squares(self):
        return self.__squares

    def square(self, pos):
        assert pos in self.__squares.keys(), 'No such square {pos} on board'.format(pos=pos)
        return self.__squares[pos]

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
    board = Board(puzzle_2)
    board.print_board()
