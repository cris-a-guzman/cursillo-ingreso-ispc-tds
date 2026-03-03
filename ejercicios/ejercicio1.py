# Ejercicio 1
# Escribe un algoritmo para calcular el promedio de tres números ingresados por el usuario.

def promedios():
	prom = 0
	iteraciones = 0
	while True:
		try:
			if iteraciones < 3:
				user_input = int(input("    Ingresa un numero: "))
				iteraciones += 1
				prom += user_input
			else:
				break
		except ValueError:
			print(" Eso no fue un numero, ingresa un numero")
		
	print(prom / 3)		
	print(f" El promedio de los numeros ingresados es: {prom / 3}")


	
	
