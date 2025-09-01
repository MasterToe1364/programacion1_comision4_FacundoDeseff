#A mi me toco hacer el ejercicio 3
# --- Ejercicio 3: Evaluación de Crédito Bancario ---
print("\n--- Simulador de Crédito Personal ---")

# 1. Solicitar datos del cliente
nombre_cliente = input("Ingrese su nombre y apellido: ") # [cite: 44]
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: $")) # [cite: 46]
antiguedad_laboral = int(input("Ingrese su antigüedad laboral (en años): ")) # [cite: 47]

# 2. Validar CUIT
while True:
    cuit_str = input("Ingrese su CUIT (formato XX-XXXXXXXX-X): ") # [cite: 45]
    # Validación simple para el ejemplo
    if len(cuit_str) == 13 and cuit_str[2] == '-' and cuit_str[11] == '-':
        break
    else:
        print("Error: Formato de CUIT incorrecto.")

# 3. Validar Historial Crediticio
while True:
    historial = input("Ingrese su historial crediticio (bueno/regular/malo): ").lower() # [cite: 48]
    if historial in ["bueno", "regular", "malo"]:
        break
    else:
        print("Error: Ingrese 'bueno', 'regular' o 'malo'.")

# 4. Lógica de evaluación de crédito
monto_aprobado = ""
if historial == "malo":
    monto_aprobado = "Rechazado (historial crediticio malo)" # [cite: 50]
elif ingresos_mensuales < 200000:
    monto_aprobado = "Rechazado (ingresos insuficientes)" # [cite: 51]
elif antiguedad_laboral < 2:
    monto_aprobado = "Aprobado hasta $500.000" # [cite: 52]
else: # Ingresos >= 200k y Antigüedad >= 2 años
    if historial == "regular":
        monto_aprobado = "Aprobado hasta $1.000.000" # [cite: 54]
    elif historial == "bueno":
        monto_aprobado = "Aprobado hasta $3.000.000" # [cite: 55]

# 5. Mostrar resultado
print("\n--- Evaluación Crediticia ---")
print(f"✔ Cliente: {nombre_cliente}")
print(f"CUIT: {cuit_str}")
print(f"Ingresos: ${ingresos_mensuales:,.2f}")
print(f"Antigüedad: {antiguedad_laboral} años")
print(f"Historial: {historial.capitalize()}")
print(f"Monto aprobado: {monto_aprobado}")


# --- Tarea 1: Clasificación de Impuestos ---
print("\n--- Calculadora de Impuesto Anual ---")

# 1. Pedir datos
nombre = input("Ingrese su nombre completo: ") # [cite: 67]
edad = int(input("Ingrese su edad: ")) # [cite: 68]
ingresos_anuales = float(input("Ingrese sus ingresos anuales: $")) # [cite: 69]

# 2. Calcular el impuesto base
impuesto_base = 0.0
if ingresos_anuales >= 5000000:
    impuesto_base = ingresos_anuales * 0.35 # [cite: 74]
elif ingresos_anuales >= 2000000:
    impuesto_base = ingresos_anuales * 0.20 # [cite: 73]
elif ingresos_anuales >= 500000:
    impuesto_base = ingresos_anuales * 0.10 # [cite: 72]
else:
    impuesto_base = 0 # No paga impuestos [cite: 71]

# 3. Aplicar reducción por edad
impuesto_final = impuesto_base
if edad > 65:
    impuesto_final *= 0.50  # Reducción del 50% [cite: 75]

# 4. Mostrar resultados
print("\n--- Resumen de Impuestos ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Ingresos Anuales: ${ingresos_anuales:,.2f}")
print(f"Impuesto a Pagar: ${impuesto_final:,.2f}")


# --- Tarea 2: Sistema de Calificaciones ---
print("\n--- Sistema de Estado Académico ---")

# 1. Pedir datos del alumno
nombre_alumno = input("Ingrese el nombre del alumno: ") # [cite: 79]
legajo = input("Ingrese el legajo del alumno: ") # [cite: 79]
nota1 = int(input("Ingrese la nota del parcial 1 (0-10): ")) # [cite: 79]
nota2 = int(input("Ingrese la nota del parcial 2 (0-10): ")) # [cite: 79]
nota3 = int(input("Ingrese la nota del parcial 3 (0-10): ")) # [cite: 79]

# 2. Calcular promedio y determinar estado
estado = ""
if nota1 < 4 or nota2 < 4 or nota3 < 4:
    estado = "🔴 Desaprobado (directo por nota inferior a 4)" # [cite: 82]
else:
    promedio = (nota1 + nota2 + nota3) / 3 # [cite: 80]
    if promedio >= 8:
        estado = "🟢 Promocionado" # [cite: 85]
    elif promedio >= 6: # El rango 6 a 7 entra aquí
        estado = "🟡 Aprobado con final" # [cite: 84]
    else: # Menor a 6
        estado = "🔴 Desaprobado (por promedio)" # [cite: 83]

# 3. Mostrar resultado
print("\n--- Estado Académico Final ---")
print(f"Alumno: {nombre_alumno} (Legajo: {legajo})")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Estado: {estado}")


# --- Tarea 3: Simulador de Cajero Automático ---
print("\n--- Cajero Automático BANCO-PY ---")

# 1. Configuración inicial
saldo = 50000  # Saldo inicial definido [cite: 92]
PIN_CORRECTO = "1234"
intentos_pin = 3

# 2. Validación de PIN
autenticado = False
while intentos_pin > 0:
    pin_ingresado = input(f"Ingrese su PIN (le quedan {intentos_pin} intentos): ") # [cite: 91]
    if pin_ingresado == PIN_CORRECTO:
        autenticado = True
        print("PIN correcto. ¡Bienvenido!")
        break
    else:
        intentos_pin -= 1
        print(f"PIN incorrecto.")

if not autenticado:
    print("Ha superado el número de intentos. Tarjeta bloqueada.")
else:
    # 3. Lógica de retiro
    while True:
        monto_str = input("\nIngrese el monto a retirar (múltiplo de 1000) o escriba 'cancelar': ").lower()
        
        if monto_str == 'cancelar': # [cite: 97]
            print("Operación cancelada. No olvide retirar su tarjeta.")
            break
            
        try:
            monto = float(monto_str)
            
            # Validaciones
            if monto > saldo:
                print(f"Error: Saldo insuficiente. Su saldo es de ${saldo:,.2f}") # [cite: 95]
            elif monto % 1000 != 0:
                print("Error: El monto debe ser múltiplo de $1000.") # [cite: 94]
            else:
                # Aplicar comisión si corresponde
                comision = 0
                if monto > 20000:
                    comision = monto * 0.02 # [cite: 96]
                    print(f"Se aplicará una comisión de ${comision:,.2f} (2%) por superar los $20.000.")
                
                saldo -= (monto + comision)
                print("Retire su dinero.")
                print(f"Saldo restante: ${saldo:,.2f}") # [cite: 98]

        except ValueError:
            print("Error: Ingrese un monto numérico válido.")


# --- Tarea 4: Categoría de Conductores ---
print("\n--- Sistema de Clasificación de Conductores ---")

# 1. Pedir datos
nombre_conductor = input("Ingrese su nombre: ") # [cite: 101]
edad_conductor = int(input("Ingrese su edad: ")) # [cite: 101]
experiencia = int(input("Ingrese sus años de experiencia conduciendo: ")) # [cite: 101]

# 2. Lógica de clasificación
categoria = ""
if edad_conductor < 18:
    categoria = "No puede conducir" # [cite: 103]
elif edad_conductor >= 30 and experiencia > 10:
    categoria = "Conductor profesional" # [cite: 106]
elif edad_conductor >= 21 and 1 <= experiencia <= 5:
    categoria = "Conductor intermedio" # [cite: 105]
elif edad_conductor >= 18 and experiencia < 1:
    categoria = "Principiante" # [cite: 104]
else:
    categoria = "Conductor estándar" # [cite: 107]

# 3. Mostrar resultado
print("\n--- Clasificación ---")
print(f"Conductor: {nombre_conductor}")
print(f"Edad: {edad_conductor} años")
print(f"Experiencia: {experiencia} años")
print(f"Categoría: {categoria}")


# --- Tarea 4: Categoría de Conductores ---
print("\n--- Sistema de Clasificación de Conductores ---")

# 1. Pedir datos
nombre_conductor = input("Ingrese su nombre: ") # [cite: 101]
edad_conductor = int(input("Ingrese su edad: ")) # [cite: 101]
experiencia = int(input("Ingrese sus años de experiencia conduciendo: ")) # [cite: 101]

# 2. Lógica de clasificación
categoria = ""
if edad_conductor < 18:
    categoria = "No puede conducir" # [cite: 103]
elif edad_conductor >= 30 and experiencia > 10:
    categoria = "Conductor profesional" # [cite: 106]
elif edad_conductor >= 21 and 1 <= experiencia <= 5:
    categoria = "Conductor intermedio" # [cite: 105]
elif edad_conductor >= 18 and experiencia < 1:
    categoria = "Principiante" # [cite: 104]
else:
    categoria = "Conductor estándar" # [cite: 107]

# 3. Mostrar resultado
print("\n--- Clasificación ---")
print(f"Conductor: {nombre_conductor}")
print(f"Edad: {edad_conductor} años")
print(f"Experiencia: {experiencia} años")
print(f"Categoría: {categoria}")


# --- Tarea 5: Simulador de Carrito de Compras ---
print("\n--- Simulador de Compras Online ---")

# 1. Pedir datos de la compra
nombre_cliente = input("Ingrese su nombre: ") # [cite: 112]
monto_total = float(input("Ingrese el monto total de la compra: $")) # [cite: 114]
cantidad_productos = int(input("Ingrese la cantidad de productos: ")) # [cite: 113]

# 2. Validar medio de pago
medios_validos = ["efectivo", "debito", "credito", "mercado_pago"]
while True:
    medio_pago = input(f"Ingrese el medio de pago ({'/'.join(medios_validos)}): ").lower() # [cite: 115]
    if medio_pago in medios_validos:
        break
    else:
        print("Error: Medio de pago no válido.")

# 3. Aplicar descuentos/recargos iniciales
total_parcial = monto_total
descuento_pago = 0
recargo_pago = 0
detalle = ""

if medio_pago == "efectivo":
    descuento_pago = monto_total * 0.15 # [cite: 117]
    total_parcial -= descuento_pago
    detalle += f"\n- Descuento por pago en efectivo (15%): -${descuento_pago:,.2f}"
elif medio_pago == "debito":
    descuento_pago = monto_total * 0.10 # [cite: 118]
    total_parcial -= descuento_pago
    detalle += f"\n- Descuento por pago con débito (10%): -${descuento_pago:,.2f}"
elif medio_pago == "credito":
    recargo_pago = monto_total * 0.05 # [cite: 119]
    total_parcial += recargo_pago
    detalle += f"\n- Recargo por pago con crédito (5%): +${recargo_pago:,.2f}"
elif medio_pago == "mercado_pago" and monto_total > 10000:
    descuento_pago = monto_total * 0.20 # [cite: 120]
    total_parcial -= descuento_pago
    detalle += f"\n- Descuento Mercado Pago > $10.000 (20%): -${descuento_pago:,.2f}"

# 4. Aplicar descuento extra por cantidad
descuento_extra = 0
if cantidad_productos > 10:
    descuento_extra = total_parcial * 0.05 # [cite: 121]
    detalle += f"\n- Descuento extra por más de 10 productos (5%): -${descuento_extra:,.2f}"

# 5. Calcular total final
total_final = total_parcial - descuento_extra

# 6. Mostrar el ticket final
print("\n--- Ticket de Compra ---")
print(f"Cliente: {nombre_cliente}")
print(f"Monto original: ${monto_total:,.2f}")
print("--- Detalle de la Operación ---")
if detalle:
    print(detalle)
else:
    print("- Sin descuentos o recargos aplicados.")
print("---------------------------------")
print(f"IMPORTE FINAL A PAGAR: ${total_final:,.2f}")