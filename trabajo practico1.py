print ("Hola Mundo!")

nombre = input ("Por favor, ingresar tu nombre: ")
print (f"Hola {nombre}!")

nombre = input ("ingresar tu nombre: ")
apellido = input ("ingresar tu apellido: ")
edad = input("ingresar tu edad: ")
residencia = input("ingresa tu lugar de residencia: ")
print(f"Soy {nombre}{apellido}, tengo {edad} años y vivo en {residencia}.")

import match
radio_str = input("Ingresar el radio del circulo: ")
radio = float(radio_str)
area = match.pi * (radio ** 2)
perimetro = 2 * match.pi * radio
print (f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

segundos_str = input("Ingresar una cantidad de segundos: ")
segundos = int(segundos_str)
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

numero = int(input("Ingresar un numero para ver su tabla de multiplicar: "))
print(f"--- Tabla del {numero}---")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

num1 = int(input("Ingresar el priumer numero entero (destino de 0): "))
num2 = int(input("Ingresar el segundo numero entero (destino de 0):"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicacion: {num1} * {num2} = {multiplicacion}")
print(f"Division: {num1} / {num2} = {division}")

peso = float(input("Ingresar tu peso en kg (ej:75.5):"))
altura = float(input("Ingresa tu altura en metros (ej: 1.78): "))
imc = peso / (altura ** 2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc}")

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F.")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio}")