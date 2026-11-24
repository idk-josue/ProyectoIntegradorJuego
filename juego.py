"""Menú inicial del juego: Tres en raya"""

# DF1: Menú inicial
# RF01: Acceso al modo de juego local

opcion = ""
while opcion != "2":
    print("TRES EN RAYA")
    print("1.-Jugar")
    print("2.-Salir")
    opcion = input("Seleccione una opción (1-2): ").strip()
    if opcion == "1":
        print("Iniciando el juego")
    elif opcion == "2":
        print("Gracias por jugar")
    else:
        print("Opción inválida. Seleccione entre 1 o 2")
