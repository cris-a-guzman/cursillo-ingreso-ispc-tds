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
opciones_menu = {
	'1' : promedios,
	'2' : numero_pi,
	'3' : saber_numero,
	'4' : aprobo,
	'5' : radio_circulo,
	'6' : calcular_grados,
	'7' : nota_usuario,
	'8' : numero_impar_par
	
}

validacion = True
while validacion:
	user_input = input(" Ingrese el numero del problema para ejecutarlo: ")
	opciones_menu[user_input]()
	