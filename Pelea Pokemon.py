import time
import numpy

class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EV, HP="===================="):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ATK = float(EV["ATK"])
        self.DEF = float(EV["DEF"])
        self.barras = 20  # barras de HP que tiene el pokemon
        self.HP = "=" * self.barras

    def impresion_caracteristicas(self, Pokemon2):
        print("---- Pelea Puchamon ----\n")
        print(f"{self.nombre}")
        print("Tipo -", self.tipos)
        print("DEF -", self.DEF)
        print("ATK -", self.ATK)
        print("\n---- VS ----\n")
        print(f"{Pokemon2.nombre}")
        print("Tipo -", Pokemon2.tipos)
        print("DEF -", Pokemon2.DEF)
        print("ATK -", Pokemon2.ATK)
        time.sleep(2)

    def tabla_tipos(self, Pokemon2):
        tipoVentaja = ["fuego", "agua", "planta"]
        efectividad_1ATK = efectividad_2ATK = ""

        if self.tipos == Pokemon2.tipos:
            efectividad_1ATK = "\nNo es muy efectivo..."
            efectividad_2ATK = "\nNo es muy efectivo..."
        elif Pokemon2.tipos == tipoVentaja[(tipoVentaja.index(self.tipos) + 1) % 3]:
            Pokemon2.ATK *= 2.0
            Pokemon2.DEF *= 2.0
            self.ATK /= 2.0
            self.DEF /= 2.0
            efectividad_1ATK = "\nEl ataque es poco efectivo..."
            efectividad_2ATK = "\nEl ataque es muy efectivo!"
        elif self.tipos == tipoVentaja[(tipoVentaja.index(Pokemon2.tipos) + 1) % 3]:
            self.ATK *= 2.0
            self.DEF *= 2.0
            Pokemon2.ATK /= 2.0
            Pokemon2.DEF /= 2.0
            efectividad_1ATK = "\nEl ataque es muy efectivo!"
            efectividad_2ATK = "\nEl ataque es poco efectivo!"

        return efectividad_1ATK, efectividad_2ATK

    def turnos(self, Pokemon2, efectividad_1ATK, efectividad_2ATK):
        while self.barras > 0 and Pokemon2.barras > 0:
            print(f"\n{self.nombre} PS: {self.HP}")
            print(f"{Pokemon2.nombre} PS: {Pokemon2.HP}")

            # Turno SELF
            print(f"Vamos {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i + 1}. {x}")
            movElegido = int(input("Selecciona un movimiento: ")) - 1
            print(f"\n{self.nombre} usó {self.movimientos[movElegido]}")
            time.sleep(1)
            print(efectividad_1ATK)
            time.sleep(1)
            
            # Calcular daño
            Pokemon2.barras -= self.ATK
            Pokemon2.HP = ""

            time.sleep(1)
            print(f"\n{self.nombre}  PS  {self.HP}")
            print(f"\n{Pokemon2.nombre}  PS  {Pokemon2.HP}")
            
            time.sleep(3)
            if Pokemon2.barras <= 0:
                print(f"\n...{Pokemon2.nombre} se debilito")
                break
            
            # Turno POKEMON2
            print(f"Vamos {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i + 1}. {x}")
            movElegido = int(input("Selecciona un movimiento: ")) - 1
            print(f"\n{Pokemon2.nombre} usó {Pokemon2.movimientos[movElegido]}")
            time.sleep(1)
            print(efectividad_2ATK)

            # Calcular daño
            self.barras -= Pokemon2.ATK
            self.HP = ""
            
            time.sleep(1)
            print(f"\n{self.nombre}  PS  {self.HP}")
            print(f"\n{Pokemon2.nombre}  PS  {Pokemon2.HP}")
            
            time.sleep(3)
            if self.barras <= 0:
                print(f"\n...{self.nombre} se debilito")
                break

    def batalla(self, Pokemon2):
        self.impresion_caracteristicas(Pokemon2)
        efectividad_1ATK, efectividad_2ATK = self.tabla_tipos(Pokemon2)
        self.turnos(Pokemon2, efectividad_1ATK, efectividad_2ATK)
        plata = numpy.random.choice(100)
        print(f"\nEl oponente te ha pagado ${plata}\n")

if __name__ == "__main__":
    Fuego = Pokemon("Arcanine", "fuego", ["Rueda fuego", "Envite ígneo", "Colmillo ígneo", "Nitrocarga"], {"ATK": 10, "DEF": 10})
    Planta = Pokemon("Leavanny", "planta", ["Hoja afilada", "Hoja aguda", "Llueve hojas", "Rayo solar"], {"ATK": 6, "DEF": 8})
    Agua = Pokemon("Quagsire", "agua", ["Pistola agua", "Danza lluvia", "Agua lodosa", "Acuacola"], {"ATK": 8, "DEF": 12})
    Fuego.batalla(Agua)
             