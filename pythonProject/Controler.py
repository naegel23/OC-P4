from Model import *
from View import View
from tinydb import TinyDB
import sys


db = TinyDB("db.json")
players_db = db.table("players")

global_players = Players()
for row in players_db:
    global_players.add_player(
        Player(row["name"], row["firstname"],
               row["birthday"], row["gender"], row["rank"]))


class Controller:

    def __init__(self):
        self.view = View()


        # === START PROGRAM ===
    def start_program(self):

        while True:
            choice = View.welcome()
            if choice == 1:
                # Create player
                Controller.insert_player(self)
            # elif choice == 2:
            #     # Create tournament
            #     Controller.create_tournament(self)
            # # elif choice == 3:
            # #     # Continue an existing tournament
            # #     # Controller.import_tournament()
            elif choice == 2:
                View.choice_leave_tournament()
                return sys.exit()
            else:
                View.error_occurred()
                return

    def create_player(self):

        name = self.view.get_name()
        first_name = self.view.get_first_name()
        birthday = self.view.get_birth_date()
        gender = self.view.get_gender()
        rank = self.view.get_ranking()

        return Player(name, first_name, birthday, gender, rank)

    def insert_player(self):
        newplayer = self.create_player()
        global_players.add_player(newplayer)
        players_db.insert(newplayer.to_dict())




    # def create_tournament(self):
    #     name = self.view.tournament_name()
    #     location = self.view.tournament_location()
    #     date = self.view.tournament_date()
    #     rounds = self.view.ask_round_amount()
    #     time = self.view.time_controler()
    #     description = self.view.get_description()
    #
    #     return Tournament(name, location, date, rounds, time, description)


controller = Controller()
controller.start_program()
controller.create_player()
controller.insert_player()
# controller.create_tournament()

