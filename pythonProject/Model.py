# import datetime
from tinydb import TinyDB


class Player:

    def __init__(self, name, first_name, birthdate, gender, rank):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = str(gender)
        self.rank = rank
        self.score = 0

    def __str__(self):
        info = f'name : {self.name} -- rank : {self.rank} -- score : {self.score}'
        return info.format(self)

    def reset_score(self):
        self.score = 0.0

    def won_match(self):
        self.score += 1.0

    def draw_match(self):
        self.score += 0.5

    def to_dict(self):
        player_dict = {"name": self.name,
                       "first_name": self.first_name,
                       "birthday": str(self.birthdate),
                       "gender": self.gender,
                       "rank": self.rank,
                       "score": self.score}

        return player_dict


class Players:

    def __init__(self):
        self.list = []

    def get_lenght(self):
        return len(self.list)

    def add(self, player):
        self.list.append(player)

    def order_by_rank(self):
        self.list.sort(key=lambda x: x.rank, reverse=True)

    def order_by_score(self):
        self.list.sort(key=lambda x: (x.score, x.rank), reverse=True)

    def matchmaking_round1(self):
        return [[self.list[0], self.list[4]], [self.list[1], self.list[5]], [self.list[2], self.list[6]],
                [self.list[3], self.list[7]]]

    def matchmaking_over_rounds(self, tournament):
        for matches in tournament.round_list:
            for match in matches.list:
                if (match.white_player == self.list[0] and match.black_player == self.list[1]) or (
                        match.black_player == self.list[0] and match.white_player == self.list[1]):
                    return [[self.list[0], self.list[2]],
                            [self.list[1], self.list[3]],
                            [self.list[4], self.list[5]],
                            [self.list[6], self.list[7]]]
        return [[self.list[0], self.list[1]],
                [self.list[2], self.list[3]],
                [self.list[4], self.list[5]],
                [self.list[6], self.list[7]]]

    def to_dict(self):
        players_dict = {
            "list": []
        }
        for player in self.list:
            players_dict["list"].append(player.to_dict())

        return players_dict


class Match:

    def __init__(self, white_player, black_player):
        self.white_player = white_player
        self.black_player = black_player
        self.winner = None

    def set_winner(self, winner):
        self.winner = winner

    def versus(self):
        versus = (self.white_player, self.black_player)
        return versus

    def to_dict(self):
        if self.winner is None:
            match_dict = {
                "white_player": self.white_player.to_dict(),
                "black_player": self.black_player.to_dict(),
                "winner": None
            }
        else:
            match_dict = {
                "white_player": self.white_player.to_dict(),
                "black_player": self.black_player.to_dict(),
                "winner": self.winner.to_dict()
            }
        return match_dict


class Matches:

    def __init__(self):
        self.list = []

    def add_match(self, match):
        self.list.append(match)

    def to_dict(self):
        matches_dict = {
            "list": []
        }
        for match in self.list:
            matches_dict["list"].append(match.to_dict())

        return matches_dict


class Tournament:

    def __init__(self, name, location, players, rounds, timer, description):
        db = TinyDB("db.json")
        tournaments_db = db.table("tournaments")

        self.id = len(tournaments_db)
        self.name = name
        self.location = location
        # self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.rounds = rounds
        self.round_list = []
        self.players = players
        self.timer = str(timer)
        self.description = description

    def __str__(self):
        info = f'name : {self.name} -- location : {self.location} -- rounds  : {self.rounds} -- timer : {self.timer} -- description : {self.description}'
        return info.format(self)

    def add_round(self, matches):
        self.round_list.append(matches)

    def current_round(self):
        return len(self.round_list)

    def to_dict(self):
        tournament_dict = {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "rounds": self.rounds,
            "round_list": [],
            "players": self.players.to_dict(),
            "timer": self.timer,
            "description": self.description
        }
        for matches in self.round_list:
            tournament_dict["round_list"].append(matches.to_dict())

        return tournament_dict
