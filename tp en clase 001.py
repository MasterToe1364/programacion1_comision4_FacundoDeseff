# 1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 20
print(f"1. El valor de numero1 es: {numero1}")

# 2. Crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = 5.5
print(f"2. El valor de numero2 es: {numero2}")

# 3. Crea una variable "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2
# Crea tres variables más para resta, multiplicación y división. Imprime estas variables.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"3. Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# 4. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Facundo"
print(f"4. Mi nombre es: {nombre}")

# 5. Crea una variable llamada "precio" y asígnale un valor decimal.
precio = 150.75
print(f"5. El precio es: ${precio}")

# 6. Crea una variable "descuento" y asígnale un valor decimal que represente el descuento.
descuento = 0.25  # Representa el 25%
print(f"6. El descuento a aplicar es del: {descuento * 100}%")

# 7. Calcula el precio final aplicando el descuento y almacénalo en "precio_final".
precio_final = precio - (precio * descuento)
print(f"7. El precio final con descuento es: ${precio_final}")

# 8. Crea una variable llamada "cadena" y asígnale una frase.
cadena = "Python es un lenguaje de programación increíble."
print(f"8. La cadena de texto es: '{cadena}'")

# 9. Crea una nueva variable "longitud" y almacena la longitud de "cadena".
longitud = len(cadena)
print(f"9. La longitud de la cadena es: {longitud} caracteres.")

# 10. Crea otra vez la variable llamada "precio" y dale un valor decimal, y conviértelo en número entero.
precio_decimal_nuevo = 89.99
precio_entero = int(precio_decimal_nuevo)
print(f"10. El precio decimal {precio_decimal_nuevo} se convierte a entero: {precio_entero}")

# 11. Concatena dos variables "nombre" y "apellido" en "nombre_completo".
# (Reutilizamos la variable 'nombre' del punto 4)
apellido = "Deseff"
nombre_completo = nombre + " " + apellido
print(f"11. El nombre completo es: {nombre_completo}")

# 12. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 30
print(f"12. Edad inicial: {edad}")
edad += 5
print(f"    Edad incrementada en 5: {edad}")
edad -= 10
print(f"    Edad disminuida en 10: {edad}")

# 13. Crea una variable "altura" que contenga decimales. Multiplícala por 4 y luego divídela en 3.
altura = 1.64
print(f"13. Altura inicial: {altura}m")
altura *= 4
print(f"     Altura multiplicada por 4: {altura}")
altura /= 3
# 14. Usamos round() para mostrar un resultado más limpio con solo 2 decimales
print(f"14.     Altura dividida en 3: {round(altura, 2)}")

# 15. Crea una variable con tu nombre en mayúsculas y luego transfórmala a minúsculas.
nombre_mayusculas = "ROBERTO GOMEZ"
print(f"15. Nombre en mayúsculas: {nombre_mayusculas}")
nombre_minusculas = nombre_mayusculas.lower()
print(f"     Nombre transformado a minúsculas: {nombre_minusculas}")

# 16. Transforma la variable con el nombre en minúsculas para que solo la primera letra sea mayúscula.
nombre_capitalizado = nombre_minusculas.capitalize()
print(f"16. Nombre con la primera letra en mayúscula: {nombre_capitalizado}")