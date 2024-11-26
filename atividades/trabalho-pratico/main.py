from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
       
        self._nome = nome
        self._idade = idade
        self._matricula = matricula
        
        
    @abstractmethod
    def descricao(self):
        pass
        
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
       
        super().__init__(nome, idade, matricula)
        self._meus_livros = []
       
    def descricao(self):
        return f"Usuário Comum: {self._nome}, Matrícula: {self._matricula}, Livros Emprestados: {len(self._meus_livros)}"
    


class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
       
        super().__init__(nome, idade, matricula)
        
    def descricao(self):
        return f"Administrador: {self._nome}, Matrícula: {self._matricula}"
        
class ItemBiblioteca (ABC):
    def __init__(self, titulo, autor):
        
        self.titulo=titulo
        self.autor = autor
        self._status = 'Disponível'
        
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicado):
        super().__init__(titulo, autor)
        self.ano_publicado=ano_publicado
        
    def descricao(self):
        return f"Livro: {self.titulo} de {self.autor} ({self.ano_publicado}), Status: {self._status}"
        
   

usuario1 = UsuarioComum(nome="João Silva", idade=25, matricula="12345")
print(usuario1.descricao())

admin1 = Administrador(nome="Maria Oliveira", idade=30, matricula="98765")
print(admin1.descricao()) 

livro1 = Livro(titulo="Aprendendo Python", autor="João Pereira", ano_publicado=2020)
livro2 = Livro(titulo="Estruturas de Dados", autor="Maria Costa", ano_publicado=2019)

print(livro1.descricao())  
print(livro2.descricao())