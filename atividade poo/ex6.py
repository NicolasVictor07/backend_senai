class Aluno:
    def __init__(self, nome, curso, nota_final):
        self.nome = nome
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        resultado = "aprovado" if self.nota_final >= 7 else "reprovado"
        print(f"Aluno: {self.nome} | Curso: {self.curso} | Nota Final: {self.nota_final} | Resultado: {resultado}")



a1 = Aluno("João", "Eletricista Industrial", 8.5)
a2 = Aluno("Maria", "Soldagem", 6.0)

a1.status()
a2.status()
