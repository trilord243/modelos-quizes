class Flower:
    def __init__(self,id,name,type,stock,colors):
        self.id = id
        self.name = name
        self.type = type
        self.stock = stock
        self.colors = colors
    
    def __str__(self):
      return f""" id: {self.id}, name: {self.name}, type: {self.type},stock: {self.stock}, colors: {self.colors}"""           
    