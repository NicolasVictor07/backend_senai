
import random

tentativas = 0
while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    tentativas += 1
    if soma == 7:
        break

print(f"Tentativas necessárias: {tentativas}")
