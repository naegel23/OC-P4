from Model import *
from View import View
from tinydb import TinyDB
import sys



db = TinyDB("db.json")
players_db = db.table("players")
tournaments_db = db.table("tournaments")
# global_players = Players()
# for row in players_db:
#     global_players.add(
#         Player(row["name"], row["firstname"],
#                row["birthday"], row["gender"], row["rank"]))


class Controller:

    def __init__(self):
        self.view = View()


        # === START PROGRAM ===
    def start_program(self):
        # self.tournament = Tournament("budokai", "lille", "23/02/2021", self.view.ask_round_amount(), "bullet", "")
        while True:
            choice = View.welcome()
            if choice == 1:
                # Create player
                Controller.insert_player(self)
            elif choice == 2:
                # Create tournament
                Controller.init_tournament(self)
            elif choice == 3:
                #Add player to tournament
                self.ask_which_player()
            # elif choice == 4:
            #     # Import tournament
            #     Controller.ask_which_tournament(self)
            # # elif choice == 3:
            # #     # Continue an existing tournament
            # #     # Controller.import_tournament()
            # elif choice == 5:
            #     Controller.play_rounds(self)
            elif choice == 6:
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
        players = Players()
        newplayer = self.create_player()
        players.add(newplayer)
        players_db.insert(newplayer.to_dict())

    def init_tournament(self):
        name = self.view.tournament_name()
        location = self.view.tournament_location()
        # date = self.view.tournament_date()
        rounds = self.view.ask_round_amount()
        time = self.view.time_controler()
        description = self.view.get_description()

        self.tournament = Tournament(name, location, rounds, time, description)
        tournaments_db.insert(self.tournament.to_dict())

    # def add_player(self):
    #     research_player = self.ask_which_player(players_db)
    #     self.tournament.players.append(
    #         Player(research_player[0]["name"], research_player[0]["first_name"], research_player[0]['birthday'],
    #                research_player[0]["gender"], research_player[0]["rank"]))
    #     for players in self.tournament.players:
    #         print(players.to_dict())

    def ask_which_player(self):
        for (i, player) in enumerate(players_db):
            View.display_player_firstname_lastname(str(i), player.name, player.first_name)

        id_list = []
        for i in range(8):
            id_list.append(View.add_player(id_list, len(players_db)))
        players = Players()

        for (i, element) in enumerate(id_list):
            players.add(
                Player(players.list[i].name,
                       players.list[i].first_name,
                       players.list[i].gender,
                       players.list[i].birthdate,
                       players.list[i].rank))

        View.intro_list_of_players()
        for (i, player) in enumerate(players.list):
            View.display_player_firstname_lastname(
                str(i), player.firstname, player.lastname)
            player.reset_score()

        View.intro_list_of_players()
        # self.play_rounds()
        # player_name = self.view.add_player(id_list, player_range)
        # query = Query()
        # result = players_db.search(query.name == player_name)


    # def play_rounds(self):
    #     p = Players()
    #     for i in range(self.tournament.current_round(), int(self.tournament.rounds)):
    #             if i == 0:
    #                 p.order_by_rank()
    #                 player_pairs = p.matchmaking_round1()
    #             else:
    #                 p.order_by_score()
    #                 player_pairs = p.matchmaking_over_rounds(self.tournament)
    #             for player in p.list:
    #                 View.display_player_infos(player.first_name, player.name,
    #                                         str(player.rank), str(player.score))
    #
    #             matches = Matches()
    #             for pair in player_pairs:
    #                 white_player = 0
    #                 black_player = 1
    #                 matches.add_match(Match(pair[0], pair[1]))
    #             View.print_matches(matches)
    #
    #             for match in matches.list:
    #                 match.winner = View.ask_winner(match)
    #                 if match.winner is None:
    #                     match.white_player.draw_match()
    #                     match.black_player.draw_match()
    #                 else:
    #                     match.winner.won_match()
    #
    #             self.tournament.add_round(matches)
    #
    #             continue_choice = View.ask_to_continue()
    #             if continue_choice == 0:
    #                 return
controller = Controller()
controller.start_program()
controller.create_player()
controller.insert_player()
# controller.play_rounds()
# controller.ask_which_tournament()
# controller.create_tournament()
