#1 Solicitar y procesar la entrada del usuario

# Se le pide al usuario que ingrese la fecha en el formato especificado.
entrada_usuario = input("Ingrese la fecha actual en formato 'dia, DD/MM': ")

# Se procesa la entrada para separar sus componentes.
partes = entrada_usuario.split(',')
dia_semana = partes[0].strip().lower()
fecha_partes = partes[1].strip().split('/')

# Se convierten los numeros del dia y mes a tipo entero para poder compararlos.
dia_numero = int(fecha_partes[0])
mes_numero = int(fecha_partes[1])

#2 Validar la fecha (dia y mes)

if dia_numero > 31 or mes_numero > 12:
    print("Error: la fecha es invalida (dia supera 31 o mes supera 12).")
else:
    # --- 3. Logica principal segun el dia de la semana ---

    # Dias con examenes: Lunes, Martes y Miercoles
    if dia_semana in ["lunes", "martes", "miercoles"]:
        print(f"Dia de clase con posible examen: {dia_semana.capitalize()}")
        hubo_examenes = input("Se tomaron examenes hoy? (si/no): ").lower()

        if hubo_examenes == "si":
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            no_aprobados = int(input("Ingrese la cantidad de alumnos que no aprobaron: "))
            
            total_alumnos = aprobados + no_aprobados
            
            # Se evita la division por cero si no hubo alumnos
            if total_alumnos > 0:
                porcentaje_aprobados = (aprobados / total_alumnos) * 100
                # Se muestra el resultado formateado a dos decimales.
                print(f"El porcentaje de aprobados es: {porcentaje_aprobados:.2f}%")
            else:
                print("No hubo alumnos en el examen.")

    # Dia de practica hablada: Jueves
    elif dia_semana == "jueves":
        print("Dia de practica hablada.")
        asistencia = float(input("Ingrese el porcentaje de asistencia (%): "))

        if asistencia > 50:
            print("Asistio la mayoria.")
        else:
            print("No asistio la mayoria.")

    # Dia de ingles para viajeros: Viernes
    elif dia_semana == "viernes":
        print("Dia de Ingles para Viajeros.")

        # Se verifica si es un dia de inicio de ciclo.
        if dia_numero == 1 or dia_numero == 7:
            print("Comienzo de nuevo ciclo!")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
            
            ingreso_total = cantidad_alumnos * arancel_por_alumno
            print(f"El ingreso total del nuevo ciclo es: ${ingreso_total:.2f}")

    # Si el dia ingresado no es valido
    else:
        print("El dia ingresado no corresponde a un dia de clase valido.")