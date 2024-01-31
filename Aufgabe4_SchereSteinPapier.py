import random
import pickle

class RPSLSEGame:
    def __init__(self):
        self.symbols = ["Stein", "Papier", "Schere", "Echse", "Spock"]
        self.player_wins = 0
        self.comp_wins = 0
        self.choices = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}

    def display_menu(self):
        print("1. Stein")
        print("2. Papier")
        print("3. Schere")
        print("4. Echse")
        print("5. Spock")
        print("6. Statistik anzeigen")
        print("7. Spiel beenden")

    def get_player_choice(self):
        choice = int(input("Wähle eine Zahl (1-7): "))
        if choice == 6:
            self.display_statistics()
            return None
        elif choice == 7:
            self.save_statistics()
            exit()
        elif 1 <= choice <= 5:
            return self.symbols[choice - 1]
        else:
            print("Ungültige Auswahl. Bitte wähle erneut.")
            return self.get_player_choice()

    def get_comp_choice(self):
        return random.choice(self.symbols)

    def determine_winner(self, player_choice, comp_choice):
        if player_choice == comp_choice:
            return "Unentschieden"
        elif (
            (player_choice == "Stein" and (comp_choice == "Schere" or comp_choice == "Echse"))
            or (player_choice == "Papier" and (comp_choice == "Stein" or comp_choice == "Spock"))
            or (player_choice == "Schere" and (comp_choice == "Papier" or comp_choice == "Echse"))
            or (player_choice == "Echse" and (comp_choice == "Papier" or comp_choice == "Spock"))
            or (player_choice == "Spock" and (comp_choice == "Stein" or comp_choice == "Schere"))
        ):
            return "Spieler gewinnt"
        else:
            return "Computer gewinnt"

    def update_statistics(self, winner, player_choice, comp_choice):
        print(f"Spieler wählt {player_choice}, Computer wählt {comp_choice}. {winner}")
        if winner == "Spieler gewinnt":
            self.player_wins += 1
        elif winner == "Computer gewinnt":
            self.comp_wins += 1
        self.choices[player_choice] += 1

    def display_statistics(self):
        print("\nStatistik:")
        print(f"Spieler gewinnt: {self.player_wins} Mal")
        print(f"Computer gewinnt: {self.comp_wins} Mal")
        print("Gewählte Symbole:")
        for symbol, count in self.choices.items():
            print(f"{symbol}: {count} Mal")
        print()

    def save_statistics(self):
        with open("statistics.pkl", "wb") as file:
            pickle.dump(self.choices, file)
        print("Statistik wurde gespeichert.")

    def play(self):
        while True:
            self.display_menu()
            player_choice = self.get_player_choice()
            comp_choice = self.get_comp_choice()
            winner = self.determine_winner(player_choice, comp_choice)
            self.update_statistics(winner, player_choice, comp_choice)

if __name__ == "__main__":
    game = RPSLSEGame()
    game.play()
