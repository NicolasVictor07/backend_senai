class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_estoque(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade em estoque: {self.quantidade}")


p1 = Produto("Parafuso", 0.50, 1000)
p2 = Produto("Chave de Fenda", 12.90, 150)

p1.mostrar_estoque()
p2.mostrar_estoque()
