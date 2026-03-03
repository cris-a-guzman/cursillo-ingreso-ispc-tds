from ejercicios.ejercicio1 import promedios
from ejercicios.ejercicio2 import numero_pi

# Algo para agregar pueden ser colores en la terminal, es una verga asi


validacion = True
while validacion:
	print(" Estos son los ejercicios que hice en el cursillo", '\n'
			" de ingreso en el I.S.P.C", '\n' 
			'\n')
	print(" Hasta ahora tenemos estos problemas para que pruebes por ahora")
	print('\n', " 1 - Ejercicio 1 - Promedios "
			'\n', " 2 - Ejercicio 2 - Numero pi"
			'\n', " presione 1111 para salir")
	user_input = input(" Ingrese el numero del problema para ejecutarlo: ")
	if user_input == "1":	
		promedios()
	elif user_input == "2":
		numero_pi()
	elif user_input == "1111":
		break
	
