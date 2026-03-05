# Ejercicio 17
# Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario 
# adivinar el número. El programa debe brindar pistas (ej. el número secreto es mayor) 
# y debe continuar pidiendo al usuario que adivine hasta que acierte. 
# Al finalizar, debe mostrar el número de intentos.
import random

def adivinar_numero():
    print(" En este programa voy a elegir un numero entr 1 y 100\n"
          " Y vos vas a tratar de adivinarlo")
    x = random.randint(1,100)
    contador = 0
    while True:
        try:
            y = int(input(" Ingresa el numero que crees que es: "))
            contador += 1
            if y <= 0 or y >= 100:
                print(" Tu numero no es valido, el juego comprende numeros entre 1 y 100")
            else:
                if y > x:
                    print(f" Tu numero ({y}) es mayor al numero que elegi.")
                elif y < x:
                    print(f" Tu numero({y}) es menor al numero que elegi.")
                elif y == x:
                    print(f" FELICIDADES, el numero era {x}\n"
                          f" Lo conseguiste en {contador} intentos!")
                    break
        except ValueError:
            print(" Lo ingresado no fue un numero")
