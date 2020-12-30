import time
import random
from configuration import GameConfiguration, PlayerConfiguration, GunsmithConfiguration
import random
import datetime

player_config = PlayerConfiguration()
game_config = GameConfiguration()
gunsmith_config = GunsmithConfiguration()

class NeverlandGame():

    # function to print messages with a 2 second delay
    def print_pause(self, message, seconds=2):
        print(message)
        time.sleep(seconds)
    
    # function to display the 'items in the list' with a serial number
    def list_serial(self, list):
        for index in range(len(list)):
            self.print_pause(str(index+1) + ". " + list[index], 1)
        self.print_pause("\n", 1)
        return ""
    
    
    # function to remove a specific item from a list
    def remove_item(self, list, item):
        new_list = []
        for index in range(len(list)):
            if list[index] != item:
                new_list.append(list[index])
        list = new_list
        return list
    
    
    # function to increase player's health within the limit of 100
    def health_increase(self, num):
        global player_health
        if player_health < 100 and player_health > 0:
            player_health += num
            if player_health > 100:
                player_health = 100
            return player_health
    
    
    # function to decrease player's health within the threshold of 0
    def health_decrease(self, health, num):
        if health > 0:
            health += num
            if health < 0:
                health = 0
            return health
        else:
            health = 0
            return health
    
    def check_upgrade_level(self, experience):

        level = player_config.level_increse(experience=experience)
        if level:
            self.print_pause("\n*****************", 0)
            self.print_pause("!!!!! You leveled up !!!!!", 0)
            self.print_pause("Your magic level is increasing more and more. Because of this, your stats will also increase.", 0)
            self.print_pause("*****************", 2)

            self.set_stats()
    
    
    # # A branch sequence to the funstion 'adventure_game'
    # def tuna_village():
    #     # trigger to end the game from the function 'fight_sequence'
    #     if game_over == "activate":
    #         self.print_pause("\n\nGame over. Try again ........")
    #         exit()
    #     # village intro
    #     # player's choice
    #     self.print_pause("\nwelcome to the fabled village of Yorkshire")
    #     self.print_pause("Where would you like to venture into:")
    #     # displays list of village locations in a serial list
    #     village_choice = input(list_serial(village_locations)).lower()
    #     # if player decides to enter into the traven
    #     if "traven" in village_choice:
    #         self.print_pause("\nYou have entered Traven to make business")
    #         shop()
    #     # if player decides to enter into the Inn
    #     elif "inn" in village_choice:
    #         self.print_pause("\nYou have checked into an Inn")
    #         inn()
    #     # if player decides to enter into the contest grounds
    #     elif "contest" in village_choice:
    #         self.print_pause("\nYou head towards the contest grounds with curiosity")
    #         contest_grounds()
    #     # if player decides to enter into the forest
    #     elif "forest" in village_choice:
    #         forest()
    #     # if player decides to enter into the cave
    #     elif "cave" in village_choice:
    #         self.print_pause("You step into the darkness of cave courageously !!")
    #         self.print_pause("The cave is a labyrinth of multiple partitions")
    #         cave()
    #     # if player decides to enter into the fort
    #     elif "fort" in village_choice:
    #         fort()
    #     # if player decides to enter into the secret passage
    #     elif "secret" in village_choice and "Secret Passage" in village_locations:
    #         secret_passage()
    #     # condition to deal with unrecognized input
    #     else:
    #         self.print_pause("The place you are looking for does not exist "
    #                     "in this village")
    #         village()
    
    def set_global_variable(self, new_game):
    
        if not new_game:
            # TODO: Settare i parametri presi dal file
            pass
    
    def set_class_variable(self, class_wizard):
        if class_wizard == "elemental wizard":
            PlayerConfiguration.attack = PlayerConfiguration.attack + 50
            PlayerConfiguration.attack_speed = PlayerConfiguration.attack_speed + 50
        elif class_wizard == "nature wizard":
            PlayerConfiguration.player_defence = PlayerConfiguration.player_defence + 50
            PlayerConfiguration.shield = PlayerConfiguration.shield + 50
        elif class_wizard == "druid wizard":
            PlayerConfiguration.player_health = PlayerConfiguration.player_health + 50
            PlayerConfiguration.player_max_health = PlayerConfiguration.player_max_health + 50
    
    def set_stats(self):
        random_value = random.randint(1, 10)
        class_value = 0
        constant_value_1 = 5
        constant_value_2 = 7
        constant_value_3 = 10
    
        PlayerConfiguration.attack = PlayerConfiguration.attack + constant_value_1 + random_value
        PlayerConfiguration.attack_speed = PlayerConfiguration.attack_speed + constant_value_1 + random_value
        PlayerConfiguration.player_defence = PlayerConfiguration.player_defence + constant_value_2 + random_value
        PlayerConfiguration.player_speed = PlayerConfiguration.player_speed + constant_value_1 + random_value
        PlayerConfiguration.shield = PlayerConfiguration.shield + constant_value_2 + random_value
        PlayerConfiguration.player_health = PlayerConfiguration.player_health + constant_value_3 + random_value
        PlayerConfiguration.player_max_health = PlayerConfiguration.player_max_health + constant_value_3 + random_value
    
    def launch_splash_screen(self):
        # TODO: Implementare lo splash screen con un po' di logo
        pass
    
    def launch_story(self):
        self.print_pause("YOU: Oh Oh Oh... Do you feel that noise?")
        self.print_pause("YOUR FRIEND: What noise? I didn't hear it, I thought it was you.")
        self.print_pause("YOU: I... The noise comes from outside.", 3)
    
        self.print_pause("\nYOU: Check what's out there.")
        self.print_pause("YOU: Oh no, the looters of magic. it is better to hide until the attack ends.")
        self.print_pause("YOUR FRIEND: I go out. I have to help my country. You stay hidden, you are still an apprentice.")
        self.print_pause("Boom!", 1)
        self.print_pause("Boom!", 1)
        self.print_pause("Boom!", 1)
        self.print_pause("YOU: No my friend, don't leave me.")
        self.print_pause("YOU: I better stay hidden until the attack ends.", 5)
    
        self.print_pause("\nAfter a long battle your hometown was destroyed. "
                    "Only a few pieces remained and there remained you, "
                    "full of fear and full of vengeance but with little magical ability.", 5)
        self.print_pause("After a few hours he found you an old druid named " + GameConfiguration.druid_name)
    
    def intro_Tuna_city(self):
        self.print_pause("\nYou are now in the city of Tuna.", 3)
        self.print_pause("This city was built many years ago and still remains the most important city in the wizarding world.", 3)
        self.print_pause("Here you will learn to be a great magician.", 5)
        self.print_pause("Please enter your wizard class form the list below")
    
        check_class = False
        player_class = []
        while not check_class:
            self.print_pause("What is your wizard class?")
            player_class = input(self.list_serial(PlayerConfiguration.player_class)).lower()
    
            check_class = player_class in PlayerConfiguration.player_class
    
        self.set_class_variable(player_class)
    
        self.print_pause("\nOh well, the chosen class is: " + player_class)
        PlayerConfiguration.player_class_chosen = player_class
        self.print_pause("In this city you will find everything you need, from the gunsmith, to the merchant, to the potion shop, and so on.")
        self.print_pause("Now, the road is yours. Try to level up by fighting with enemies, trading rare items.")
        self.print_pause("And find out who killed our world..", 5)
    
        self.print_pause("Oh yeah, I forgot. Since this is a new beginning for you, I give you 100 experience points.", 5)
        self.check_upgrade_level(100)
    
    def intro2_Tuna_city(self):
        self.print_pause("\nNow it's time to start the new adventure.", 3)
        self.print_pause("Head to the gunsmith to buy your first weapon. Then begins your discovery towards dark magic.", 3)
    
        # If you are inside Tuna you have to choose where you want to go
        self.go_inside_Tuna()

    def create_item(self, type_item, rarity):
        item = PlayerConfiguration.general_item
        item['name'] = "Boh"
        item['type_item'] = type_item

        if type_item == "weapon":
            item['type_weapon'] = random.choices(GunsmithConfiguration.list_weapon_item, weights=[20, 20, 20, 20, 20], k=1)
            item['rarity'] = rarity

            if rarity == "base":
                item['attack'] = random.randint(10, 20)
                item['gold'] = 30
            elif rarity == "silver":
                item['attack'] = random.randint(30, 50)
                item['gold'] = 100
            elif rarity == "epic":
                item['attack'] = random.randint(80, 100)
                item['gold'] = 200
            elif rarity == "leggendary":
                item['attack'] = random.randint(150, 200)
                item['gold'] = 500
            else:
                item['attack'] = 10
                item['gold'] = 30

    def generate_item_gunsmith(self):

        if len(GunsmithConfiguration.gunsmith_item) == 0:
            GunsmithConfiguration.date_generate_item = datetime.datetime.now()

        diff = datetime.datetime.now() - GunsmithConfiguration.date_generate_item
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        if len(GunsmithConfiguration.gunsmith_item) == 0 or hours >= 24:
            GunsmithConfiguration.gunsmith_item = []
            num_of_weapon = random.randint(3,6)

            for i in range(0, num_of_weapon):
                rarity = random.choices(GunsmithConfiguration.rarity_item, weights=[60, 30, 8, 2], k=1)
                GunsmithConfiguration.gunsmith_item.append(self.create_item('weapon', rarity))

    def gunsmith(self):
        self.print_pause("What action do you want to do?")
        action = input(self.list_serial(GunsmithConfiguration.list_action_gunsmith)).lower()

        self.generate_item_gunsmith()

        if action.lower() in GunsmithConfiguration.list_action_gunsmith[0].lower():
            self.print_pause("Aron: Bye, Bye.", 3)
            self.go_inside_Tuna()
        elif action.lower() in GunsmithConfiguration.list_action_gunsmith[1].lower():
            if GunsmithConfiguration.first_to_gunsmith:
                self.print_pause("Aron: Ahhh, you want to buy something.", 3)
                self.print_pause("Aron: Mmm.. Novac says me that you are new in this town.", 3)
                self.print_pause("Aron: For this time I give you a dagger.", 3)

                #TODO: Metti nell'inventario il pugnale

                GunsmithConfiguration.first_to_gunsmith = False
            else:
                self.print_pause("Aron: What do you want to buy?", 3)
                item = input(self.list_serial(GunsmithConfiguration.gunsmith_item)).lower()

                #TODO: Creare una lista di Item, con i loro campi (un array di dict presumo) e fare la compravendita

            self.gunsmith()
        elif action.lower() in GunsmithConfiguration.list_action_gunsmith[2].lower():
            if len(PlayerConfiguration.bag) == 0:
                self.print_pause("Aron: You don't have any items to sell", 3)
                self.print_pause("Aron: Come here when you have something for me", 3)
            else:
                pass
            
            self.gunsmith()
        elif action.lower() in GunsmithConfiguration.list_action_gunsmith[3].lower():
            if GunsmithConfiguration.gunsmith_ok:
                self.print_pause("Aron: Our world has been destroyed by dark magic.", 3)
                self.print_pause("Aron: Mishra, the archmage is responsible. He sure knew about magic, until he took the path of black magic.", 3)
                self.print_pause("Aron: If you want to kill him and put an end to our despair, you better train yourself well. "
                            "I don't think it will be that simple.", 3)
            else:
                self.print_pause("Aron: Do you want to know what killed our world ???", 3)
                self.print_pause("Aron: You are not my friend, so I don't want to share this information. "
                            "But, if you enter the Forbidden Forest, and bring me unicorn blood, then maybe I can tell you what happened.", 3)
            self.gunsmith()
        elif action.lower() in GunsmithConfiguration.list_action_gunsmith[4].lower():
            self.print_pause("Aron: Mmm .. Old Novac was the teacher of many people in this village.", 3)
            self.print_pause("Aron: But now it has lost all its great power.", 3)
            self.print_pause("Aron: BThere are rumors that he possessed a dark talisman.. "
                        "Maybe he was linked to dark magic? Who knows.. "
                        "If I were you you won't pay us much attention", 3)
            self.gunsmith()
        else:
            self.gunsmith()
    def potion(self):
        pass
    
    def novac(self):
        pass
    
    def go_inside_Tuna(self):
        self.print_pause("Where do you want to go into Tuna Village?")
        place = input(self.list_serial(GameConfiguration.tuna_place)).lower()
    
        if GameConfiguration.game_over:
            self.print_pause("\n\nGame over. Try again ........")
            exit()
        elif place.lower() in 'Gunsmith'.lower():
            self.print_pause("Now you are at the gunsmith. The owner is called Aron. He is a somewhat dark man, but full of resources")
            self.print_pause("Here you can buy or sell any weapons")
            self.gunsmith()
            self.go_inside_Tuna()
        elif place.lower() in 'Merchant'.lower():
            self.print_pause("Now you are at the gunsmith named Kesha")
            self.go_inside_Tuna()
        elif place.lower() in 'Potion Shop'.lower():
            self.print_pause("Now you are at the gunsmith named The World of Potion")
    
            if not GameConfiguration.potion_shop_open:
                self.print_pause("If you want something, you have to talk with Tom...")
                self.print_pause("Now the shop is close. Try later!")
                self.go_inside_Tuna()
            else:
                self.potion()

            self.go_inside_Tuna()
        elif place.lower() in 'Druid Novac'.lower():
            self.print_pause("Hi" + PlayerConfiguration.player + ", how can I help you?")
            self.novac()
            self.go_inside_Tuna()
    
        elif place.lower() in 'Port'.lower():
            self.print_pause("Mmm, there is no one here. Seems to enter darkness")
            self.print_pause("I don't know what there is to find in this place, but maybe the fishmonger can help us out.")
            self.go_inside_Tuna()
    
            
        elif place.lower() in 'Go to World'.lower():
            self.print_pause("Now you are at the gunsmith named Aron")
        else:
            self.print_pause("The place you are looking for does not exist in this village")
            self.go_inside_Tuna()
    
    # ------------main function to trigger the game-------------
    def adventure_game(self, new_game=True):
    
        new_game = True
        if new_game:
            self.launch_splash_screen()
            #self.launch_story()
        self.set_global_variable(new_game)

        # input to ask for the player's name
        player = input(GameConfiguration.druid_name + ": What is your name?\n")
        self.print_pause("\n" + GameConfiguration.druid_name +": A young apprentice named " + player + ".", 3)
        self.print_pause(GameConfiguration.druid_name +": Ahhh. Come as in the city of Tuna that I teach you to master magic.")
    
        PlayerConfiguration.player = player
    
        # Go to the main city
        self.intro_Tuna_city()
        self.intro2_Tuna_city()
