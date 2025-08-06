notas = []
while True:
    try:
        nota = float(input("Digite uma nota (ou -1 para encerrar): "))
        if nota == -1:
            break
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media}")
else:
    print("Nenhuma nota válida foi inserida.")
