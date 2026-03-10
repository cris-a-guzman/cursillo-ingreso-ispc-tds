# Ejercicio 4
# Un estudiante aprueba una materia si su nota es mayor a 7 y ha entregado el trabajo práctico.

def aprobo():
	print('\n', " En este programa te voy a pedir que ingreses tu nota y en base a tu resultado"
				" Voy a decirte si aprobaste")
	while True:
		user_input = input(" Entregaste el trabajo practico? ").lower()
		
		if user_input == "si":
			print(" Que bueno que lo hayas entregado", '\n')
			
			try:
				user_nota = int(input(" Ahora decime que nota te sacaste: "))

			except ValueError:
				print(" No ingresaste un valor valido")

				if user_nota > 10 or user_nota < 0:
					print(" Sos un mentiroso, esa nota que pusiste no existe, seguro te fue para el orto")
				elif user_nota > 7:
					print(" Felicitaciones, aprobaste la materia por haber entregado el", '\n'
							" Trabajo practico y haber sacado mas de 7")
				elif user_nota >= 4:
					print(" Estuviste bien por entregar el trabajo practico", '\n'
							" Pero no alcanzaste a aprobar, te vas a recuperatorio")
				else:
					print(" Te vas a rendir directo la materia, no te salva ni maradona", '\n')
					
		elif user_input == "no":
			print(" Bueno, cagaste, pero te vas a rendir la materia, lo siento")
			break
		else:
			print(" Ponele voluntad, pone una respuesta valida")
