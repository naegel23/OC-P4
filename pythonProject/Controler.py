from Model import *
from View import View
from tinydb import TinyDB, Query
import sys


class Controller:

    def __init__(self):
        self.view = View()
        db = TinyDB("db.json")
        self.players_db = db.table("players")
        self.tournaments_db = db.table("tournaments")

        # === START PROGRAM ===
    def start_program(self):
        while True:
            choice = View.welcome()
            if choice == 1:
                # Create player
                Controller.insert_player(self)
            elif choice == 2:
                # Create tournament
                Controller.create_tournament(self)
            elif choice == 3:
                # Import tournament
                Controller.choice_import_tournament(self, self.tournaments_db)
            # elif choice == 4:
            #     Controller.play_rounds(self)
            elif choice == 4:
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
        self.players_db.insert(newplayer.to_dict())

    def init_tournament(self, players):
        name = self.view.tournament_name()
        location = self.view.tournament_location()
        # date = self.view.tournament_date()
        rounds = self.view.ask_round_amount()
        time = self.view.time_controler()
        description = self.view.get_description()

        return Tournament(name, location, players, rounds, time, description)

    def create_tournament(self):
        View.intro_choice_create_tournament()
        for (i, player) in enumerate(self.players_db):
            View.display_player_firstname_lastname(str(i), player["name"], player["first_name"])

        id_list = []
        for i in range(8):
            id_list.append(View.add_player(id_list, len(self.players_db)))
        players = Players()

        for (i, element) in enumerate(id_list):
            data = self.players_db.get(doc_id=element + 1)
            players.add(
                Player(data["name"],
                       data["first_name"],
                       data["gender"],
                       data["birthday"],
                       data["rank"]))

        View.intro_list_of_players()
        for (i, player) in enumerate(players.list):
            View.display_player_firstname_lastname(
                str(i), player.name, player.first_name)
            player.reset_score()
        tournament = self.init_tournament(players)
        print(tournament.to_dict())
        self.tournaments_db.insert(tournament.to_dict())
        View.intro_list_of_players()
        Controller.play_rounds(self, tournament, players)

        View.display_results(tournament)

    def play_rounds(self, tournament, p):
        for i in range(tournament.current_round(), int(tournament.rounds)):
            if i == 0:
                p.order_by_rank()
                player_pairs = p.matchmaking_round1()
            else:
                p.order_by_score()
                player_pairs = p.matchmaking_over_rounds(tournament)
            for player in p.list:
                View.display_player_infos(player.first_name, player.name, str(player.rank), str(player.score))

            matches = Matches()
            for pair in player_pairs:
                white_player = 0
                black_player = 1
                matches.add_match(Match(pair[0], pair[1]))
            View.print_matches(matches)

            for match in matches.list:
                match.winner = View.ask_winner(match)
                if match.winner is None:
                    match.white_player.draw_match()
                    match.black_player.draw_match()
                else:
                    match.winner.won_match()

            tournament.add_round(matches)
            tournament_in_db = Query()
            self.tournaments_db.update(tournament.to_dict(), tournament_in_db.id == tournament.id)

            continue_choice = View.ask_to_continue()
            if continue_choice == 0:
                return

    def choice_import_tournament(self, tournaments_db):
    #enlever tournaments-db et remplacer par self.tournaments_db
        View.intro_choice_import_tournament()
        result = self.ask_which_tournament()[0]

        players = Players()
        tournament = Tournament(result["name"], result["location"], players,
                                result["rounds"],
                                result["timer"], result["description"])
        tournament.id = result["id"]

        for player in result["players"]["list"]:
            current_player = Player(player["name"], player["first_name"],
                                    player["gender"], player["birthday"],
                                    player["rank"])
            current_player.score = player["score"]

            players.add(current_player)

        for rounds in result["round_list"]:
            temp_round = Matches()
            for matches in rounds["list"]:
                white_player = Player(matches["white_player"]["name"],
                                      matches["white_player"]["first_name"],
                                      matches["white_player"]["gender"],
                                      matches["white_player"]["birthday"],
                                      matches["white_player"]["rank"])
                white_player.score = matches["white_player"]["score"]
                black_player = Player(matches["black_player"]["name"],
                                      matches["black_player"]["first_name"],
                                      matches["black_player"]["gender"],
                                      matches["black_player"]["birthday"],
                                      matches["black_player"]["rank"])
                white_player.score = matches["black_player"]["score"]
                temp_match = Match(white_player, black_player)
                if matches["winner"] is not None:
                    temp_match.set_winner(Player(
                        matches["winner"]["name"],
                        matches["winner"]["first_name"],
                        matches["winner"]["gender"],
                        matches["winner"]["birthday"],
                        matches["winner"]["rank"]))
                    temp_match.winner.score = matches["winner"]["score"]
                temp_round.add_match(temp_match)

            tournament.add_round(temp_round)

        View.intro_list_of_players()
        for (i, player) in enumerate(players.list):
            View.display_player_firstname_lastname(
                str(i), player.name, player.first_name)

        Controller.play_rounds(self, tournament, players)
        View.display_results(tournament)

    def ask_which_tournament(self):
        for tournament in self.tournaments_db.all():
            View.display_tournament_infos(
                str(tournament["id"]), tournament["name"],
                tournament["location"])

        tournament_id = View.ask_tournament_id(len(self.tournaments_db))
        query = Query()
        result = self.tournaments_db.search(query.id == tournament_id)

        return result


controller = Controller()
controller.start_program()
