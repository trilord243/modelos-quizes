from Flower import Flower
from Verficar import input_numerico
clase=[]
flores=[]
semillas=[]
aparte=[]
class App:
    def __init__(self):
        pass
    
    def registrar_producto(self):
        id_f= input_numerico("Ingrese el id del producto: ")
        name=input("Ingrese el nombre del producto: ")
        stock=input("Ingrese el stock del producto: ")
        colores=input("Ingrese el colores del producto: ")
        tipo=input("Ingrese el tipo del producto: ")
        b=Flower(id_f,name,tipo,stock,colores)
        clase.append(b)
    
    def ver_producto(self):
      for i in range(len(clase)):
    
       
          if clase[i].type=="Flower":
              flores.append(clase[i])
          elif clase[i].type=="Semilla":
              flores.append(clase[i])
          else:
              aparte.append(clase[i])
    
                   
       
       
        
    def productos(self):
        print("FLORES\n")
        for i in range(len(flores)):
            print(flores[i])
        print("\nSEMILLAS\n")
        for i in range(len(semillas)):
            print(semillas[i])
            
        print("\nAPARTE\n")
        for i in range(len(aparte)):
            print(aparte[i])
        
            
                
               

        
    def start(self):
        menu=True
        while menu:
            print("Ingrese una opcion: ")
            print("1.Registrar Producto")
            print("2.Ver Producto") 
            opcion=input("Ingrese una opcion: ")
            if opcion=="1":
                self.registrar_producto()
            elif opcion=="2":
                self.ver_producto()
                self.productos() 
            else:
                menu=False  
       
         