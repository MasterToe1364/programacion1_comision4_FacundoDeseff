#le pedimos al usuario el largo y ancho de un rectangulo
largo = float(input("Ingrese el valor del largo del rectangulo: "))
ancho = float(input("Ingrese el valor del ancho del rectanuglo: "))
area = largo * ancho
print(f"El area del triangulo es: {area} ")
#--------------------------------------------

numero = float(input("Ingrese un numero: "))

if numero > 0:
    print("El numero ingresado es positivo")
else:
    print("El numero ingresado es negativo")
#-------------------------------------------------

edad_cliente = int(input("Ingrese su edad: "))

estudiante_si_no = (input("Ingrese (s) si es estudiante o de lo contrario ingrese (n): "))

if edad_cliente < 12:
    print("El precio de la entrada del cine para usted es de $5!!")
elif edad_cliente > 12 and estudiante_si_no == "s":
    print("El precio de la entrada del cine para usted es de $8!!")
elif edad_cliente > 65 and estudiante_si_no == "n":
    print("El precio de la entrada del cine para usted es de $7!!")
else:
    print("El precio de la entrada del cine para usted es de $12!!")

#------------------------------------------------------------------
for i in range(5, 51, 5):
    print(i)
#--------------------------------------------------------

contador = 0
while contador <= 100:
    numero = float(input("Ingrese un numero: "))
    contador = contador + numero
print(f"La suma dio: {contador}")
#------------------------------------------------------------

suma_total = 0
while True:
    numero = float(input("Ingrese un numero: "))
    if numero < 0:
        print("Numero negativo ignorado. Ingrese otro numero: ")
        continue
    if numero == 0:
        break
    else:
        print(f"Sumando {numero}....")
        suma_total = suma_total + numero

print(f"La suma total de los numeros ingresados es de: {suma_total}")
#--------------------------------------------------------------------------
lista_ejercicio = ["Ana", 25, "Carlos", 99, "Zanahoria"]
primero_elemento = lista_ejercicio[2]
segundo_elemento = lista_ejercicio[3]
tercer_elemento = lista_ejercicio[4]
ultimo_elemento = lista_ejercicio[-1]
print(f"{primero_elemento}, {segundo_elemento}, {tercer_elemento}")
print(f"{ultimo_elemento}")
#--------------------------------------------------------------------------

compras = ["leche", "pan", "huevos"]
compras.append("arroz")
compras.remove("pan")
print(f"{compras}")
