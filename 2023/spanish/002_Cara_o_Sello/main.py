print("Juguemos a Cara o Sello...\n")
import random

random_side = random.randint(0,1)
input('\nEscribe "L" para Lanzar la moneda al aire.\n').upper()
if "L":
  if random_side == 0:
    print("\n" + "Cara" + "\n")
  elif random_side == 1:
    print("\n" + "Sello" + "\n")
input('\nPresiona Run para volver a empezar el juego.\n')