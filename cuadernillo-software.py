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

# Algo para agregar pueden ser colores en la terminal, es una verga asi
# A todos estos programas le podemos agregar un json para que queden guardados los datos
# Todos estos programas pueden ir guardados en un diccionario
# Hay varias cosas que pueden ir dentro de una funcion para no repetir codigo (como salir de los ejercicios)

menu_bienvenida()
menu_pag1()
iterador = 1
opciones_menu = {
	'1' : promedios,
	'2' : numero_pi,
	'3' : saber_numero,
	'4' : aprobo,
	'5' : radio_circulo,
	'6' : calcular_grados,
	'7' : nota_usuario,
	'8' : numero_impar_par,
	'9' : division_simple,
	'10' : dia_semana,
	'11' : categoria_edad,
	'12' : triangulo,
	'13' : precio,
	'14' : sumatoria,
	'15' : contar_string,
	'16' : contar_vocales,
	'17' : adivinar_numero,
	'18' : amigos,
	'19' : ordenar_numeros,
	'20' : contar_numeros,
	'21' : tuplas
}

validacion = True
while validacion:
	user_input = input(" Ingrese el numero del problema para ejecutarlo: ")
	opciones_menu[user_input]()
	