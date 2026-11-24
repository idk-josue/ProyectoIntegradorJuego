"""Validación y fin de partida de tres en raya"""

# DF2: VALIDACION DE LA JUGADA
# RF04: Validar la jugada
# RF06: Evitar casillas ocupadas

print("Validación de jugada")

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c5 = 1
valida = 0
while valida == 0:
    jugada = input("Ingrese una casilla del 1 al 9: ").strip()

    if not jugada.isdigit():
        print("Entrada invalida. Ingrese un numero.")
    elif int(jugada) < 1 or int(jugada) > 9:
        print("Casilla invalida. Elija del 1 al 9.")
    else:
        jugada = int(jugada)

        if jugada == 1:
            ocupada = c1 != 0
        elif jugada == 2:
            ocupada = c2 != 0
        elif jugada == 3:
            ocupada = c3 != 0
        elif jugada == 4:
            ocupada = c4 != 0
        elif jugada == 5:
            ocupada = c5 != 0
        elif jugada == 6:
            ocupada = c6 != 0
        elif jugada == 7:
            ocupada = c7 != 0
        elif jugada == 8:
            ocupada = c8 != 0
        else:
            ocupada = c9 != 0

        if ocupada:
            print("Casilla ocupada")
        else:
            valida = 1
print("Jugada valida. Casilla aceptada.")

# DF3: FIN DE LA PARTIDA
# RF07: Identificar al ganador
# RF08: Detectar empate

print("Fin de la partida")
print("Seleccione el caso que desea probar:")
print("1. Gana el jugador 1")
print("2. Gana el jugador 2")
print("3. Empate")
print("4. La partida continua")
opcion = input("Ingrese una opcion: ").strip()
while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
    print("Opcion invalida")
    opcion = input("Ingrese una opcion: ").strip()
opcion = int(opcion)
if opcion == 1:
    c1, c2, c3 = 1, 1, 1
    c4, c5, c6 = 2, 2, 0
    c7, c8, c9 = 0, 0, 0
    contador = 5

elif opcion == 2:
    c1, c2, c3 = 2, 2, 2
    c4, c5, c6 = 1, 1, 0
    c7, c8, c9 = 0, 0, 1
    contador = 6

elif opcion == 3:
    c1, c2, c3 = 1, 1, 2
    c4, c5, c6 = 2, 2, 1
    c7, c8, c9 = 1, 2, 1
    contador = 9

else:
    c1, c2, c3 = 1, 2, 0
    c4, c5, c6 = 0, 1, 0
    c7, c8, c9 = 0, 2, 0
    contador = 4
ganador = 0
if (
    (c1 == 1 and c2 == 1 and c3 == 1)
    or (c4 == 1 and c5 == 1 and c6 == 1)
    or (c7 == 1 and c8 == 1 and c9 == 1)
    or (c1 == 1 and c4 == 1 and c7 == 1)
    or (c2 == 1 and c5 == 1 and c8 == 1)
    or (c3 == 1 and c6 == 1 and c9 == 1)
    or (c1 == 1 and c5 == 1 and c9 == 1)
    or (c3 == 1 and c5 == 1 and c7 == 1)
):
    ganador = 1
elif (
    (c1 == 2 and c2 == 2 and c3 == 2)
    or (c4 == 2 and c5 == 2 and c6 == 2)
    or (c7 == 2 and c8 == 2 and c9 == 2)
    or (c1 == 2 and c4 == 2 and c7 == 2)
    or (c2 == 2 and c5 == 2 and c8 == 2)
    or (c3 == 2 and c6 == 2 and c9 == 2)
    or (c1 == 2 and c5 == 2 and c9 == 2)
    or (c3 == 2 and c5 == 2 and c7 == 2)
):
    ganador = 2
if ganador == 1:
    print("Gana el jugador 1")
elif ganador == 2:
    print("Gana el jugador 2")
elif contador == 9:
    print("Empate")
else:
    print("La partida continua")
