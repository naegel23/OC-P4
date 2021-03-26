from Model import *
from View import View




class Controller:
    def __init__(self):
        self.view = View()

    def create_player(self):
        username = self.view.get_username()
        name = self.view.get_name()
        first_name = self.view.get_first_name()
        birthday = self.view.get_birth_date()
        gender = self.view.get_gender()
        rank = self.view.get_ranking()

        return Player(username, name, first_name, birthday, gender, rank)

    def create_tournament(self):
        name = self.view.tournament_name()
        location = self.view.tournament_location()
        date = self.view.tournament_date()
        tour = self.view.get_tour_number()
        time = self.view.time_controler()
        description = self.view.get_description()

        return Tournament(name, location, date, tour, time, description)


    def play_round(self):
        print("-----------------")
        player1 = Player('naegel', 'najim', 'elcabiri', '23/02/1996', 'Male', int(1))
        player2 = Player('JD', 'Jean', 'Dujardin', '17/10/1978', 'Male', int(25), )
        player3 = Player('dragon queen', 'daenerys', 'targarien', '17/10/1978', 'Female', int(2))
        player4 = Player('big front', 'sakura', 'haruno', '17/10/1978', 'Female', int(48))
        player5 = Player('shingeki no kyujin', 'eren', 'jager', '17/10/1978', 'Male', int(102))
        player6 = Player('coup de tete', 'zinedine', 'zidane', '17/10/1978', 'Male', int(10))
        player7 = Player('sans nez', 'voldemort', 'potter', '17/10/1978', 'Male', int(666))
        player8 = Player('sorcière', 'hermione', 'granger', '17/10/1978', 'Female', int(16))
        p = Players()
        p.list = [player1, player2, player3, player4, player5, player6, player7, player8]
        p.order_by_rank()
        players_pair = p.matchmaking_round1()
        for player in p.list:
            print(player)
        print("-------------------")
        for player in p.list:
            View.display_player_infos(player.first_name, player.name,
                                      str(player.rank), str(player.score))
        print("-------------------")
        matches = Matches()
        for pair in players_pair:
            white_player = 0
            black_player = 1
            matches.add_match(Match(pair[0], pair[1]))

        View.print_matches(matches)
        print("-------------------")
        for match in matches.list:
            match.winner = View.ask_winner(match)
            if match.winner is None:
                match.white_player.draw_match()
                match.black_player.draw_match()
            else:
                match.winner.won_match()
        print("-------------------")
        p.order_by_score()
        lst = []
        for match in matches.list:
            lst.append(match.black_player)
            lst.append(match.white_player)
        print("-------------------")
        p.list = lst
        p.order_by_score()

        # creer un objet round qui sera contenu dans p et qui vaux
        # rounds = []
        # for i in range(0, 6, 2):
        #     match = Match(p.list[i]
        #     vs
        #     p.list[i + 1], None)
        #     rounds.append(match)

        for player in p.list:
            View.display_player_infos(player.first_name, player.name,
                                      str(player.rank), str(player.score))
        for match in matches.list:
            for pair in players_pair:
                white_player = 0
                black_player = 1
                matches.add_match(Match(pair[0], pair[1]))

            View.print_matches(matches)
        print("-------------------")

# garder la liste des rounds pour l'historique et garder round pour le round actuel


controller = Controller()
controller.play_round()


