print("\n--- Ejercicio 1 ---")
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


print("\n--- Ejercicio 2 ---")
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


print("\n--- Ejercicio 3 ---")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


print("\n--- Ejercicio 4 ---")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


print("\n--- Ejercicio 5 ---")
password = input("Ingrese una contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


print("\n--- Ejercicio 6 ---")
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No cumple con ninguno de los criterios anteriores")


print("\n--- Ejercicio 7 ---")
texto = input("Ingrese una palabra o frase: ")
if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)


print("\n--- Ejercicio 8 ---")
nombre = input("Ingrese su nombre: ")
opcion = (input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


print("\n--- Ejercicio 9 ---")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


print("\n--- Ejercicio 10 ---")
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("La estación es:", estacion)
