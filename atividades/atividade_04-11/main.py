class Funcionario: 
    
    def __init__(self, nome, cargo, salario_inicial=0):
        self.nome=nome
        self.cargo=cargo
        self.__salario=salario_inicial

    def consultar_salario(self):
        return self.__salario
    

    def aumentar_salario(self, valor):
        if valor > 0:
            self.__salario += valor
            print(f"Bônus de R${valor} aplicado. Salário atual: R${self.__salario}")
        else:
            print("Valor de aumento inválido.")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus_salario):
       
        super().__init__(nome, cargo, salario)
        self.bonus_salario = bonus_salario 

    def aplicar_bonus(self):
        bonus = self.bonus_salario
        self.aumentar_salario(bonus)


def exibir_detalhes_conta(conta):
    print(f"Funcionário: {conta.nome}")
    print(f"Cargo: {conta.cargo}")
    print(f"Salário atual: R${conta.consultar_salario()}")


conta_func = Funcionario("Michely", "Aux.Adm", 1412)
exibir_detalhes_conta(conta_func)

conta_ger = Gerente("Railson", "Gerente", 1412, 600)
conta_ger.aplicar_bonus()  
