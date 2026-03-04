# Ejercicio 10
# Pide al usuario un número del 1 al 7 
# y muestra el nombre del día de la semana correspondiente (1 = lunes, 7 = domingo).

def dia_semana():
    print(" En este programa te voy a pedir que ingreses un numero del 1 al 7 y te muestro \n"
          " A que dia de la semana corresponde.")
    dia_semana = {
        1 : 'lunes',
        2 : 'martes',
        3 : 'miercoles',
        4 : 'jueves',
        5 : 'viernes',
        6 : 'sabado',
        7 : 'domingo'
    }
    while True:

        user_input = int(input(" Ingrese un numero del 1 al 7: "))
        if user_input >= 1 and user_input <= 7:
            print(f" El dia de la semana n° {user_input} corresponde al {dia_semana[user_input]}.")
        else:
            print(f" El numero {user_input} no corresponde a ningun dia de la semana.")