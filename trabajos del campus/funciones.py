# Crear una función llamada imprimir_hola_mundo.
def imprimir_hola_mundo():
    print("Hola Mundo!")

print("Iniciando programa...")
imprimir_hola_mundo()
print("Programa finalizado.")

#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    saludo = f"Hola {nombre}!"
    return saludo

nombre_ingresado = input("Por favor, ingresa tu nombre: ")
mensaje_saludo = saludar_usuario(nombre_ingresado)
print(mensaje_saludo)

# función llamada informacion_personal.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
edad_usuario = input("Ingresa tu edad: ")
residencia_usuario = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#Crear dos funciones:
import math # Necesitamos importar la librería math para usar pi


def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio_circulo = float(input("Ingresa el radio del círculo: "))

area_resultado = calcular_area_circulo(radio_circulo)
perimetro_resultado = calcular_perimetro_circulo(radio_circulo)

print(f"El área del círculo es: {area_resultado}")
print(f"El perímetro del círculo es: {perimetro_resultado}")

# segundos_a_horas

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos_ingresados = int(input("Ingresa una cantidad de segundos: "))

horas_resultado = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {horas_resultado} horas.")

# tabla_multiplicar

def tabla_multiplicar(numero):
    print(f"--- Tabla de multiplicar del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)

# operaciones_basicas

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
        return (suma, resta, multiplicacion, division)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# calcular_imc

def calcular_imc(peso, altura):
    if altura > 0:
        imc = peso / (altura ** 2)
        return imc
    else:
        return "Altura inválida"

peso_kg = float(input("Ingresa tu peso en kg: "))
altura_m = float(input("Ingresa tu altura en metros (ej: 1.75): "))

imc_resultado = calcular_imc(peso_kg, altura_m)

if isinstance(imc_resultado, float):
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")
else:
    print(imc_resultado)


# celsius_a_fahrenheit

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)

print(f"{grados_celsius}°C equivalen a {grados_fahrenheit}°F.")

#calcular_promedio

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num_a = float(input("Ingresa el primer número: "))
num_b = float(input("Ingresa el segundo número: "))
num_c = float(input("Ingresa el tercer número: "))

promedio_resultado = calcular_promedio(num_a, num_b, num_c)

print(f"El promedio de los tres números es: {promedio_resultado}")