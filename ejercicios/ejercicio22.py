# Ejercicio 22
# Escribe un programa que administre el inventario de una tienda. 
# El programa debe permitir agregar nuevos productos, 
# actualizar las cantidades de los productos existentes, y mostrar el inventario actual.

inventario = {
    "producto1" : {
        "nombre" : "producto1",
        "cantidad" : 132
    },
    "producto 2" : {
        "nombre" : "producto 2",
        "cantidad" : 1
    }
}

while True:
    print(" Bienvenido al programa de inventario.\n",
          " En este programa lo que podes hacer es:\n",
          " 1 - Agregar productos.\n",
          " 2 - Ver inventario actual.\n",
          " 3 - Actualizar productos existentes.")
    user_choice = input(" Ingrese el numero de la opcion que deseas elegir: ")
    if user_choice == "1":
        nombre = input(" Ingrese el nombre del producto que desea agregar: ")
        cantidad = input(" Ingrese la cantidad del producto que desea agregar: ")
        print(f" se va a agregar el producto: {nombre} con la cantidad: {cantidad}, desea modificar? ")
        user__choice = input(" Ingrese SI para modificar, ingrese No para agregar el producto: ").lower().strip()
        
        inventario[nombre] = {}
        inventario[nombre]["nombre"] = nombre
        inventario[nombre]["cantidad"] = cantidad
        print(inventario)
        
    elif user_choice == "2":
        for i in inventario.keys():
            print(i)
            a = inventario[i]["cantidad"]
            print(f"la cantidad es: {a}")
        
    elif user_choice == "3":
        print(" Los productos en existencias son: ")
        contador = 0
        for i in inventario.keys():

            print(f" {contador} Nombre: {i}\n",
                  f" Cantidad: {inventario[i]["cantidad"]}")
            contador += 1
        user_input = input(" Ingrese el nombre de producto para modificarlo: ")
        print(inventario[user_input])
        usr_choice = input(" Seleccione 1 para modificar el nombre, seleccione 2 para modificar la cantidad")
        if user_choice == "1":
            inventario[user_input]["nombre"] = input(" Ingrese el nuevo nombre: ")
    elif user_choice == "4":
        pass
    else:
        print(" El numero ingresado no corresponde a ninguna opcion.")