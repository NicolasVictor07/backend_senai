# Classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Carro: {self.marca} {self.modelo} - Ano: {self.ano}")


# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e trabalho no setor de {self.setor}.")


# Classe Manual
class Manual:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print(f"O manual '{self.titulo}', escrito por {self.autor}, foi publicado em {self.ano_publicacao}.")


# Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_estoque(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade em estoque: {self.quantidade}")


# Classe Treinamento
class Treinamento:
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao = duracao

    def descricao(self):
        print(f"Treinamento: {self.titulo} | Instrutor: {self.instrutor} | Duração: {self.duracao} minutos")


# Classe Aluno
class Aluno:
    def __init__(self, nome, curso, nota_final):
        self.nome = nome
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        resultado = "Aprovado" if self.nota_final >= 7 else "Reprovado"
        print(f"Aluno: {self.nome} | Curso: {self.curso} | Nota Final: {self.nota_final} | Resultado: {resultado}")


# =======================
# SIMULAÇÃO DO SISTEMA
# =======================

print("\n=== FROTA DE VEÍCULOS ===")
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Ford", "Fiesta", 2018)
carro1.detalhes()
carro2.detalhes()

print("\n=== FUNCIONÁRIOS ===")
p1 = Pessoa("Maria", 30, "Produção")
p2 = Pessoa("João", 45, "Manutenção")
p3 = Pessoa("Carla", 29, "Qualidade")
p1.apresentar()
p2.apresentar()
p3.apresentar()

print("\n=== MANUAIS TÉCNICOS ===")
m1 = Manual("Manutenção de Motores", "Carlos Silva", 2021)
m2 = Manual("Segurança do Trabalho", "Ana Souza", 2019)
m1.informacoes()
m2.informacoes()

print("\n=== PRODUTOS EM ESTOQUE ===")
prod1 = Produto("Parafuso", 0.50, 1000)
prod2 = Produto("Chave de Fenda", 12.90, 150)
prod3 = Produto("Martelo", 25.00, 80)
prod1.mostrar_estoque()
prod2.mostrar_estoque()
prod3.mostrar_estoque()

print("\n=== TREINAMENTOS OBRIGATÓRIOS ===")
t1 = Treinamento("Segurança no Trabalho", "Carlos Souza", 120)
t2 = Treinamento("Primeiros Socorros", "Ana Lima", 90)
t1.descricao()
t2.descricao()

print("\n=== CURSOS DE CAPACITAÇÃO ===")
a1 = Aluno("João", "Eletricista Industrial", 8.5)
a2 = Aluno("Maria", "Soldagem", 6.0)
a3 = Aluno("Paulo", "Automação", 7.0)
a1.status()
a2.status()
a3.status()
