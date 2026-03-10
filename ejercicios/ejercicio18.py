# # Ejercicio 18
# Dada la siguiente lista:
# amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

# a. Devuelve la posición (el index) del amigo "Matías". listo
# b. Devuelve la misma lista pero añadiendo los amigos de la infancia "Juan" y "Andrés" como otra lista. listo
# c. Agrega un nuevo amigo "María" y devuelve el número de amigos. listo
# d. Elimina el último elemento amigo y devuelve el nombre del amigo eliminado. listo
# e. Devuelve el arreglo ordenado alfabéticamente. listo

# ESTO SE PUEDE MEJORAR UNA BANDA

def amigos():
    print(" Este programa es pasivo, se da una lista y se devuelven los siguientes objetivos:")
    print("a. Devuelve la posición (el index) del amigo 'Matías'"
            "b. Devuelve la misma lista pero añadiendo los amigos de la infancia 'Juan' y 'Andrés' como otra lista.\n"
            "c. Agrega un nuevo amigo 'María' y devuelve el número de amigos.\n"
            "d. Elimina el último elemento amigo y devuelve el nombre del amigo eliminado.\n"
            "e. Devuelve el arreglo ordenado alfabéticamente.\n")
    amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']
    amigos = [amigo.lower() for amigo in amigos]
    print(amigos)
    posicion = amigos.index("matías")
    print(posicion)
    amigos_nuevos = ["Juan", "Andrés"]
    todos = amigos + amigos_nuevos
    print(f" Los amigos nuevos son {amigos_nuevos}")
    print(f" Unidos a los amigos viejos quedaria: {todos}")
    print(" Ahora se agrego María")
    todos.append("María")
    print(f" En totan los amigos son: {len(todos)}")
    print(f" Vamos a eliminar el ultimo amigo")
    popeado = todos.pop()
    print(f" El amigo eliminado fue: {popeado}")
    print(f" La lista va a ser ordenada, actualmente es {todos}")
    todos = [todo.lower() for todo in todos]
    todos.sort()
    print(f" Quedo asi: {todos}")


