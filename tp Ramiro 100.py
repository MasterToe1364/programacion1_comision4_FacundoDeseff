# 1)

# Se le pide al usuario los datos
parcial_1 = float(input("Ingrese la calificacion del primer parcial: "))
parcial_2 = float(input("Ingrese la calificacion del segundo parcial: "))
parcial_3 = float(input("Ingrese la calificacion del tercer parcial: "))
examen_final = float(input("Ingrese la calificacion del examen final: "))
trabajo_final = float(input("Ingrese la calificacion del trabajo final: "))

# Se calcula el promedio y porcentaje
promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3
porcentaje_parciales = promedio_parciales * 0.55
porcentaje_examen = examen_final * 0.30
porcentaje_trabajo = trabajo_final * 0.15

# Resultado final de la calificacion
calificacion_final = porcentaje_parciales + porcentaje_examen + porcentaje_trabajo

# Muestra del resultado final
print(f"Tu calificacion final en Algoritmos es: {calificacion_final:.2f}")

#2)

# Conversion de divisas
tasa_col = 4032.59  # Dolar a pesos colombianos
tasa_ars = 1305.20   # Dolar a pesos argentinos
tasa_eur = 0.86     # Dolar a Euro

# Se solicitan la cantidad de dolares
dolares = float(input("Ingrese el monto en dolares a convertir: "))

# El tipo de conversion
pesos_colombianos = dolares * tasa_col
pesos_argentinos = dolares * tasa_ars
euros = dolares * tasa_eur

# Resultado de la conversion
print(f"El equivalente de ${dolares:.2f} USD es:")
print(f"- {pesos_colombianos:.2f} Pesos Colombianos")
print(f"- {pesos_argentinos:.2f} Pesos Argentinos")
print(f"- {euros:.2f} Euros")

#3)

consumo_por_100km = 8.0
velocidad_promedio_kmh = 90.0

# Se le pide los datos al usuario
distancia_km = float(input("Ingrese la distancia del viaje en km: "))
precio_litro_gasolina = float(input("Ingrese el precio de la nafta por litro: "))

# Calculos del viaje en auto
litros_necesarios = (distancia_km / 100) * consumo_por_100km
costo_viaje = litros_necesarios * precio_litro_gasolina
tiempo_viaje_horas = distancia_km / velocidad_promedio_kmh

# Muestra de resultados
print(" Detalles del Viaje ")
print(f"Litros necesarios: {litros_necesarios:.2f} L")
print(f"Costo total del viaje: ${costo_viaje:.2f}")
print(f"Tiempo estimado de viaje: {tiempo_viaje_horas:.2f} horas")


#4)

plazo_meses = 12
interes_mensual_fijo = 0.02  # Esto representa el 2%

# Se le pide al usuario el monto de la solicitud del prestamo
monto_solicitado = float(input("Ingresa el monto del prestamo a solicitar: "))

# Se hacen los calculos correspondientes
interes_total = monto_solicitado * interes_mensual_fijo * plazo_meses
monto_total_a_devolver = monto_solicitado + interes_total
valor_cuota_mensual = monto_total_a_devolver / plazo_meses

# Resultados
print(" Resumen del Prestamo ")
print(f"Monto total a devolver: ${monto_total_a_devolver:.2f}")
print(f"Valor de cada cuota mensual ({plazo_meses} meses): ${valor_cuota_mensual:.2f}")
