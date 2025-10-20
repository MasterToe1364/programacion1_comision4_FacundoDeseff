#1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario original: {precios_frutas}")

# Añadir las siguientes frutas 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300  
print(f"Diccionario con frutas añadidas: {precios_frutas}")

# 2) Actualizar los precios 
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(f"Diccionario con precios actualizados: {precios_frutas}")

# 3) Crear una lista que contenga únicamente las frutas 
lista_frutas = list(precios_frutas.keys())
print(f"Lista de frutas (claves): {lista_frutas}")


# Agenda Telefónica
contactos = {}
print("--- Carga de 5 contactos ---")
for i in range(5):
    nombre = input(f"Ingrese nombre del contacto {i+1}: ")
    numero = input(f"Ingrese número de teléfono de {nombre}: ")
    contactos[nombre] = numero

print("\n--- Agenda Completa ---")
print(contactos)

# Pedí un nombre y mostrale el número asociado 
print("\n--- Consulta de Contacto ---")
nombre_consulta = input("Ingrese un nombre para buscar su número: ")

# Usamos .get() para evitar un error si el nombre no existe.
numero_encontrado = contactos.get(nombre_consulta, "Contacto no encontrado")

print(f"Resultado: {numero_encontrado}")


#Palabras únicas y recuento
frase = input("Introduce una frase: ")

# Normalizamos (todo a minúsculas) y dividimos la frase en una lista de palabras
palabras = frase.lower().split()

# 1. Las palabras únicas
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# 2. Un diccionario con la cantidad de veces que aparece cada palabra 
recuento = {}
for palabra in palabras:
    # Si la palabra ya está en el diccionario, le suma 1
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Recuento de palabras: {recuento}")


#Promedio de notas
alumnos = {}
# Permití ingresar los nombres de 3 alumnos 
for _ in range(3):
    nombre = input(f"Ingrese nombre del alumno {_ + 1}: ")
    
    # Pedimos las 3 notas como string separado por comas
    notas_str = input(f"Ingrese las 3 notas de {nombre} (separadas por coma, ej: 10, 9, 8): ")

    notas_tupla = tuple(int(n.strip()) for n in notas_str.split(',')) # 
    
    alumnos[nombre] = notas_tupla

print("\n--- Promedios ---")
# Mostrá el promedio de cada alumno [cite: 42]
for nombre, notas in alumnos.items():
    # sum(notas) suma todos los elementos de la tupla
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} (Notas: {notas}) es: {promedio:.2f}")


#Operaciones con sets
# Creamos los sets de ejemplo
parcial_1 = {"Juan", "Ana", "Luis", "Sofía", "Pedro", "Maria"}
parcial_2 = {"Ana", "Sofía", "Miguel", "Carla", "Luis", "Jorge"}

print(f"Aprobaron Parcial 1: {parcial_1}")
print(f"Aprobaron Parcial 2: {parcial_2}")

# 1. Mostrá los que aprobaron ambos parciales (Intersección) 
ambos_parciales = parcial_1.intersection(parcial_2)
print(f"\nAprobaron ambos parciales: {ambos_parciales}")

# 2. Mostrá los que aprobaron solo uno de los dos (Diferencia Simétrica) 
solo_un_parcial = parcial_1.symmetric_difference(parcial_2)
print(f"Aprobaron solo uno de los dos: {solo_un_parcial}")

# 3. Mostrá la lista total (sin repetir) (Unión) 
todos_los_que_aprobaron = parcial_1.union(parcial_2)
print(f"Lista total de aprobados (al menos un parcial): {todos_los_que_aprobaron}")


#Control de stock
stock = {"leche": 10, "pan": 5, "huevos": 20} # 

while True:
    print("\n--- CONTROL DE STOCK ---")
    print("1. Consultar stock")
    print("2. Agregar stock / Cargar nuevo producto")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        # Consultar el stock de un producto ingresado [cite: 55]
        producto = input("Ingrese nombre del producto a consultar: ")
        print(f"Stock de {producto}: {stock.get(producto, 'Producto no encontrado')}")
    
    elif opcion == "2":
        producto = input("Ingrese nombre del producto: ")
        cantidad = int(input(f"Ingrese cantidad a agregar a {producto}: "))
        
        stock[producto] = stock.get(producto, 0) + cantidad
        print(f"Stock de {producto} actualizado a: {stock[producto]}")
        
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida.")

print(f"\nStock final: {stock}")


#Agenda (Día, Hora)
# Las claves son tuplas de (día, hora) 
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Turno con el dentista",
    ("viernes", "21:00"): "Cena"
}

print("--- Consultar Agenda ---")
# Permití consultar qué actividad hay en cierto día y hora 
dia = input("Ingrese el día (ej: lunes): ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")

# Creamos la tupla para buscar
clave_agenda = (dia, hora)

# Consultamos usando la tupla como clave
evento = agenda.get(clave_agenda, "No hay eventos programados en esa fecha y hora.")
print(f"Evento: {evento}")


#Invertir diccionario
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Francia": "París",
    "Japón": "Tokio",
    "Perú": "Lima"
}

capitales_paises = {}

# Recorremos el diccionario original
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
    
print(f"Original: {paises_capitales}")
print(f"Invertido: {capitales_paises}")