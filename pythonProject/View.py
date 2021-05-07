import re
import datetime


class View:
    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print("\n==================================================")
        print("Hello ! Welcome to the Chess Tournament Manager Program\n")
        print("What do you want to do ?")
        print("1 - Create a new player")
        print("2 - Create a new tournament")
        print("3 - Continue an existing tournament")
        print("4 - End the program\n")
        try:
            choice = int(input("Enter your choice (1,2,3,4,5,6) : "))
            if choice < 1 or choice > 4:
                raise ValueError
            print("\nYour choice ({}) has been "
                  "successfully entered...\n".format(choice))
            return choice
        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return View.welcome()

# ============création player==============
    def get_username(self):
        username = input("Entrer votre username : ")
        try:
            if len(username) <= 2:
                raise ValueError("La taille du nom est trop court")
            return username
        except Exception as e:
            print(e)
            return self.get_username()

    # récupération du nom
    def get_first_name(self):
        first_name = input("entrer votre nom : ")
        try:
            if len(first_name) <= 2:
                raise ValueError("La taille du nom est trop court")
            return first_name
        except Exception as e:
            print(e)
            return self.get_first_name()

    # récupération du prénom
    def get_name(self):
        name = input("entrer votre prenom : ")
        try:
            if len(name) <= 2:
                raise ValueError("la taille du prenom est trop court")
            return name
        except Exception as e:
            print(e)
            return self.get_name()

    # récupération de la date de naissance
    def get_birth_date(self):
        while True:
            DOB = input('Enter your Date of Birth :')
            try:
                DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")

        return DOB

    # récupération du genre
    def get_gender(self):
        try:
            gender = input("Enter gender (Male or Female): ")
            if gender != "Male" and gender != "Female":
                raise ValueError
            print("Gender entered successfully...")
            return gender
        except ValueError:
            print("Incorrect gender, has to be 'Male' or 'Female'")
            return self.get_gender()

    # récupération du rank
    def get_ranking(self):
        ranking = input("indiquer votre rank : ")
        try:
            ranking = int(ranking)
            print(f"Vous êtes rank {ranking}")
            if ranking <= 0:
                raise ValueError("le rank saisie est négatif ou nulle")
            return ranking
        except ValueError:
            print("la valeur saisie est invalide")
            return self.get_ranking()

# ================ création Tournoi =================
    def tournament_name(self):
        name = input("nom du tournoi :")
        try:
            if len(name) <= 2:
                raise ValueError("Le nom est trop court ou incorrect")
            return name
        except Exception as e:
            print(e)
            return self.tournament_name()

        # récupération du lieu

    def tournament_location(self):
        expression = r"^[A-Za-z ]*"
        exp_loc = re.compile(expression)
        location = input("Indiquer le lieu du tournoi :")
        while exp_loc.search(location) is None:
            location = input("Indiquer le lieu du tournoi :")

        return location

        # récupération de la date du déroulement du tournoi

    def tournament_date(self):
        while True:
            DOT = input('Enter your Date of Tournament :')
            try:
                DOT = datetime.datetime.strptime(DOT, "%d/%m/%Y")
                break
            except ValueError:
                print("Error: must be format dd/mm/yyyy ")

        return DOT

        # récupération du nom du round

    @staticmethod
    def ask_round_amount():
        try:
            round_amount = input("Please enter the round "
                                 "amount (min = 1, max = 20, default = 4) : ")
            if round_amount == "":
                round_amount = 4
            round_amount = int(round_amount)
            if round_amount < 1 or round_amount > 20:
                raise ValueError
            print("Round amount entered successfully")
            return round_amount
        except ValueError:
            print("The round amount isn't in the"
                  " value range (0 < round_amount < 21) !")
            return View.ask_round_amount()

    def time_controler(self):
        while True:
            try:
                time = input("game time : bullet, blitz or coup rapide ")
                if time == "bullet" or time == "blitz" or time == "coup rapide":
                    print(f"The game time is {time}")
                    break
                else:
                    print("Game time should be either bullet, blitz or coup rapide :")
            except:
                continue

    def get_description(self):
        description = input("Information : ")
        return description

# ============== View Match =================
    @staticmethod
    def display_player_infos(firstname, lastname, rank, score):
        print(firstname + " " + lastname +
              " - Rank = " + rank +
              " - Score = " + score)

    @staticmethod
    def print_matches(matches):
        print("This round will confront :\n")
        for match in matches.list:
            print(match.white_player.first_name + " " +
                  match.white_player.name + " (white) VS " +
                  match.black_player.first_name + " " +
                  match.black_player.name + " (black)")

    @staticmethod
    def ask_winner(match):
        try:
            print("Who won the match : " + match.white_player.first_name
                  + " " + match.white_player.name
                  + " (white) VS " + match.black_player.first_name + " "
                  + match.black_player.name + " (black) :")
            winner = input("Format (W or B or D for Draw) : ")
            if winner.upper() != "W" and winner.upper() != "B" \
                    and winner.upper() != "D":
                raise ValueError
            print("Winner entered successfully...")
            if winner.upper() == "W":
                return match.white_player
            elif winner.upper() == "B":
                return match.black_player
            elif winner.upper() == "D":
                return None
        except ValueError:
            print("The winner doesn't respect the format (W or B) !")
            return View.ask_winner(match)

    @staticmethod
    def ask_to_continue():
        try:
            print(
                "Do you want to stop here and continue later ? ")
            choice = input("Format 'yes' or 'no' : ")
            if choice != "yes" and choice != "no":
                raise ValueError
            if choice == "yes":
                return 0
            elif choice == "no":
                return 1
            print("Choice entered successfully...")
            return choice
        except ValueError:
            print("The choice entered doesn't respect "
                  "the format ('yes' or 'no') !")
            return View.ask_to_continue()

    @staticmethod
    def choice_leave_tournament():
        print("Program ended ! See you soon ! Don't forget "
              "everything you've done is saved and waiting "
              "for you to comeback !")

    @staticmethod
    def error_occurred():
        print("An unknown error occurred ...")

    @staticmethod
    def intro_list_of_players():
        print("\n==================================================")
        print("Here's the list of the tournament's players :")

    @staticmethod
    def add_player(id_list, player_range):
        try:
            player_id = int(input(
                "Please enter the id of the user you want to add : "))
            if player_id < 0 or player_id > player_range - 1:
                raise ValueError
            if player_id in id_list:
                raise ValueError
            print("ID successfully...")
            return player_id
        except ValueError:
            print("The ID entered is not in the range or has "
                  "already been added !")
            return View.add_player(id_list, player_range)

    @staticmethod
    def display_player_firstname_lastname(i, name, first_name):
        print(i + " - " + name + " " + first_name)

    @staticmethod
    def intro_choice_import_tournament():
        print("\n==================================================")
        print("You've chosen to import an existing tournament !\n")

    @staticmethod
    def display_tournament_infos(i, name, location):
        print(i + " - Name: " + name + " - Place: " + location)

    @staticmethod
    def ask_tournament_id(id_range):
        print("\n==================================================")
        try:
            choice = int(input(
                "What tournament do you want to chose ? "))
            if choice < 0 or choice > id_range:
                raise ValueError
            print("ID entered successfully...")
            return choice
        except ValueError:
            print("The ID entered is not in the range !")
            return View.ask_tournament_id(id_range)

    @staticmethod
    def display_results(tournament):
        print("\n==================================================")
        print("The tournament is now finished, every match "
              "has been played, here's the recap :")

        print("Results of " + tournament.name + " :")
        tournament.players.order_by_score()
        for player in tournament.players.list:
            print(player.name + " " + player.first_name + " - Rank = "
                  + str(player.rank) + " - Final score = " + str(player.score))

    @staticmethod
    def intro_choice_create_tournament():
        print("\n==================================================")
        print("You've chosen to create a tournament from scratch !\n")

        print("Here are all the players in your database :")
