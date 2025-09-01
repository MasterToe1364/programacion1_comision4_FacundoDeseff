# Definimos el alfabeto español de 27 letras.
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# 1. Pedimos el número de corrimiento
corrimiento = int(input("Ingrese la cantidad de lugares a desplazar las letras: "))

# Línea para separar visualmente
print("-" * 30) 

# 2. Usamos el bucle for
for i in range(5):
    
    # Pedimos el mensaje que vamos a encriptar.
    mensaje_original = input(f"Ingrese el mensaje #{i+1}: ")
    
    # Preparamos una variable vacía para guardar el resultado.
    mensaje_cifrado = ""

    # 3. Usamos un segundo FOR (anidado) para recorrer cada letra del mensaje.
    for letra in mensaje_original:
        
        # Convertimos la letra a minúscula para poder buscarla en el alfabeto.
        letra_minuscula = letra.lower()
        
        # Verificamos si el carácter es una letra que podemos cifrar.
        if letra_minuscula in alfabeto:
            
            # Si es una letra, la ciframos:
            indice = alfabeto.find(letra_minuscula)
            nuevo_indice = (indice + corrimiento) % 27
            nueva_letra = alfabeto[nuevo_indice]
            
            # Si la letra original era mayúscula, la nueva también lo será.
            if letra.isupper():
                mensaje_cifrado += nueva_letra.upper()
            else:
                mensaje_cifrado += nueva_letra
        
        else:
            # Si no es una letra (un espacio, número, etc.), la agregamos tal cual.
            mensaje_cifrado += letra
            
    # Imprimimos el resultado de este mensaje antes de pedir el siguiente.
    print(f"Mensaje #{i+1} encriptado: {mensaje_cifrado}\n")


#PIEDRA PAPEL O TIJERA


    import random

# --- Variables iniciales del juego ---
victorias_jugador = 0
victorias_computadora = 0
opciones = ["piedra", "papel", "tijera"]

# --- Bucle principal del juego ---
# Este bucle 'while True' se ejecutará continuamente hasta que decidamos romperlo.
jugar = True
while jugar:
    print("\n" + "="*30)
    print(" PIEDRA, PAPEL O TIJERA")
    print("="*30)
    print(f"MARCADOR: Jugador {victorias_jugador} - {victorias_computadora} Computadora")
    print("-" * 30)
    
    # --- Bucle para la entrada del usuario ---
    # Este bucle se repetirá hasta que el usuario ingrese una opción válida.
    eleccion_usuario = ""
    while eleccion_usuario not in ["piedra", "papel", "tijera", "salir"]:
        eleccion_usuario = input("Escribe 'piedra', 'papel', 'tijera' o 'salir' para terminar: ").lower()
        if eleccion_usuario not in ["piedra", "papel", "tijera", "salir"]:
            print("Opción no válida. Por favor, intenta de nuevo.")
    
    # Si el usuario elige 'salir', cambiamos la variable 'jugar' a False para terminar el bucle principal.
    if eleccion_usuario == "salir":
        jugar = False
    else:
        # La computadora elige su jugada al azar.
        eleccion_computadora = random.choice(opciones)
        
        print("-" * 30)
        print(f"Tú elegiste: {eleccion_usuario.capitalize()}")
        print(f"La computadora eligió: {eleccion_computadora.capitalize()}")
        print("-" * 30)

        # --- Lógica para determinar el ganador de la ronda ---
        if eleccion_usuario == eleccion_computadora:
            print("Resultado: ¡Es un empate!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("Resultado: ¡Ganaste la ronda! 🎉")
            victorias_jugador += 1
        else:
            print("Resultado: La computadora gana la ronda. 💻")
            victorias_computadora += 1
        
        # Pausa para que el jugador pueda leer el resultado antes de la siguiente ronda.
        input("\nPresiona Enter para continuar...")

# --- Fin del juego (cuando el bucle 'while' termina) ---
print("\n" + "="*30)
print("       FIN DEL JUEGO")
print("="*30)
print("Gracias por jugar. Este es el resultado final:")
print(f" Tus victorias: {victorias_jugador}")
print(f" Victorias de la computadora: {victorias_computadora}")
print("="*30)