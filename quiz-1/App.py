from Alcohol import Alcohol
from Refresco import Refresco
almacen_desactualizado = {
            "Alcohol":
        [
        	{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        	{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
        	{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ],
    
        "Refresco":
        [
        	{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        	{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        	{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
        ] 
}

almacen_actualizado=[]
class App:
    def __init__(self):
        pass
    
    
    
    
    #Metodo para actualizar el almacen usando clases con Refresco y Alcohol
    def actualizar_almacen(self):
        for key, item in almacen_desactualizado.items():
            if key == "Alcohol":
             for i in range(len(item)):
                 b=Alcohol(item[i]["nombre"],item[i]["marca"],item[i]["grado"],item[i]["tipo"],item[i]["disponible"])
                 almacen_actualizado.append(b)
            elif key == "Refresco":
                for i in range(len(item)):
                    b=Refresco(item[i]["nombre"],item[i]["marca"],item[i]["azucar"],item[i]["sabor"],item[i]["disponible"])
                    almacen_actualizado.append(b)
                    
                
    

    def ver_inventario(self):
        for i in range(len(almacen_actualizado)):
            almacen_actualizado[i].mostrar()
    
    
    def eliminar_bebidas(self):
        self.ver_inventario()
        print("Porfavor escoja el nombe de la bebida que desea eliminar")
        opcion=input("Escoja la bebida que desea eliminar: ")
        for i in range(len(almacen_actualizado)):
            if opcion==almacen_actualizado[i].nombre:
                almacen_actualizado.pop(i)
                print("Bebida eliminada")
                break
            else:
                print("No se encuentra la bebida")
                break
        
       
    
    #Esto es un menu
    def menu(self):
        print(""" Bienvenido a la aplicación Porfavor escoge una opción:
        
        1.Ver inventario
        2.Eliminar bebdas del inventario 
        
        Para salir de la aplicación, escriba cualquier otra tecla 
              
              
              """)
        opcion=input("Ingrese una opción: ")
        return opcion
    
    
    
    
    #App de start
    def start(self):
        self.actualizar_almacen()
        print(almacen_actualizado)
        validacion_menu=True
        while validacion_menu:
            opcion=self.menu()
            if opcion=="1":
                self.ver_inventario()
            elif opcion=="2":
                self.eliminar_bebidas()
            else:
                validacion_menu=False
            
            
    
