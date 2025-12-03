#16. Peça um número inteiro e mostre sua representação em binário (sem usar bin()).
numero = int(input("Digite um número inteiro: "))
if numero == 0:
    print("0")
else:
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    print(binario)
