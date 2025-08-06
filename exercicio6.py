positivos = 0
for i in range(10):
    input_num = int(input(f"Digite o número {i+1}: "))
    if input_num < 0:
        print(f"o numero {input_num} é negativo.")
    else:
        print(f"o numero {input_num} é positivo.")
        positivos += 1
print(f"Quantidade de números positivos: {positivos}")