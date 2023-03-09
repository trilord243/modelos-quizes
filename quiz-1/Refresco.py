from Bebida import Bebida

class Refresco(Bebida):
    def __init__(self,nombre,marca,disponible,azucar,sabor):
        self.azucar = azucar
        self.sabor = sabor
        super().__init__(nombre,marca,disponible)
        
    
    def mostrar(self):  
        super().mostrar()
        print(f" AZUCAR: {self.azucar}")
        print(f" SABOR: {self.sabor}")
        