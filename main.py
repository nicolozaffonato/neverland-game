from neverland import NeverlandGame
from configuration import GameConfiguration, GunsmithConfiguration, PlayerConfiguration
from datetime import datetime, timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = NeverlandGame()
    gun = GunsmithConfiguration()
    game_configuration = GameConfiguration()

    # TODO: Implemenetare l'upload del file di salvataggio, la scelta se fare un nuovo gioco e cominciare da un salvataggio

    new_game = True
    game.adventure_game(new_game)
    game_configuration.credits(game_configuration.get_gameover())

