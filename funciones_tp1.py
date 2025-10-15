def suma_digitos(numero):

    suma = 0
    for digito in str(numero):
        suma += 1
    return suma

def solicitar_numero():
    while True:
        try:
            numero_ingresado = int(input("Ingrese un numero y si desea terminar ingrese el cero: "))
            return numero_ingresado
        except ValueError:
            print("Error. Por favor ingrese solo numeros enteros.")

def programa_principal():
    suma_total = 0
    print("---Calculadora de suma de digitos---")

    while True:
        numero_actual = solicitar_numero()
        if numero_actual == 0:
            print("\nCalculando los resultados finales!")
            break
        suma_total += numero_actual
        resultado_digitos = suma_digitos(numero_actual)

    print(f"> la suma de los digitos de {numero_actual} es de: {resultado_digitos}\n")

    print("------------------------------------------------")
    print(f"La suma total de todos los numeros ingresados es de: {suma_total}")
    digitos_del_total = suma_digitos(suma_total)
    print(f"La suma de los digitos del total es: {(suma_total)} es: {digitos_del_total}")
programa_principal()



