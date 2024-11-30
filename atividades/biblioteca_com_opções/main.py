#caro Wellington, resolvi juntar o código da calculadora de
#estrutura de software com essa atividade pois achei que com 
#as opçoes o código ficaria mais organizado de inicializar, pois
#eu estava me perdendo mais do que cego em tiroteio.
#Att. Michely 

#código da calculadora em questão:

'''
print("Olá, bem vindo a sua calculadora! Escolha qual operação você gostaria de fazer:\n\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n")
escolha = input("Digite sua escolha: ")

m= float(input("Digite o primeiro número:"))
r= float(input("Digite o segundo número:"))

if escolha == '1':
    print(m + r)
elif escolha == '2':
    print(m - r)
elif escolha == '3':
    print(m * r)
elif escolha == '4':
    if r == 0:
        print("Divisão por 0 não permitida.")
    else:
        print(m / r)
else:
    print("Escolha inválida")
    
'''

#class base Pessoa (abstrata)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade 
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

#class UsuarioComum herda de Pessoa
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  #chama o construtor da classe base
        self.matricula = matricula 
        self.livros_emprestados = [] 

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3:  
            if livro.disponivel:  #verifica se o livro está disponível para empréstimo
                self.livros_emprestados.append(livro)
                livro.emprestar()  #marca o livro como emprestado
                print(f"Livro '{livro.titulo}' emprestado com sucesso!")
            else:
                print(f"Livro '{livro.titulo}' não está disponível.")
        else:
            print("Você já atingiu o limite de 3 livros emprestados!")
    
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            print(f"Livro {livro.titulo} devolvido com sucesso!")
        else:
            print("Você não tem esse livro emprestado.")
    
    def exibir_livros_emprestados(self):
        if self.livros_emprestados:
            print("Livros emprestados:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")
        else:
            print("Nenhum livro emprestado.")
            
class Administrador(UsuarioComum):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)  #chama o construtor da classe UsuarioComum
    
    #método exclusivo para o administrador cadastrar livros
    def cadastrar_livro(self, livros):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação: "))
        novo_livro = Livro(titulo, autor, ano_publicacao)
        livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    #método exclusivo para o administrador cadastrar usuários
    def cadastrar_usuario(self, usuarios):
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        matricula = int(input("Digite a matrícula do usuário: "))
        novo_usuario = UsuarioComum(nome, idade, matricula)
        usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

#classe ItemBiblioteca (abstrata)
class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo  #atributo de título
        self.autor = autor  #atributo de autor
    
    def exibir_informacoes(self):
        pass  #método que será implementado nas subclasses

#classe Livro herda de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor)  #chama o construtor da classe base
        self.ano_publicacao = ano_publicacao  #atributo de ano de publicação
        self.disponivel = True  #controle de disponibilidade do livro
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro {self.titulo} emprestado.")
        else:
            print(f"Livro {self.titulo} não está disponível para empréstimo.")
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Livro {self.titulo} devolvido.")
        else:
            print(f"Livro {self.titulo} já está disponível.")

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}")

#função principal que simula o menu do sistema
def menu():
    livros = [Livro("Você é insubstituível", "Augusto Cury", 2018),
              Livro("Teto para dois", "Beth O´leary", 2019),
              Livro("O Anticristo", "Friedrich Nietzsche", 2008),
              Livro("O futuro de uma ilusão", "Freud", 1927),
              Livro("Quente como o inferno", "Marcela Talavus", 2021)]
    
    usuarios = [UsuarioComum("Maria", 19, 4321), UsuarioComum("Wellington", 30, 12345)]
    administradores = [Administrador("Michely", 19, 35023403)]
    
    while True: #while True mantem o menu em execução até o usuário escolher a opção de sair
        print("\n1. Cadastrar livro (Administrador)")
        print("2. Cadastrar usuário (Administrador)")
        print("3. Empréstimo de livro")
        print("4. Devolver livro")
        print("5. Exibir livros disponíveis")
        print("6. Exibir usuários e seus livros emprestados")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            #apenas administrador pode cadastrar livro
            usuario_nome = input("Digite o nome do administrador: ")
            admin = next((a for a in administradores if a.nome == usuario_nome), None) #esse next é pra percorrer o código e ver se o nome do administrador é o mesmo q o usuário colcou
            if admin:
                admin.cadastrar_livro(livros)
            else:
                print("Administrador não encontrado.")
                
        elif escolha == '2':
            #spenas administrador pode cadastrar usuário
            usuario_nome = input("Digite o nome do administrador: ")
            admin = next((a for a in administradores if a.nome == usuario_nome), None)
            if admin:
                admin.cadastrar_usuario(usuarios)
            else:
                print("Administrador não encontrado.")

        elif escolha == '3':
            usuario_nome = input("Digite o nome do usuário para empréstimo: ")
            livro_titulo = input("Digite o título do livro para empréstimo: ")
            usuario = next((u for u in usuarios if u.nome == usuario_nome), None)
            livro = next((l for l in livros if l.titulo == livro_titulo), None)
            if usuario and livro:
                usuario.emprestar_livro(livro)
                livro.emprestar()
            else:
                print("Usuário ou livro não encontrado.")

        elif escolha == '4':
            usuario_nome = input("Digite o nome do usuário para devolução: ")
            livro_titulo = input("Digite o título do livro para devolução: ")
            usuario = next((u for u in usuarios if u.nome == usuario_nome), None)
            livro = next((l for l in livros if l.titulo == livro_titulo), None)
            if usuario and livro:
                usuario.devolver_livro(livro)
                livro.devolver()
            else:
                print("Usuário ou livro não encontrado.")

        elif escolha == '5':
            print("\nLivros disponíveis:")
            for livro in livros:
                livro.exibir_informacoes()
                

        elif escolha == '6':
            print("\nUsuários e seus livros emprestados:")
            for usuario in usuarios:
                print(f"\n{usuario.nome}:")
                usuario.exibir_livros_emprestados()

        elif escolha == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

#chama a função principal para rodar o sistema
menu()
