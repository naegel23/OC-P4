import datetime

class Player:

    def __init__(self, username, name, first_name, birthdate, gender, rank):
        self.username = username
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.score = 0

    def __str__(self):
        players = f'{self.username}, {self.name}, rank/score : {self.rank}, {self.score}'
        return players.format(self)

    def won_match(self):
        self.score += 1.0

    def draw_match(self):
        self.score += 0.5
class Players:

    def __init__(self):
        self.list = []

    def get_lenght(self):
        return len(self.list)

    def add_player(self, player):
        self.list.append(player)

    def order_by_rank(self):
        self.list.sort(key=lambda x: x.rank, reverse=True)

    def order_by_score(self):
        self.list.sort(key=lambda x: (x.score, x.rank), reverse=True)

    def matchmaking_round1(self):
        return[[self.list[0], self.list[4]], [self.list[1], self.list[5]], [self.list[2], self.list[6]], [self.list[3], self.list[7]]]

    def matchmaking_over_rounds(self, matches):

        for match in matches.list:
            if (match.white_player == self.list[0] and match.black_player == self.list[1]) or (match.black_player == self.list[0] and match.white_player == self.list[1]):
                 return [[self.list[0], self.list[2]],
                        [self.list[1], self.list[3]],
                        [self.list[4], self.list[5]],
                        [self.list[6], self.list[7]]]
            return [[self.list[0], self.list[1]],
                [self.list[2], self.list[3]],
                [self.list[4], self.list[5]],
                [self.list[6], self.list[7]]]


class Match:

    def __init__(self, white_player, black_player):
        self.white_player = white_player
        self.black_player = black_player
        self.winner = None

    def versus(self):
        versus = (self.white_player, self.black_player)
        return versus

class Matches:

    def __init__(self):
        self.list = []

    def add_match(self, match):
        self.list.append(match)


class Tournament:

    def __init__(self, name, location, players, rounds, timer, description):
        self.name = name
        self.location = location
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.rounds = rounds
        self.round_list = []
        self.players = players
        self.timer = timer
        self.description = description

    def add_round(self, matches):
        self.round_list.append(matches)

    def current_round(self):
        return len(self.round_list)