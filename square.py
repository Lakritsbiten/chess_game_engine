VALID_ROWS = [1, 2, 3, 4, 5, 6, 7, 8]
VALID_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class Square(object):

    def __init__(self, row, column, piece=None):
        assert(row in VALID_ROWS)
        assert(column in VALID_COLUMNS)
        self.__row = row
        self.__column = column
        self.__name = '%s%d' % (self.__column, self.__row)
        self.__piece = piece

    def name(self):
        return self.__name 

    def piece(self):
        return self.__piece

    def set_piece(self, piece):
        self.__piece = piece
