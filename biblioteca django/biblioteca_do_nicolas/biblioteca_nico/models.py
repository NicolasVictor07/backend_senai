from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nome}-{self.data_nascimento}-{self.biografia}"


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    descricao = models.TextField()

    
    def __str__(self):
        return f"{self.titulo}-{self.isbn}-{self.descricao}"
    
class Livro_Autor(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

class Livro_Categoria(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Associacao(models.Model):
    tipo = models.CharField(max_length=100)
    beneficios = models.TextField()
    def __str__(self):
        return f"{self.tipo}-{self.beneficios}"

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    identificacao = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField()
    associacao = models.ForeignKey(Associacao,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nome} - {self.identificacao} - {self.email} - {self.data_cadastro} - {self.associacao}"

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    data_devolucao_limite = models.DateField()

    def __str__(self):
        return (
            f"Usuário: {self.usuario.nome} | "
            f"Livro: {self.livro.titulo} | "
            f"Empréstimo: {self.data_emprestimo} | "
            f"Devolução: {self.data_devolucao if self.data_devolucao else 'Não devolvido'} | "
            f"Limite: {self.data_devolucao_limite}"
        )
