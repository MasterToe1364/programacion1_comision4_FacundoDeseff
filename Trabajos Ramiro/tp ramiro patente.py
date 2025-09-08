# Definimos el alfabeto que vamos a usar para las patentes
LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TOTAL_LETRAS = len(LETRAS)
COMBINACIONES_NUMERICAS = 1000
# Calculo el número máximo de patentes posibles.
MAX_PATENTES = (TOTAL_LETRAS ** 3) * COMBINACIONES_NUMERICAS
print("--- Calculadora de Patentes ---")
print(f"El sistema soporta hasta {MAX_PATENTES:,} patentes (desde AAA 000 hasta ZZZ 999).")
while True:
    # Pedimos al usuario que ingrese un número.
    entrada_usuario = input("\nIngresa un número de patente (o 'salir' para terminar): ")
    # Si el usuario escribe 'salir', terminamos el programa.
    if entrada_usuario.lower() == 'salir':
        print("¡Adiós!")
        break
    try:
        # Intentamos convertir la entrada a un número entero.
        numero_patente = int(entrada_usuario)
        # Verificamos si el número está dentro del rango válido.
        if not (1 <= numero_patente <= MAX_PATENTES):
            print(f"Error: Por favor, ingresa un número entre 1 y {MAX_PATENTES}.")
            continue
        valor = numero_patente - 1

        # 1. Calculamos la parte numérica de la patente.
        parte_numerica = valor % COMBINACIONES_NUMERICAS

        # 2. Calculamos la parte de las letras.

        indice_letras = valor // COMBINACIONES_NUMERICAS

        # Ahora convertimos ese "índice de letras" en las tres letras correspondientes.
        letra_1 = LETRAS[(indice_letras // (TOTAL_LETRAS**2)) % TOTAL_LETRAS]
        letra_2 = LETRAS[(indice_letras // TOTAL_LETRAS) % TOTAL_LETRAS]
        letra_3 = LETRAS[indice_letras % TOTAL_LETRAS]
        
        parte_letras = f"{letra_1}{letra_2}{letra_3}"

        print(f"La patente número {numero_patente} es: {parte_letras} {parte_numerica:03d}")

    except ValueError:
        # Si el usuario no ingresa un número válido, mostramos un error.
        print("Error: Entrada no válida. Por favor, ingresa solo un número.")