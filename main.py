import GameFactory

if __name__ == '__main__':

    gameFactory = GameFactory.PlayGame()
    game = gameFactory.create(game_name="Azul", number_of_players=3)
    game.initialize_game()
    game.initialize_player()
    game.prepare_turn()
    game.player_take_tiles('human')
    game.calculate_points()
