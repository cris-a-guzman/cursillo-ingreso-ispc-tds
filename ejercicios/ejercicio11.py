# Ejercicio 11
#Pide al usuario que ingrese una categoría entre 
# "niño", "adolescente", "adulto" y "adulto mayor".
# Usa match para mostrar un mensaje personalizado para cada categoría.



def categoria_edad():
    categorias = ["niño", "adolescente", "adulto", "adulto mayor"]
    print(" Ejercicio 11", '\n'
          " Las categorias son: ")
    for i in categorias:
        print(i)
    
    while True:
        user_input = input(" Ingresa a que categoria perteneces: ")

        match user_input:
            case "niño":
                print(" Sos un niño")
            case "adulto":
                print(" Sos un adulto")
            case "adolescente":
                print(" Sos un adolescente")
            case "adulto mayor":
                print(" Sos un adulto mayor")
            case _:
                print(" La opcion ingresada no corresponde a una categoria.")
        user_choice = input(" Te gustaria ingresar otra categoria? SI o NO").lower()
        if user_choice == "no":
            break
