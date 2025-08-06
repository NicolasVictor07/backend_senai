#18. Peça um valor e calcule a quantidade mínima de cédulas (100, 50, 20, 10, 5, 2, 1) para esse valor
valor = int(input("Digite um valor: "))
cedulas = [100, 50, 20, 10, 5, 2, 1]
quantidade = []

for cedula in cedulas:
    quantidade.append(valor // cedula)
    valor %= cedula

print("Quantidade mínima de cédulas:")
for i in range(len(cedulas)):
    print(f"R$ {cedulas[i]}: {quantidade[i]}")