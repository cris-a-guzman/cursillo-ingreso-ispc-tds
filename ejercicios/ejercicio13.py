# Ejercicio 13
# Escribe un programa que solicite al usuario el precio y la cantidad de un producto.
# Clasifique el producto como "caro" si el precio es mayor de $100 o si la cantidad es menor que 10 
# y el precio es mayor de $50. De lo contrario, clasifíquelo como "barato".
# Incluye condiciones para manejar valores falsos (0 o vacío).

def precio():
    print(" En este programa vas a ingresar el precio y cantidad de un producto\n"
          " Y en base a eso te digo si es caro o barato")
    try:
        user_input1 = int(input(" Ingrese el precio: $"))
        user_input2 = int(input(" Ingrese la cantidad: "))

        if user_input1 <= 0 or user_input2 <=0:
            print(" No ingresaste un numero valido")
        else:

            if user_input1 > 100:
                print(" Te cagaron, el producto esta caro.")
            elif user_input1 > 50 and user_input2 < 10:
                print(" Te cagaron, esta caro.")
            else:
                print(" Esta barato")
    except ValueError:
        print(" Se pueden ingresar solo numeros enteros")