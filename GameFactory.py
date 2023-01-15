import Games
import AbstractGame


class PlayGame:

    @staticmethod
    def create(game_name, number_of_players):
        try:
            if game_name == "Azul":
                return Games.Azul(number_of_players)
            raise AssertionError("Game still not developed!")
        except AssertionError as e:
            print(e)
