#---EJERCICIO 1---
# Creamos una lista vacia para guardar los numeros
multiplos_de_cuatro = []
# Recorremos los numeros del 1 al 100
for numero in range(1, 101):
    if numero % 4 == 0:
        multiplos_de_cuatro.append(numero)
# Imprimimos la lista final
print(multiplos_de_cuatro)


#---EJERCICIO 2---
# Creamos una lista con cinco elementos
mis_gustos = ["Pizza", "Programar", "Musica", "Videojuegos", "Cafe"]
# Accedemos al penultimo elemento con el indice -2
penultimo_elemento = mis_gustos[-2]
# Imprimimos el resultado
print(penultimo_elemento)



#---EJERCICIO 3---
# Creamos una lista vacia
palabras = []
# Agregamos tres palabras
palabras.append("Hola")
palabras.append("mundo")
palabras.append("Python")
# Imprimimos la lista completa
print(palabras)




#---EJERCICIO 4---
# Lista original
animales = ["perro", "gato", "conejo", "pez"]
# Reemplazamos el segundo elemento (indice 1)
animales[1] = "loro"
# Reemplazamos el ultimo elemento (indice -1)
animales[-1] = "oso"
# Imprimimos la lista modificada
print(animales)



#---EJERCICIO 5---
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)


#---EJERCICIO 6---
# Creamos la lista usando range con un paso de 5
numeros = list(range(10, 31, 5))
# Usamos slicing para obtener los dos primeros elementos
dos_primeros = numeros[0:2]
# Imprimimos el resultado
print(dos_primeros)



#---EJERCICIO 7---
# Lista original
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazamos los elementos en los indices 1 y 2
autos[1:3] = ["coupe", "camioneta"]
# Imprimimos la lista modificada
print(autos)


#---EJERCICIO 8---
# Creamos la lista vacia
dobles = []
# Agregamos el doble de cada numero
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
# Imprimimos la lista resultante
print(dobles)



#---EJERCICIO 9---
# Lista anidada original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
#Imprimir la lista resultante por pantalla
print(compras)


#---EJERCICIO 10---
# Creamos la lista anidada directamente
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
# Imprimimos la lista completa para verificar
print(lista_anidada)
print("Elemento en [2][1]:", lista_anidada[2][1])