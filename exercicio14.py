fibonacci = int(input("Digite um número: "))
a, b = 0, 1
for i in range(1, fibonacci + 1):
    print(a)
    a, b = b, a + b