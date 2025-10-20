def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    # Caso Base: El factorial de 0 es 1.
    if n == 0:
        return 1
    # Caso Recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def calcular_factoriales_hasta(numero):
    """
    Usa la función factorial para mostrar los factoriales
    desde 1 hasta el número dado.
    """
    print(f"\n--- Factoriales desde 1 hasta {numero} ---")
    for i in range(1, numero + 1):
        print(f"Factorial de {i} es {factorial(i)}")


def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n de forma recursiva."""
    # Caso Base 1: F(0) = 0
    if n == 0:
        return 0
    # Caso Base 2: F(1) = 1
    elif n == 1:
        return 1
    # Caso Recursivo: F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(posicion):
    """
    Muestra la serie completa de Fibonacci hasta la posición dada,
    usando la función recursiva.
    """
    print(f"\n--- Serie de Fibonacci hasta la posición {posicion} ---")
    for i in range(posicion + 1):
        print(fibonacci(i), end=" ")
    print() # Para un salto de línea al final


def potencia(base, exponente):
    """Calcula la potencia de forma recursiva."""
    # Caso Base: n^0 = 1
    if exponente == 0:
        return 1
    # Caso Recursivo: n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)
    

def decimal_a_binario(n):
    """Convierte un número decimal a una cadena binaria de forma recursiva."""
    # Caso Base: Si n es 0 o 1, su binario es él mismo.
    if n < 2:
        return str(n)
    # Caso Recursivo: 
    # Llama recursivamente con el cociente (n // 2)
    # y concatena el resto (n % 2) al final.
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    


def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo de forma recursiva."""
    palabra = palabra.lower() # Pasamos a minúscula para ser consistentes
    
    # Caso Base 1: 0 o 1 letra
    if len(palabra) <= 1:
        return True
    # Caso Base 2: Primera y última letra no coinciden
    elif palabra[0] != palabra[-1]:
        return False
    # Caso Recursivo: Llamar a la función con la sub-palabra interior
    else:
        return es_palindromo(palabra[1:-1]) # Slice de la 2da a la penúltima
    

def suma_digitos(n):
    """Suma los dígitos de un número entero de forma recursiva."""
    # Caso Base: Si es un número de un solo dígito (0-9), la suma es él mismo.
    if n < 10:
        return n
    # Caso Recursivo: Último dígito (n % 10) + suma_digitos(resto del número)
    else:
        return (n % 10) + suma_digitos(n // 10)
    

def contar_bloques(n):
    """Calcula el total de bloques en una pirámide de n niveles."""
    # Caso Base: Una pirámide de 1 nivel tiene 1 bloque.
    if n == 1:
        return 1
    # Caso Recursivo: n + (el total de una pirámide de n-1)
    else:
        return n + contar_bloques(n - 1)
    

def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número."""
    # Caso Base: El número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    
    # Caso Recursivo:
    contador_actual = 0
    if (numero % 10) == digito: # ¿Es el último dígito el que buscamos?
        contador_actual = 1
    
    # Devolver 1 (o 0) + el resultado de buscar en el resto del número
    return contador_actual + contar_digito(numero // 10, digito)

