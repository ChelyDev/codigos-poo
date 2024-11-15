from abc import ABC, abstractmethod

class Veiculo(ABC): 
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano

    def descricao(self): 
        return f"{self.marca} - {self.modelo} - {self.ano}"
    
    def adicionais(self): 
       pass

    @abstractmethod
    def tipo_combustivel(self): 
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas:int):
        super().__init__(marca, modelo, ano,)
        self.portas = portas  
       
    def tipo_combustivel(self): 
        return "Gasolina"
    
    def adicionais(self):
        return f"{self.portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas:int):
        super().__init__(marca, modelo, ano,)
        self.cilindradas = cilindradas  

    def tipo_combustivel(self): 
        return "Gasolina"
    
    def adicionais(self):
        return f"{self.cilindradas} cilindradas"
        

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima:int):
        super().__init__(marca, modelo, ano,)
        self.carga_maxima = carga_maxima  
   
    def tipo_combustivel(self): 
        return "Diesel"

    def adicionais(self):
        return f"{self.carga_maxima} carga_maxima"


def mostrar_informacoes(veiculo: Veiculo):
    print(veiculo.descricao())
    print(veiculo.adicionais())
    print(f"Tipo de combustível: {veiculo.tipo_combustivel()}")


carro = Carro("Chevrolet", "Impala", 1967, 4)
moto = Moto("Harley-Davidson", "Dyna Super Glide", 2005, 1.450)
caminhao = Caminhao("Mercedes-Benz", "Actros", 2023, 26.000)

mostrar_informacoes(carro)
mostrar_informacoes(moto)
mostrar_informacoes(caminhao)