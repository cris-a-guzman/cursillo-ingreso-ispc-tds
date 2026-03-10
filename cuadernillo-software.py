from ejercicios.ejercicio1 import promedios
from ejercicios.ejercicio2 import numero_pi
from ejercicios.ejercicio3 import saber_numero
from ejercicios.ejercicio4 import aprobo
from ejercicios.ejercicio5 import radio_circulo
from ejercicios.ejercicio6 import calcular_grados
from ejercicios.ejercicio7 import nota_usuario
from ejercicios.ejercicio8 import numero_impar_par 
from ejercicios.ejercicio9 import division_simple
from ejercicios.ejercicio10 import dia_semana
from ejercicios.ejercicio11 import categoria_edad
from ejercicios.ejercicio12 import triangulo
from ejercicios.ejercicio13 import precio
from ejercicios.ejercicio14 import sumatoria
from ejercicios.ejercicio15 import contar_string
from ejercicios.ejercicio16 import contar_vocales
from ejercicios.ejercicio17 import adivinar_numero
from ejercicios.ejercicio18 import amigos
from ejercicios.ejercicio19 import ordenar_numeros
from ejercicios.ejercicio20 import contar_numeros
from ejercicios.ejercicio21 import tuplas
from ejercicios.textos import *

colores = ["\033[91m", "\033[92m", "\033[93m", "\33[94m", "\33[95m",
           "\33[96m"]
TITULO = "\33[4;97m"
RESET = "\033[0m"

# Algo para agregar pueden ser colores en la terminal, es una verga asi
# A todos estos programas le podemos agregar un json para que queden guardados los datos
# Hay varias cosas que pueden ir dentro de una funcion para no repetir codigo (como salir de los ejercicios)


pagina_0= {
	'1' : promedios,
	'2' : numero_pi,
	'3' : saber_numero,
	'4' : aprobo,
	'5' : radio_circulo,
	'6' : calcular_grados
}
pagina_1= {
    '7' : nota_usuario,
	'8' : numero_impar_par,
	'9' : division_simple,
	'10' : dia_semana,
	'11' : categoria_edad,
	'12' : triangulo
}
pagina_2= {
    '13' : precio,
	'14' : sumatoria,
	'15' : contar_string,
	'16' : contar_vocales,
	'17' : adivinar_numero,
	'18' : amigos
}
pagina_3= {
    '19' : ordenar_numeros,
	'20' : contar_numeros,
	'21' : tuplas
}
iterador = 0
paginas = [pagina_0, pagina_1, pagina_2, pagina_3]

def mostrar_pagina(pagina_actual):
	index_color = 0
	for clave, valor in pagina_actual.items():
		formateo = valor.__name__.replace("_", " ").title()
		if index_color == len(colores):
			index_color = 0
		print(f"{colores[index_color]} Ejercicio {clave} {RESET}- {formateo} ")
		
		index_color +=1
	print("\n Ingrese 0000 para salir del programa\n",
	   		f" {TITULO}Ingrese '+' para pasar a la siguiente pagina\n",
			f" Ingrese '-' para volver a la pagina anterior{RESET}\n")
	
print("Bienvenido al hub de ejercicios resueltos del\n",
	"cursillo de ingreso del I.S.P.C")

def pasar_pagina(pagina_actual):
	global iterador
	if iterador > len(pagina_actual):
		iterador = 0
	else:
		iterador += 1
	mostrar_pagina(pagina_actual)
	

while True:
	if iterador > 3:
		iterador = 0
	print(f" {TITULO}Pagina {iterador+1}{RESET}")
	mostrar_pagina(paginas[iterador])
	user_choice = input(" Ingrese el numero de ejercicio para ejecutar el programa: ")

	if user_choice == "+":
			pasar_pagina(paginas[iterador])
	elif user_choice == '0000':
		break
	elif user_choice not in paginas[iterador]:
		print(" El ejercicio no se encuentra en esta pagina")
	else: # aca va if user_choice > paginas[iterador] then "El ejercicio no se encuentra en esta pagina".........
		paginas[iterador][user_choice]()
		input("\nPresione ENTER para volver al menu...")
		
