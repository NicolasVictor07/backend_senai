class Manual:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print(f"O manual '{self.titulo}', escrito por {self.autor}, foi publicado em {self.ano_publicacao}.")


# Exemplo de uso
m1 = Manual("Manutenção de Motores", "Carlos Silva", 2021)
m2 = Manual("Segurança do Trabalho", "Ana Souza", 2019)

m1.informacoes()
m2.informacoes()
