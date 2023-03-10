from Flower import Flower
from Verficar import input_numerico
clase=[]
flores=[]
semillas=[]
aparte=[]
vendor_1 = [
{ "product_id": 5, "customer_id": 333, "amnt": 1 },
{ "product_id": 5, "customer_id": 1010, "amnt": 2 },
{ "product_id": 3, "customer_id": 1111, "amnt": 3 },
{ "product_id": 2, "customer_id": 222, "amnt": 6 },
{ "product_id": 6, "customer_id": 444, "amnt": 7 },
{ "product_id": 1, "customer_id": 1111, "amnt": 20 },
]

vendor_2 = [
{ "product_id": 6, "customer_id": 888, "amnt": 10 },
{ "product_id": 1, "customer_id": 123, "amnt": 5 },
{ "product_id": 2, "customer_id": 321, "amnt": 4 },
{ "product_id": 4, "customer_id": 555, "amnt": 2 },
{ "product_id": 1, "customer_id": 777, "amnt": 1 },
]

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
        
            
    def modulo_inventario(self):
        ventas = []
        i, j = 0, 0

        while i < len(vendor_1) and j < len(vendor_2):
            if vendor_1[i]["amnt"] <= vendor_2[j]["amnt"]:
                ventas.append(vendor_1[i])
                i += 1
            else:
                ventas.append(vendor_2[j])
                j += 1

        while i < len(vendor_1):
            ventas.append(vendor_1[i])
            i += 1

        while j < len(vendor_2):
            ventas.append(vendor_2[j])
            j += 1

        for i in range(len(ventas)):
            min_index = i
            for j in range(i + 1, len(ventas)):
                if ventas[min_index]["amnt"] > ventas[j]["amnt"]:
                    min_index = j
            ventas[i], ventas[min_index] = ventas[min_index], ventas[i]

        print(ventas)
               

        
    def start(self):
        menu=True
        while menu:
            print("Ingrese una opcion: ")
            print("1.Registrar Producto")
            print("2.Ver Producto") 
            print("3 Modulo inventario")
            opcion=input("Ingrese una opcion: ")
            if opcion=="1":
                self.registrar_producto()
            elif opcion=="2":
                self.ver_producto()
                self.productos() 
            elif opcion=="3":
                self.modulo_inventario()
            else:
                menu=False  
       
         