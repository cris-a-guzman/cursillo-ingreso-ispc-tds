# Ejercicio 12
# Escribe un programa que solicite tres lados de un triángulo e indique si es 
# equilátero, isósceles o escaleno.

# equilatero = 3 lados iguales
# isoseles = 2 lados iguales
# escaleno = 3 lados desiguales
# Hay que agregar un error para los numeros negativos
def pedir_lado():
    print(" En este programa vas a ingresar 3 lados de un triangulo", '\n'
          " En base a lo ingresado te digo que tipo de triangulo es")
    
    while True:
        try:
            x = int(input(" Ingrese el lado del triangulo: "))
            if x <= 0:
                raise ValueError(" No se admiten numeros negativos")
            else:
                return x
        except ValueError:
            print(" Ingresa un numero valido")

def triangulo():
    a = pedir_lado()
    b = pedir_lado()
    c = pedir_lado()

    if (a+b) > c or (a+c) > b or (b+c)> a:    
        if a == b and b == c:
            print(" Es un equilatero")
        elif a == b or b == c or a == c:
            print(" Es un isoseles")
        else:
            print(" Es un escaleno")
    else:
        print(" Lo que pusiste no constituye un triangulo ya que la regla 'a+b > c' no se cumple")