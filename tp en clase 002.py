#1 Pedir al usuario el monto total de la cuenta.
monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

#2 Calcular la propina sugerida al 10% y el total.
propina_10 = monto_cuenta * 0.10
total_10 = monto_cuenta + propina_10

#3 Calcular la propina sugerida al 15% y el total.
propina_15 = monto_cuenta * 0.15
total_15 = monto_cuenta + propina_15

#4 Mostrar todos los resultados en pantalla.
# Usamos f-strings para formatear la salida de manera clara.
print(f"Propina sugerida (10%): {propina_10}")
print(f"Total a pagar (10%): {total_10}")
print(f"Propina sugerida (15%): {propina_15}")
print(f"Total a pagar (15%): {total_15}")