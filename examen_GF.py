#productos= {modelo: [marca,pantalla,RAM,disco,GB de DD,procesador,video],..}
Productos = {"8475HD": ["HP",15.6,"8GB","DD","1T", "intel Core i5", "Nvidia GTX1050"],
             "2175HD":["lenovo",14,"4GB","SSD","512GB", "intel Core i5", "Nvidia GTX1050"],
             "JjfFHD":["ASUS",14,"16GB","SSD","256GB", "intel Core i7", "Nvidia RTX2080Ti"],
             "fgdxFHD":["HP",15.6,"8GB","DD","1T", "intel Core i3", "integrada"],
             "GF75HD":["Asus",15.6,"8GB","DD","1T", "intel Core i7", "Nvidia GTX1050"],
             "123FHD":["Lenovo",14,"6GB","DD","1T", "AMD Ryzen 5", "integrada"],
             "342FHD":["Lenovo",15.6,"8GB","DD","1T", "AMD Ryzen 7", "Nvidia GTX1050"],
             "UWU131HD":["Dell",15.6,"8GB","DD","1T", "AMD Ryzen 3", "Nvidia GTX1050"],
                   
}
            
#Stock={modelo:[precio,stock],..}

Stock={      "8475HD": [387990,10],
             "2175HD":[327990,4],
             "JjfFHD":[424990,1],
             "fgdxFHD":[664990,21],
             "GF75HD":[749990,2],
             "123FHD":[290890,32],
             "342FHD":[444990,7],
             "UWU131HD":[349990,1],}

def menu():
    print('Menú de productos Pybooks')
    print('~'*20)
    print("""
    1.- Stock de marca.
    2.- Busqueda por precio.
    3.- Actualizar precio.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op

def Stock_marca(Marca):
    contador = 0
    totalcomputadores=0
    Marca =input ("Ingrese Marca que desea buscar: ").strip()
    for parte, parte2 in Productos.items():
         if Marca==parte2 [0]:
             contador+=1
             totalcomputadores+= +1
         if contador != 0:
             print(f"El stock es {totalcomputadores}")
         else: 
             print("No hay productos con ese nombre de marca")
    
 

def Busqueda_Precio(p_min, p_max):
    while True:
     if Stock != 0:
          p_min= float (input("ingrese precio minimo por favor"))
          p_max= float (input("ingrese el precio maximo por favor"))
          for parte, parte2 in  Stock.items():
            if parte2[0]>=p_min and parte2[0] <=p_max:
                print (f" Se han encontrado productos, hay {parte2[1]} a {parte2[0]} pesos")
                break


def Actualizar_precio(modelo, p):
     modelo= input("ingresa el modelo a actualizar el precio")
     if modelo in Stock:
         modelo[Stock[0]]
         print(modelo)
         return
            
  


     #examen funciones
import examen_GF as fc
opcion = ''
Marca = {}
precio={}
valor={}

while opcion != '4':
    opcion = fc.menu()
    if opcion == '4':
        print('Programa Terminado.')
    elif opcion == '1':
        print(' Buscar marca')
        Marca = fc.Stock_marca(Marca)
      
    elif opcion == '2':
        print('buscar precio')
        fc.Busqueda_Precio(valor,Marca)
    elif opcion == '3':
        print('')
        precio = fc.Actualizar_precio(valor,Marca)
        print(Marca)
   
    else:
        print('Error: Opción NO Existe')  
       
           
       
        