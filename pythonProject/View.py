import re
from Model import *


class View:
    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print("Hello ! Welcome to the Chess Tournament Manager Program\n")
        print("What do you want to do ?")
        print("1 - Create a new player")
        print("2 - Create a new tournament")
        print("3 - Continue an existing tournament")
        print("4 - Display reports")
        print("5 - End the program\n")
        try:
            choice = int(input("Enter your choice (1,2,3,4,5) : "))
            if choice < 1 or choice > 5:
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
        while True:
            try:
                gender = input("Enter gender (Male or Female): ")
                if gender == "Male" or gender == "Female":
                    print("Gender entered successfully...")
                    break
                else:
                    print("Gender should be either Male or Female")
            except:
                continue

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
        expression = r"^[A-Za-z]{1,}$"
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

    def get_tour_number(self):
        number = input("Round number : ")
        try:
            number = int(number)
            if number <= 0:
                raise ValueError("le rank saisie est négatif ou nulle")
            return number
        except ValueError:
            print("la valeur saisie est invalide")
            return self.get_tour_number()

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
        try:
            if len(description) <= 0:
                raise ValueError("Aucune information saisie ou saisie invalide")
            return description
        except Exception as e:
            print(e)
            return self.get_description()


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
