from AbstractGame import AbstractGame
import random
from Player import Player
RED = 0
BLUE = 1
WHITE = 2
ORANGE = 3
BLACK = 4
TILES_NUMBER = 100


class Azul(AbstractGame):
    def __init__(self, number_of_players):
        self.gameId = 1
        self.gameName = "Azul"
        self.numberOfPlayers = number_of_players
        self.bag = []
        self.factoryDisplays = []
        self.middle = []
        self.players = []
        for tile_nb in range(TILES_NUMBER):
            if tile_nb < 20:
                self.bag.append(RED)
            elif (tile_nb < 40) and (tile_nb > 20):
                self.bag.append(BLUE)
            elif (tile_nb < 60) and (tile_nb > 40):
                self.bag.append(WHITE)
            elif (tile_nb < 80) and (tile_nb > 60):
                self.bag.append(ORANGE)
            elif (tile_nb < 100) and (tile_nb > 80):
                self.bag.append(BLACK)

        if self.numberOfPlayers == 2:
            self.factoryDisplaysNb = 5
        elif self.numberOfPlayers == 3:
            self.factoryDisplaysNb = 7
        elif self.numberOfPlayers == 4:
            self.factoryDisplaysNb = 9

    def initialize_game(self):
        print("Azul game selected")
        # Shuffle tiles bag
        random.shuffle(self.bag)
        print(self.bag)

    def prepare_turn(self):
        self.factoryDisplays.clear()
        self.middle.clear()
        for i in range(self.factoryDisplaysNb):
            fac_dis =[]
            for tileNb in range(4):
                fac_dis.append(self.bag[0])
                self.bag.pop(0)
            self.factoryDisplays.append(fac_dis)
        print(self.factoryDisplays)
        print(self.bag)

    def initialize_player(self):
        for player in range(self.numberOfPlayers):
            self.players.append(Player())

    def player_take_tiles(self, player_type):
        if player_type == 'human':
            while self.factory_display_not_empty() or self.middle_not_empty():
                for playerNb in range(self.numberOfPlayers):
                    if not (self.factory_display_not_empty() or self.middle_not_empty()):
                        break
                    while True:
                        print()
                        factoryDisplayNb = int(input("Take from factory display nb ----> "))
                        tilesType = int(input("Take tiles type ---->"))
                        rowTobeFilled = int(input("Select row of your board to be filled ----> "))
                        count_tiles = 0
                        find_one_more_tiles = False
                        if factoryDisplayNb < self.factoryDisplaysNb:
                            for tileNb in range(len(self.factoryDisplays[factoryDisplayNb])):
                                if self.factoryDisplays[factoryDisplayNb][tileNb] == tilesType:
                                    count_tiles += 1
                                    find_one_more_tiles = True
                        elif factoryDisplayNb == self.factoryDisplaysNb:
                            break
                        if find_one_more_tiles:
                            if (rowTobeFilled > 0) and (rowTobeFilled <= 5):
                                if rowTobeFilled == 1:
                                    check_row = self.players[playerNb].board.firstRowLeft
                                elif rowTobeFilled == 2:
                                    check_row = self.players[playerNb].board.secondRowLeft
                                elif rowTobeFilled == 3:
                                    check_row = self.players[playerNb].board.thirdRowLeft
                                elif rowTobeFilled == 4:
                                    check_row = self.players[playerNb].board.forthRowLeft
                                elif rowTobeFilled == 5:
                                    check_row = self.players[playerNb].board.fifthRowLeft
                               # if self.players[playerNb].board.take_tiles_allowed(tilesType, check_row):
                                break
                        else:
                            print("the type selected is not present")
                    if factoryDisplayNb <= (self.factoryDisplaysNb - 1):
                        tileToBeTaken = self.factoryDisplays[factoryDisplayNb]
                    else:
                        tileToBeTaken = self.middle
                    for tileNb in range(len(tileToBeTaken)):
                        if tileToBeTaken[tileNb] == tilesType:
                            if rowTobeFilled == 1:
                                if (len(self.players[playerNb].board.firstRowLeft) == \
                                        self.players[playerNb].board.firstRowLeft.maxlen) or \
                                    (len(self.players[playerNb].board.firstRowLeft) != 0 and \
                                     self.players[playerNb].board.firstRowLeft[0] != tilesType):
                                    self.players[playerNb].board.penaltyRow.append(tilesType)
                                else:
                                    self.players[playerNb].board.firstRowLeft.appendleft(tilesType)
                                tileToBeTaken[tileNb] = -1
                            elif rowTobeFilled == 2:
                                if (len(self.players[playerNb].board.secondRowLeft) == \
                                        self.players[playerNb].board.secondRowLeft.maxlen) or \
                                    (len(self.players[playerNb].board.secondRowLeft) != 0 and \
                                     self.players[playerNb].board.secondRowLeft[0] != tilesType):
                                    self.players[playerNb].board.penaltyRow.append(tilesType)
                                else:
                                    self.players[playerNb].board.secondRowLeft.appendleft(tilesType)
                                tileToBeTaken[tileNb] = -1
                            elif rowTobeFilled == 3:
                                if (len(self.players[playerNb].board.thirdRowLeft) == \
                                        self.players[playerNb].board.thirdRowLeft.maxlen) or \
                                    (len(self.players[playerNb].board.thirdRowLeft) != 0 and \
                                     self.players[playerNb].board.thirdRowLeft[0] != tilesType):
                                    self.players[playerNb].board.penaltyRow.append(tilesType)
                                else:
                                    self.players[playerNb].board.thirdRowLeft.appendleft(tilesType)
                                tileToBeTaken[tileNb] = -1
                            elif rowTobeFilled == 4:
                                if (len(self.players[playerNb].board.forthRowLeft) == \
                                        self.players[playerNb].board.forthRowLeft.maxlen) or \
                                    (len(self.players[playerNb].board.forthRowLeft) != 0 and \
                                     self.players[playerNb].board.forthRowLeft[0] != tilesType):
                                    self.players[playerNb].board.penaltyRow.append(tilesType)
                                else:
                                    self.players[playerNb].board.forthRowLeft.appendleft(tilesType)
                                tileToBeTaken[tileNb] = -1
                            elif rowTobeFilled == 5:
                                if (len(self.players[playerNb].board.fifthRowLeft) == \
                                        self.players[playerNb].board.fifthRowLeft.maxlen)or \
                                    (len(self.players[playerNb].board.fifthRowLeft) != 0 and \
                                     self.players[playerNb].board.fifthRowLeft[0] != tilesType):
                                    self.players[playerNb].board.penaltyRow.append(tilesType)
                                else:
                                    self.players[playerNb].board.fifthRowLeft.appendleft(tilesType)
                                tileToBeTaken[tileNb] = -1
                        else:
                            if factoryDisplayNb != self.factoryDisplaysNb:
                                self.middle.append(self.factoryDisplays[factoryDisplayNb][tileNb])
                                self.factoryDisplays[factoryDisplayNb][tileNb] = -1
                    print(self.factoryDisplays)
                    print(self.players[playerNb].board.print_board())
                    print(self.middle)

    def factory_display_not_empty(self):
        is_empty = False
        for i in range(len(self.factoryDisplays)):
            for j in range(len(self.factoryDisplays[0])):
                if self.factoryDisplays[i][j] != -1:
                    is_empty = True
        return is_empty

    def middle_not_empty(self):
        is_empty = False
        for i in range(len(self.middle)):
            if self.middle[i] != -1:
                is_empty = True
        return is_empty

