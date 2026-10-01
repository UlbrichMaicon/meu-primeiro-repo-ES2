import random
import time
import os

cores = [
    "\033[91m",  # vermelho
    "\033[92m",  # verde
    "\033[93m",  # amarelo
    "\033[94m",  # azul
    "\033[95m",  # roxo
    "\033[96m",  # ciano
]

RESET = "\033[0m"

largura = 60
altura = 15

while True:
    os.system("cls" if os.name == "nt" else "clear")

    for _ in range(altura):
        linha = ""

        for _ in range(largura):
            if random.random() < 0.08:
                linha += random.choice(cores) + random.choice("*.+o") + RESET
            else:
                linha += " "

        print(linha)

    time.sleep(0.1)
