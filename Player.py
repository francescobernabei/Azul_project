import collections


class Player:
    def __init__(self):
        self.board = Board()

    def set_name_surname(self, name, surname):
        self.name = name
        self.surname = surname


class Board:
    def __init__(self):
        self.firstRowLeft = collections.deque(maxlen=1)
        self.secondRowLeft = collections.deque(maxlen=2)
        self.thirdRowLeft = collections.deque(maxlen=3)
        self.forthRowLeft = collections.deque(maxlen=4)
        self.fifthRowLeft = collections.deque(maxlen=5)
        self.firstRowRight = collections.deque(maxlen=1)
        self.secondRowRight = collections.deque(maxlen=2)
        self.thirdRowRight = collections.deque(maxlen=3)
        self.forthRowRight = collections.deque(maxlen=4)
        self.fifthRowRight = collections.deque(maxlen=5)
        self.penaltyRow = []

    def print_board(self):
        print(self.firstRowLeft)
        print(self.secondRowLeft)
        print(self.thirdRowLeft)
        print(self.forthRowLeft)
        print(self.fifthRowLeft)
        print(self.penaltyRow)

    def take_tiles_allowed(self, tile_type, row_selected):
        if len(row_selected) != 0:
            if (tile_type != row_selected[0]) and (len(row_selected) < row_selected.maxlen):
                print("Wrong type tiles selected")
                return False
            else:
                return True
        return True
