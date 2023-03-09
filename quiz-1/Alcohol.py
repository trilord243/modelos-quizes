from Bebida import Bebida



class Alcohol(Bebida):
    def __init__(self,nombre,marca,disponible,grado,tipo):
        self.grado=grado
        self.tipo=tipo
        super().__init__(nombre,marca,disponible)
        
    
    def mostrar(self):
        
        
        super().mostrar()
        
        print("Grado: ",self.grado)
        print("Tipo: ",self.tipo)