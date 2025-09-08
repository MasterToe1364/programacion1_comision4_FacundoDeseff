# Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100.
print("--- Ejercicio 1: Números del 0 al 100 ---")

for numero in range(101):
    print(numero)


# Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de dígitos que contiene.
print("\n--- Ejercicio 2: Cantidad de dígitos ---")

numero_ingresado = int(input("Ingrese un número entero: "))

if numero_ingresado == 0:
    cantidad = 1
else:
# Usar el valor absoluto para contar dígitos de números negativos
    cantidad = 0
    numero = abs(numero_ingresado)
    while numero > 0:
        numero = numero // 10
    cantidad += 1

print(f"El número {numero_ingresado} tiene {cantidad} dígito(s).")




# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
print("\n--- Ejercicio 3: Suma entre dos valores ---")

valor1 = int(input("Ingrese el primer número entero: "))
valor2 = int(input("Ingrese el segundo número entero: "))

# Asegurarse de que el bucle vaya del menor al mayor
inicio = min(valor1, valor2)
fin = max(valor1, valor2)

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los enteros entre {valor1} y {valor2} es: {suma}")






# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse cuando el usuario ingrese un 0.
print("\n--- Ejercicio 4: Sumar hasta ingresar 0 ---")

total_acumulado = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break  # Rompe el bucle si el número es 0
    total_acumulado += num

print(f"La suma total acumulada es: {total_acumulado}")






# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, mostrar cuántos intentos fueron necesarios.
import random
print("\n--- Ejercicio 5: Adivina el número ---")

numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intentos += 1
    suposicion = int(input("Adivina el número secreto (entre 0 y 9): "))
    if suposicion == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Incorrecto. ¡Sigue intentando!")






# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("\n--- Ejercicio 6: Pares en orden decreciente ---")

for i in range(100, -1, -2):
    print(i)




# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("\n--- Ejercicio 7: Suma hasta un número ---")

limite = int(input("Ingrese un número entero positivo: "))
suma_total = 0

if limite >= 0:
    # range(limite + 1) genera números de 0 a limite
    for i in range(limite + 1):
        suma_total += i
    print(f"La suma de los números de 0 a {limite} es: {suma_total}")
else:
    print("El número debe ser positivo.")





# Escribe un programa que permita al usuario ingresar 100 números enteros y luego indique cuántos son pares, impares, negativos y positivos.
print("\n--- Ejercicio 8: Clasificador de números ---")

CANTIDAD_NUMEROS = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD_NUMEROS):
    n = int(input(f"Ingrese el número {i+1}/{CANTIDAD_NUMEROS}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("\n--- Resultados del conteo ---")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")




# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
print("\n--- Ejercicio 9: Media de valores ---")

# Para probar, puedes cambiar este valor a uno más pequeño (ej. 10)
TOTAL_A_INGRESAR = 100
suma_para_media = 0

for i in range(TOTAL_A_INGRESAR):
    numero_media = int(input(f"Ingrese el número {i+1}/{TOTAL_A_INGRESAR}: "))
    suma_para_media += numero_media

media = suma_para_media / TOTAL_A_INGRESAR
print(f"La media de los {TOTAL_A_INGRESAR} números es: {media}")



# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
print("\n--- Ejercicio 10: Invertir un número ---")

numero_a_invertir = int(input("Ingrese un número para invertir: "))
invertido = 0
numero_temporal = abs(numero_a_invertir) # Usar valor absoluto para el cálculo

while numero_temporal > 0:
    ultimo_digito = numero_temporal % 10
    invertido = (invertido * 10) + ultimo_digito
    numero_temporal = numero_temporal // 10

# Si el original era negativo, el resultado también debe serlo
if numero_a_invertir < 0:
    invertido = -invertido

print(f"El número {numero_a_invertir} invertido es: {invertido}")

