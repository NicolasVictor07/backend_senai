import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    if palpite < numero_secreto:
        print("Número muito baixo! Tente um maior.")
    elif palpite > numero_secreto:
        print("Número muito alto! Tente um menor.")
    else:
        print("Parabéns! Você acertou.")
        break