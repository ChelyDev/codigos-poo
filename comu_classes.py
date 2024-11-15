class Livro:
    def __init__(self, pessoa, titulo):
        self.pessoa = pessoa
        self.titulo = titulo
        self.ler_livro = False

    def ler_livro(self, titulo):
        self.titulo = titulo
        print(f"{self.pessoa} está lendo o livro {self.titulo}")

    def nao_leu(self, livro):
        self.livro = livro
        print(f"{self.pessoa} não está lendo o livro {self.titulo}")

class Pessoa:
    def __init__(self, pessoa):
        self.pessoa=pessoa


pessoa=input("Informe o seu nome: ")
titulo=input("Informe o titulo do livro: ")
lido=input("Você está lendo o livro?: ")






