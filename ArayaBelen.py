import os
os.system("cls")


stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], }

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

def actualizar_precio(modelo, p):
    modelo=input("Ingrese el modelo a actualizar: ")
    if not modelo in stock:
        print("El modelo no existe en la lista")
    else:
        for i in range(len(stock)):
            if stock[i][productos]==modelo:
                pass

def busqueda_precio(p_min, p_max):
    pass

def menu():
    print('''
*** MENU PRINCIPAL ***
1.	Stock marca.
2.	Búsqueda por precio.
3.	Actualizar precio.
4.	Salir.

''')

while True:
    menu()
    try:
        opcion=int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe seleccionar una opción válida!!")
        continue
    if opcion==1:
        stock_marca=input("Ingrese marca a consultar: ").lower()
        encontrado=False
        for s in stock:
            if s[stock]==stock_marca:
                print(f"El stock es: {stock}")
                encontrado=True
            elif not encontrado:
                print("No se encontró la marca")
                break
    elif opcion==2:
        pass
    elif opcion==3:
        actualizar_precio
    elif opcion==4:
        print("Programa finalizado")
        break
