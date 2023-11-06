# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
tempo = 10

print(f"falta {tempo} segundo para estourar os fogos ")
while tempo > 0:
    print(tempo)
    tempo -= 1
    time.sleep(1)
print("POW POW 🎆🎆🎆🔥🔥")