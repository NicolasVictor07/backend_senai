class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e trabalho no setor de {self.setor}.")


# Exemplo de uso
p1 = Pessoa("Maria", 30, "Produção")
p2 = Pessoa("João", 45, "Manutenção")

p1.apresentar()
p2.apresentar()
