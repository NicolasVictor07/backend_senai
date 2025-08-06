login= input("Digite seu login: ")
senha= input("Digite sua senha: ")
while senha != "1234":
    print("Senha incorreta. Tente novamente.")
    senha= input("Digite sua senha: ")
print(f"Bem-vindo, {login}!")