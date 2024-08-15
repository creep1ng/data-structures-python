from deck import Deck
from hand import Hand

class Taller1:
    
    def __init__(self) -> None:
        self.deck = Deck()  # Inicializa un mazo barajado
        self.players_hands = {}  # Diccionario para almacenar las manos de los jugadores

    def add_player(self, player_name: str) -> None:
        """Agrega un jugador al juego e inicializa su mano con 5 cartas."""
        if player_name in self.players_hands:
            raise ValueError(f"Player {player_name} is already in the game.")
        
        self.players_hands[player_name] = Hand(self.deck, player_name)

    def replace_cards(self, player_name: str, card_indices: list[int]) -> None:
        """Permite al jugador reemplazar cartas en su mano."""
        if player_name not in self.players_hands:
            raise ValueError(f"Player {player_name} is not in the game.")
        
        for index in card_indices:
            self.players_hands[player_name].replace(self.deck, index)

    def show_hands(self) -> None:
        """Muestra las manos actuales de todos los jugadores."""
        for player_name, hand in self.players_hands.items():
            print(hand)

    def determine_winner(self) -> str:
        """Determina cuál jugador tiene la mejor mano y retorna su nombre."""
        best_hand = None
        winner = None

        for player_name, hand in self.players_hands.items():
            if best_hand is None or hand._get_hand_type() > best_hand._get_hand_type():
                best_hand = hand
                winner = player_name

        return winner

    def main(self) -> None:
        """Ejecuta el flujo principal del juego."""
        num_players = int(input("Enter the number of players: "))
        
        for _ in range(num_players):
            player_name = input("Enter the name of the player: ")
            self.add_player(player_name)

        # Muestra las manos iniciales de todos los jugadores
        print("Initial hands:")
        self.show_hands()

        # Permitir a cada jugador reemplazar cartas
        for player_name in self.players_hands.keys():
            replace = input(f"{player_name}, do you want to replace any cards? (yes/no): ").strip().lower()
            if replace == 'yes':
                card_indices = list(map(int, input("Enter the card indices to replace (1-5, separated by space): ").split()))
                self.replace_cards(player_name, [index - 1 for index in card_indices])

        # Muestra las manos finales de todos los jugadores
        print("Final hands:")
        self.show_hands()

        # Determinar y anunciar el ganador
        winner = self.determine_winner()
        print(f"The winner is {winner} with the hand: {self.players_hands[winner]}")

