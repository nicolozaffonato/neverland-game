import time
import datetime

# Game configuration

class GameConfiguration():

    def __init__(self):
        pass
    time_zone = "day"
    game_over = False
    druid_name = "Novac"
    potion_shop_open = False
    world_place = ["Tuna Village", "Forbidden Forest", "Dark Tower"]
    tuna_place = ["Gunsmith", "Merchant", "Potion Shop", "Druid Novac", "Port", "Go to World"]

    # function to print messages with a 2 second delay
    def print_pause_config(self, message, seconds=2):
        print(message)
        time.sleep(seconds)

    def credits(self, gameover):

        if gameover:
            self.print_pause_config("\n\n         //  Congratulations on completing the game  //")
            self.print_pause_config("\n\n\n\n___________________ DISCLAIMER ____________________")
            self.print_pause_config("\n>> This game is a pure work of fiction,")
            self.print_pause_config(">> We strictly followed the 'Player-Monster-Coexist-World"
                        " Peace' rule in this game\n\n")
            self.print_pause_config("___________________ CREDITS ____________________")
            self.print_pause_config("\nThis game was developed by and\nsole property of "
                        "// 'Nicolo\' Zaffonato' //\n")
            self.print_pause_config("\n\n")
            self.print_pause_config("Thanks for playing the game, wait of the next sequel and expansion....//")
        else:
            self.print_pause_config("\n\n         //  Gameover. If you saved the game before, you can load the game and you can try again.  //")

    def get_gameover(self):
        return self.game_over

class GunsmithConfiguration():
    def __init__(self):
        pass

    gunsmith_ok = False
    first_to_gunsmith = True
    list_action_gunsmith = ["Go to Tuna", "Buy Item", "Sell Item", "Why has our world been destroyed?", "Why is Novac so lonely?"]
    date_generate_item = ""
    rarity_item = ["base", 'silver', 'epic', 'legendary']
    list_weapon_item = ["sword", 'dagger', 'stick', 'arch', 'ax']
    list_amulet = ["add health amulet", 'more damage amulet', 'more shield amulet']
    list_armor = ["add health amulet", 'more damage amulet', 'more shield amulet']
    gunsmith_item = []


class PlayerConfiguration():

    def __init__(self):
        pass

    bag = []
    player_class = ["elemental wizard", "nature wizard", "druid wizard"]
    player_class_chosen = ''
    player = "New_Game"
    attack = 10
    attack_speed = 10
    player_speed = 10
    player_defence = 10
    shield = 10
    player_health = 100
    player_max_health = 100

    magic_level = 0
    experience = 0
    gold = 50

    general_item = {
        "name" : "",
        "type_item" : "",
        "type_weapon" : "",
        "attack" : 0,
        "defence" : 0,
        "gold" : 0,
        "rarity" : "",
        "version" : "base"
    }

    def level_increse(self, experience):

        threshold_level = 100 + self.magic_level*50
        self.set_experience(experience=experience)

        if self.get_experience() >= threshold_level:
            self.magic_level = self.magic_level + 1
            return True
        else:
            return False

    def set_experience(self, experience=0):
        self.experience = self.experience + experience

    def get_experience(self):
        return self.experience

    def set_gold(self, gold=0):
        self.gold = self.gold + gold

    def get_gold(self):
        return self.gold
