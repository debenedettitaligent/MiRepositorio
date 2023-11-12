import sys

if len(sys.argv) == 3:

    cadena = sys.argv[1]

    repeticiones = int(sys.argv[2])

    for repeticiones in range(0, repeticiones):
        print(cadena)

else:
    print("Introduce bien la cantidad de argumentos")
    