from ejercicios.ejercicio1 import promedios
from ejercicios.ejercicio2 import numero_pi
from ejercicios.ejercicio3 import saber_numero
from ejercicios.ejercicio4 import aprobo

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\33[94m"
MAGENTA = "\33[95m"
CYAN = "\33[96m"
TITULO = "\33[4;97m"
RESET = "\033[0m"

# Algo para agregar pueden ser colores en la terminal, es una verga asi

validacion = True
while validacion:
	print('\n', f"{TITULO}Estos son los ejercicios que hice en el cursillo {RESET}", '\n'
			f"  {TITULO}de ingreso en el I.S.P.C {RESET}", '\n' 
			'\n')
	print(" Hasta ahora tenemos estos problemas para que pruebes:")
	print('\n', f"{ROJO} Ejercicio 1 {RESET}- Promedios "
			'\n', f"{VERDE} Ejercicio 2 {RESET}- Numero pi"
			'\n', f"{AMARILLO} Ejercicio 3 {RESET}- Numero mayor a 10 o menor a 0?"
			'\n', f"{AZUL} Ejercicio 4 {RESET}- Verificador de nota", '\n'
			'\n', " - presione 1111 para salir")
	user_input = input(" Ingrese el numero del problema para ejecutarlo: ")
	if user_input == "1":	
		promedios()
	elif user_input == "2":
		numero_pi()
	elif user_input == "3":
		saber_numero()		
	elif user_input == "4":
		aprobo()
	elif user_input == "1111":
		break
	
