class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Carro: {self.marca} {self.modelo} - Ano: {self.ano}")


# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Ford", "Fiesta", 2018)

carro1.detalhes()
carro2.detalhes()
