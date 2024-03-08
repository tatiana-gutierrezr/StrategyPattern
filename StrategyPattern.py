import time
import random
import sys

class CompAtaque:
    def ataque(self):
        pass

class Movimiento:
    def move(self):
        pass

class AtaqueSoldado(CompAtaque):
    def ataque(self):
        print("Soldado atacando con fusil")

class MovSoldado(Movimiento):
    def move(self):
        print("Soldado moviéndose a pie")

class AtaqueArquero(CompAtaque):
    def ataque(self):
        print("Arquero disparando flechas")

class MovArquero(Movimiento):
    def move(self):
        print("Arquero moviéndose a pie")

class AtaqueCaballero(CompAtaque):
    def ataque(self):
        print("Caballero atacando con espada")

class MovCaballero(Movimiento):
    def move(self):
        print("Caballero moviéndose a caballo")

class Unidad:
    def __init__(self, name, comp_ataque, comp_mov):
        self.name = name
        self.comp_ataque = comp_ataque
        self.comp_mov = comp_mov

    def set_comp_ataque(self, comp_ataque):
        self.comp_ataque = comp_ataque

    def set_comp_mov(self, comp_mov):
        self.comp_mov = comp_mov

    def perform_ataque(self):
        print(f"{self.name} está listo para atacar")
        self.comp_ataque.ataque()

    def perform_movimiento(self):
        print(f"{self.name} está listo para moverse")
        self.comp_mov.move()

    def __str__(self):
        return f"{self.name}"

def print_menu():
    print("╔════════════════════════╗")
    print("║         Menú           ║")
    print("╠════════════════════════╣")
    print("║ 1. Soldado             ║")
    print("║ 2. Arquero             ║")
    print("║ 3. Caballero           ║")
    print("║ 4. Salir               ║")
    print("╚════════════════════════╝")

def print_unidades(units):
    print("╔════════════════════════╗")
    print("║  Unidades Disponibles  ║")
    print("╠════════════════════════╣")

    #Itera sobre las unidades disponibles con su índice
    for i, unit in enumerate(units, start=1):
        #Imprime una línea con el índice, el nombre de la unidad y
        #un relleno para ajustar los bordes
        print(f"║ {i}. {unit.name:<20}║")

    print("╚════════════════════════╝")

def battle(unit1, unit2):
    print(f"\nComienza la batalla entre {unit1} y {unit2}")
    time.sleep(1)

    print(f"\nTurno de {unit1}:")
    unit1.perform_movimiento()
    time.sleep(1)
    unit1.perform_ataque()
    time.sleep(1)

    print(f"\nTurno de {unit2}:")
    unit2.perform_movimiento()
    time.sleep(1)
    unit2.perform_ataque()
    time.sleep(1)

    ganador = random.choice([unit1, unit2])
    print(f"\n{ganador} es el ganador de la batalla")
    time.sleep(1)

    sys.exit()

if __name__ == "__main__":
    units = [
        Unidad("Soldado", AtaqueSoldado(), MovSoldado()),
        Unidad("Arquero", AtaqueArquero(), MovArquero()),
        Unidad("Caballero", AtaqueCaballero(), MovCaballero())
    ]

    while True:
        print_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '4':
            sys.exit()

        try:
            opcion = int(opcion)
            if opcion not in range(1, 4):
                raise ValueError
        except ValueError:
            print("Opción no válida")
            continue

        if 1 <= opcion <= len(units):
            unit1 = units.pop(opcion - 1)
        else:
            print("Opción no válida")
            continue

        print_unidades(units)
        opcion = input("\nSelecciona la segunda unidad para la batalla: ")

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(units):
                unit2 = units.pop(opcion - 1)
            else:
                raise ValueError
        except ValueError:
            print("Opción no válida")
            continue

        battle(unit1, unit2)