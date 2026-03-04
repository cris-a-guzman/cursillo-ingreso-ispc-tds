# Ejercicio 9
# Escribe un programa que permita realizar la división de dos números siempre
# y cuando el denominador no sea 0.

def division_simple():
    while True:
        print(" En este programa vamos a hacer una division.\n")
        try:
            user_input = int(input(" Ingresa el numerador: "))
            user_input2 = int(input(" Ingresa el denominador: "))
            if user_input2 == 0:
                print(" No se puede hacer division por 0, queres romper el mundo?")
            else:
                div = user_input / user_input2
                print(f" El resultado de la division de {user_input} y {user_input2} es: {div}")
            user_choice = input(" Queres hacer otra division? SI o NO").lower()
            if user_choice == "no":
                break
        except ValueError:
            print(" Lo que ingresaste no es un numero, intenta de nuevo")