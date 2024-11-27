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
    

    def pegar_livro(self, livro):
        if len(self._meus_livros) < 3 and livro._status == 'Disponível':
            self._meus_livros.append(livro)
            livro._status = 'Emprestado'
            return f"Livro '{livro.titulo}' emprestado com sucesso!"
        return "Não foi possível emprestar o livro."

    def devolver_livro(self, livro):
        if livro in self._meus_livros:
            self._meus_livros.remove(livro)
            livro._status = 'Disponível'
            return f"Livro '{livro.titulo}' devolvido com sucesso!"
        return "Este livro não foi emprestado para este usuário."


class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.emprestar_livro = []
        
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
        

class Biblioteca:
    def __init__(self):
        
        self.livros = []  
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, usuario, livro):
        if len(usuario._meus_livros) < 3 and livro._status == 'Disponível':
            usuario._meus_livros.append(livro)
            livro._status = 'Emprestado'
            return f"Livro {livro.titulo} emprestado para {usuario._nome}"
        else:
            return "Empréstimo não realizado. Verifique as condições."

    def devolver_livro(self, usuario, livro):
        if livro in usuario._meus_livros:
            usuario._meus_livros.remove(livro)
            livro._status = 'Disponível'
            return f"Livro {livro.titulo} devolvido."
        else:
            return "Este livro não foi emprestado para esse usuário."

    def livros_disponiveis(self):
        return [livro for livro in self.livros if livro._status == 'Disponível']

    def usuarios_com_livros(self):
        return [usuario.descricao() for usuario in self.usuarios if len(usuario._meus_livros) > 0]
                
   

usuario1 = UsuarioComum(nome="João Silva", idade=25, matricula="12345")
print(usuario1.descricao())
usuario2 = UsuarioComum(nome="Michely", idade=19, matricula="54321")

admin1 = Administrador(nome="Maria Oliveira", idade=30, matricula="98765")
print(admin1.descricao()) 

livro1 = Livro(titulo="Aprendendo Python", autor="João Pereira", ano_publicado=2020)
livro2 = Livro(titulo="Estruturas de Dados", autor="Maria Costa", ano_publicado=2019)

print(livro1.descricao())  
print(livro2.descricao())

biblioteca = Biblioteca()
biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)


print(biblioteca.emprestar_livro(usuario1, livro1))  
print(biblioteca.emprestar_livro(usuario1, livro2))  


livro3 = Livro(titulo="Algoritmos Avançados", autor="Carlos Souza", ano_publicado=2021)
biblioteca.cadastrar_livro(livro3)
print(biblioteca.emprestar_livro(usuario1, livro3))  


print(biblioteca.devolver_livro(usuario1, livro1))


print("Livros disponíveis:")
for livro in biblioteca.livros_disponiveis():
    print(livro.descricao())

print("Usuários com livros emprestados:")
for usuario in biblioteca.usuarios_com_livros():
    print(usuario.descricao())