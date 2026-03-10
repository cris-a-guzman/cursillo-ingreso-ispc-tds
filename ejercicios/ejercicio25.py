# Ejercicio 25
# Escribe una función que reciba una lista de números y devuelva el promedio.

def promedios_2():
    print(" En este programa vamos a realizar una lista de numeros y voy a devolver el promedio.")
    lista = []
    while True:
        user_input = input(" Presione 1 para crear la lista, presione 2 para crearla automaticamente")
        validacion = True
        if user_input == "1":
            while validacion:
                try:
                    print(" Vas a crear la lista.\n")
                    longitud = int(input(" Cuantos numeros queres que tenga la lista de numeros?\n"))
                    for i in range(longitud):
                        try:
                            numero = int(input(" Ingrese el numero: "))
                            lista.append(numero)
                        except ValueError:
                            print(" Lo ingresado no fue un numero.")
                except ValueError:
                    print(" Lo ingresado no fue un numero.")
        elif user_input == "2":
            while validacion:
                pass # a esto lo voy a terminar otro dia, no tengo ganas ahora
promedios_2()


