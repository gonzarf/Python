class Carta:
    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"


baraja = []
palos = ["Bastos", "Oros", "Copas", "Espadas"]
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


for carta in baraja:
    print(carta)
