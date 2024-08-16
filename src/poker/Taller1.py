import random
from deck import Deck
from hand import Hand
from handtypes import HandType

class Taller1:

    def __init__(self, num_jugadores):
        self.num_jugadores = num_jugadores
        self.jugadores = [f"Jugador {i+1}" for i in range(num_jugadores)]
        self.manos = []
        self.deck = Deck()
        self.pases = [False] * num_jugadores

    def inicializar_manos(self):
        self.manos = [Hand(self.deck, nombre) for nombre in self.jugadores]

    def pedir_carta(self, jugador_index, carta_index):
        self.manos[jugador_index].replace(self.deck, carta_index)
        
    def pasar(self, jugador_index):
        self.pases[jugador_index] = True

    def todos_pasan(self):
        return all(self.pases)
    
    def mostrar_manos(self):
        for mano in self.manos:
            print(mano)

    def obtener_ganador(self):
        return max(self.manos, key=lambda mano: mano._get_hand_type().value)

    def jugar(self):
        self.inicializar_manos()
        turno_actual = 0

        while True:
            print(f"\n--- Turno de {self.jugadores[turno_actual]} ---")
            self.mostrar_manos()

            accion = input(f"{self.jugadores[turno_actual]}, ¿Qué quieres hacer? (pasar/pedir): ").strip().lower()

            if accion == "pasar":
                self.pasar(turno_actual)
            elif accion == "pedir":
                carta_index = int(input("Indica el índice de la carta que deseas reemplazar (0-4): "))
                self.pedir_carta(turno_actual, carta_index)

            if self.todos_pasan():
                break
            turno_actual = (turno_actual + 1) % self.num_jugadores

        ganador = self.obtener_ganador()
        print(f"\nEl ganador es {ganador._player_name} con {ganador._get_hand_type().name}: {ganador}")

if __name__ == "__main__":
    num_jugadores = int(input("¿Cuántos jugadores participarán?: ").strip())
    juego = Taller1(num_jugadores)
    juego.jugar()