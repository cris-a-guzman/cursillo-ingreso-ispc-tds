# Ejercicio 21
# Crea una tupla de números y verifica si el número ingresado por el usuario existe.

def tuplas():
    print(" En este programa vamos a ver si el numero que ingresas se encuentra en mi tupla")
    numeros = (17, 3, 42, 8, 29, 14, 56, 1, 33, 21)
    while True:
        try:
            user_input = int(input(" Ingrese el numero: "))
            if user_input in numeros:
                print(" Tu numero aparece en mi tupla") # Aca podemos mostrar la posicion en la que aparece el numero
            else:
                print(" Tu numero no aparece en mi tupla")
            user_choice = input(" Desea intentarlo de nuevo? SI/NO").lower().strip()
            if user_choice == "no":
                print(" Volviendo al menu de inicio.")
                break
            

        except ValueError:
            print(f" El dato ingresado no corresponde a un numero ({user_input})")