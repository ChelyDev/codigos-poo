#aula 02/09 + atualizações

#create class product
class Product: 
    #é um padrão a classe começar com letra maiúscula e não ser no plural
    def __init__(self, name, price, qtd):
        self.name=name
        self.price=price
        self.qtd=qtd

          #a função init é um construtor 
          #self declara ela mesma
          #self chama o atributo

    def __str__(self): 
        return f"{self.name} - {self.price} - {self.qtd}"
    
    #method update_price
    def update_price(self, new_price):
        self.price = new_price
        print(f"O preço do produto {self.name} foi atualizado para {self.price:.2f}")

    #method update_qtd
    def update_qtd(self, new_qtd):
        self.qtd = new_qtd
        print(f"O estoque do produto {self.name} foi atualizado para {self.qtd}")
        
#create a instance of a product
p1 = Product("laptop", 1000, 5)
#chama a função e atualiza o preço
p1.update_price(899)
p1.update_qtd(4)
print(p1)
        