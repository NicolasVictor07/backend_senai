maior= None
menor= None
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")