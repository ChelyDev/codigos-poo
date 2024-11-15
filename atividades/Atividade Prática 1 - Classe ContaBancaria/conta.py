class conta_bancaria:
    def __init__(self, nome, deposito, saque,  saldo,):
        self.nome=nome
        self.deposito=deposito
        self.saque=saque
        self.saldo=saldo

    def __str__(self): 
        return f"{self.nome} - {self.deposito} - {self.saque} - {self.saldo}"
    
    def update_deposito(self, new_saldo):
        self.saldo = new_saldo
        print(f"{self.nome}, o saldo da sua conta foi atualizado para {self.deposito+self.saldo}")

    def update_saque(self, new_saque):
        if new_saque <= self.saldo:
            self.saque = new_saque
            self.saldo -= self.saque
            print(f"O saldo da conta {self.nome} foi atualizado para {self.saldo}")
        else:
            print(f"Saldo insuficiente para o saque. Seu saldo atual é de: {self.saldo}" )
        
    def update_saldo(self, new_saldo):
        self.saldo = new_saldo
        print(f"{self.nome}, o seu saldo foi atualizado para {self.deposito+self.saldo}")

    def update_saldo(self, new_saldo):
        self.saldo = new_saldo
        print(f"{self.nome}, o seu saldo foi atualizado para foi atualizado para {(self.saldo+self.deposito)-self.saque}")

    def __str__(self):
        return f"Dados da conta: {self.nome} - Saldo R$: {self.saldo:.2f}"


nome=input("Informe o seu nome: ")
p1 = conta_bancaria(nome, 0, 0, 0)
deposito=float(input("Informe o valor do depósito: "))
p1.update_deposito(deposito)
saque=float(input("Informe o valor do saque: "))
p1.update_saque(saque)

print(p1)