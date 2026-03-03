# Ejercicio 3
# Queremos saber si un número es menor que 0 o mayor que 10.

def saber_numero():
	print('\n', " Ejercicio 3"
		  '\n', " En este ejercicio te voy a pedir que ingreses un numero"
		  '\n', " Y en base a lo que pongas te digo si es menor a 0 o mayor a 10")
	
	while True:
		try:
			user_input = input(" Ingrese un numero: ")
			num = int(user_input)
			
			if num < 0:
				print('\n', " Tu numero es menor a 0")
			elif num > 10:
				print('\n', " Tu numero es mayor a 10")
			else:
				print('\n', " Tu numero esta entre 0 y 10")
		except ValueError:
			print('\n', " Eso no fue un numero, ingresa un numero valido la proxima vez")
							
		print('\n', " Desea seguir probando?", '\n'
							" Ponga SI para seguir.", '\n'
							" Ponga NO para volver atras", '\n')
		
		user_input = input(" ").lower()
		
		if user_input == "no":
			break
		
							
