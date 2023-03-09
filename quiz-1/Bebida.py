class Bebida:
    def __init__(self,nombre,marca,disponible):
        self.nombre=nombre
        self.marca=marca
        self.disponible=disponible
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nMarca: {self.marca}\nDisponible: {self.disponible}"
    
    def mostrar(self):
        print(self.__str__())