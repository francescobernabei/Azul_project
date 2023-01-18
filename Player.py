import collections

RED = 0
BLUE = 1
WHITE = 2
ORANGE = 3
BLACK = 4
TILES_NUMBER = 100

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
        self.penaltyRow = []
        self.rightPart = []
        self.firstRowRight = {BLUE: False,
                              ORANGE: False,
                              RED: False,
                              BLACK: False,
                              WHITE: False
                              }
        self.secondRowRight = {WHITE: False,
                               BLUE: False,
                               ORANGE: False,
                               RED: False,
                               BLACK: False
                               }
        self.thirdRowRight = {BLACK: False,
                              WHITE: False,
                              BLUE: False,
                              ORANGE: False,
                              RED: False
                              }
        self.fourthRowRight = {RED: False,
                               BLACK: False,
                               WHITE: False,
                               BLUE: False,
                               ORANGE: False
                               }
        self.fifthRowRight = {ORANGE: False,
                              RED: False,
                              BLACK: False,
                              WHITE: False,
                              BLUE: False
                              }
        self.rightPart.append(self.firstRowRight)
        self.rightPart.append(self.secondRowRight)
        self.rightPart.append(self.thirdRowRight)
        self.rightPart.append(self.fourthRowRight)
        self.rightPart.append(self.fifthRowRight)

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

    def check_full_rows(self):
        if len(self.firstRowLeft) == self.firstRowLeft.maxlen :
            self.rightPart[0][self.firstRowLeft[0]] = True
            for elem in range(len(self.firstRowLeft)):
                self.firstRowLeft[elem] = -1
        if len(self.secondRowLeft) == self.secondRowLeft.maxlen :
            self.rightPart[1][self.secondRowLeft[0]] = True
            for elem in range(len(self.secondRowLeft)):
                self.secondRowLeft[elem] = -1
        if len(self.thirdRowLeft) == self.thirdRowLeft.maxlen :
            self.rightPart[2][self.thirdRowLeft[0]] = True
            for elem in range(len(self.thirdRowLeft)):
                self.thirdRowLeft[elem] = -1
        if len(self.forthRowLeft) == self.forthRowLeft.maxlen :
            self.rightPart[3][self.forthRowLeft[0]] = True
            for elem in range(len(self.forthRowLeft)):
                self.forthRowLeft[elem] = -1
        if len(self.fifthRowLeft) == self.fifthRowLeft.maxlen :
            self.rightPart[4][self.fifthRowLeft[0]] = True
            for elem in range(len(self.fifthRowLeft)):
                self.fifthRowLeft[elem] = -1
        self.print_board()