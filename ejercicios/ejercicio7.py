# Ejercicio 7
# Escribe un programa que solicite al usuario una nota numérica entre 0 y 100, 
# y que muestre en pantalla un mensaje según la siguiente escala:
# Si la nota es 90 o más, mostrar: "Excelente".
# Si la nota está entre 70 y 89, mostrar: "Aprobado".
# Si la nota es menor a 70, mostrar: "Reprobado".

def nota_usuario():
    while True:
        try:
            user_input = int(input(" Ingrese la nota obtenida en la evaluacion: "))
            if user_input >= 0 and user_input <= 100:
                if user_input >= 90:
                    print('\n', " \033[92mExcelente.\033[0m")
                elif user_input >= 70 and user_input < 90:
                    print('\n', " \033[93mAprobado.\033[0m")
                elif user_input < 70:
                    print('\n', " \033[91mReprobado.\033[0m")
                else:
                    print("\033[91mAlgo Salio Mal\033[0m")
            else:
                print(" Tu nota no es valida.")
            user_choice = input(" Queres ingresar otra nota? Si (1) - No (2)")
            if user_choice == "2":
                break
        except ValueError:
            print(" \033[91mLo que ingresaste no es un numero, intenta de nuevo.\033[0m")