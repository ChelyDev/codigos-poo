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
        
#create a instance of a product
p1 = Product("laptop", 1000, 5)

print(p1)
        