x = int(input("Digite um número: "))

if x < 2:
    print(f"{x} não é primo.")
else:
    primo = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            primo = False
            break
    if primo:
        print(f"{x} é primo.")
    else:
        print(f"{x} não é primo.")