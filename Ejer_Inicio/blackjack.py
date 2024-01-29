
"""Jugar al 21.
Se trata de que un jugador comience una partida contra la casa. Se reparten 2 cartas a cada participante.
La casa mostrará siempre todas sus cartas menos la última.
El jugador puede seguir pidiendo cartas hasta que se pase de 21, momento en el que pierde, o decida plantarse.
Si decide plantarse, la casa se repartirá a sí misma hasta que el valor de sus cartas supere el número 16.
Si la casa no se ha pasado de 21, momento en el que el jugador gana, se comparan los resultados.
Aquel que se acerque más a 21 gana la partida. Se puede empatar."""

import random


class Carta:
    def __init__(self,nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"

baraja = []
palos = ["bastos", "oros", "copas", "espadas"]

for i in range(4):
    for j in range(1, 11):

        if j == 8:
            baraja.append(Carta(f"Sota de {palos[i]}", palos[i], 10))
        elif j == 9:
            baraja.append(Carta(f"Caballo de {palos[i]}", palos[i], 10))
        elif j == 10:
            baraja.append(Carta(f"Rey de {palos[i]}", palos[i], 10))
        else:
            baraja.append(Carta(f"{j} de {palos[i]}", palos[i], j))

# Metodo para barajar la carta
random.shuffle(baraja)

# Definición del método jugar
def juagar():
    turno = 0
    jugador = []
    casa = []





    turno = turno + 1

for carta in baraja:
    print(carta)