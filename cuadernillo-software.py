from ejercicios.ejercicio1 import promedios
from ejercicios.ejercicio2 import numero_pi
from ejercicios.ejercicio3 import saber_numero
from ejercicios.ejercicio4 import aprobo
from ejercicios.ejercicio5 import radio_circulo
from ejercicios.ejercicio6 import calcular_grados
from ejercicios.ejercicio7 import nota_usuario
from ejercicios.ejercicio8 import numero_impar_par
from ejercicios.textos import *

# Algo para agregar pueden ser colores en la terminal, es una verga asi
# A todos estos programas le podemos agregar un json para que queden guardados los datos
# Todos estos programas pueden ir guardados en un diccionario
# Hay varias cosas que pueden ir dentro de una funcion para no repetir codigo (como salir de los ejercicios)

menu_bienvenida()
menu_pag1()
iterador = 1

validacion = True
while validacion:
	user_input = input(" Ingrese el numero del problema para ejecutarlo: ")
	if user_input == "1":	
		promedios()
	elif user_input == "2":
		numero_pi()
	elif user_input == "3":
		saber_numero()		
	elif user_input == "4":
		aprobo()
	elif user_input == "5":
		radio_circulo()
	elif user_input == "6":
		calcular_grados()
	elif user_input == "7":
		nota_usuario()
	elif user_input == "8":
		numero_impar_par()
	elif user_input == "1111":
		break
	elif user_input == "+":
		if iterador == 1:
			menu_pag2()
			iterador = 2
		elif iterador == 2:
			#menu_pag3()
			print(" Aca va el menu 3")
			iterador = 3
		elif iterador == 3:
			menu_pag1()
			iterador = 1
	elif user_input == "-":
		if iterador == 1:
			# menu_pag3()
			iterador = 3
		elif iterador == 2:
			menu_pag1()
			iterador = 1
		elif iterador == 3:
			menu_pag2()
			iterador = 2

	
