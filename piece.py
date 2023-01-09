from enum import Enum

class Color(Enum):
    White = 1
    Black = 2


class Piece(object):

    def __init__(self, color):
        self.__color = color

    def color(self):
        return self.__color

    def name(self):
        return '{color} {piece_type}'.format(color=self.color().name, piece_type=self.__class__.__name__)

    def possible_next_positions(self):
        raise NotImplementedError('Base class %s called. Use sub class instead' % self.__class__.__name__)

