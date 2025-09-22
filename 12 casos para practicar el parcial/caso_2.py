especialidades = []
cupos = []

while True:
    print("\n--- Menu de Gestion de Turnos---")
    print("1. Ingresar listas de especialidades")
    print("2. Ingresar lista de cupos disponibles")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupos")
    print("6. Agregar especialidad")
    print("7. Actualizar cupo (reservar/cancelar)")
    print("8. Ver agenda (completa)")
    print("9. Salir")

    opcion = input("Seleccione una opcion: ")
    if not opcion.isdigit():
        print("ERROR: Debe ingresar un numero valido.")
        continue
    match opcion:
        case "1":
            print("---Ingresar Especialidades---")
            especialidades_ingresadas = input("Escriba las especialidades separas por coma: ")

            if not especialidades_ingresadas:
                print("No se ingreso ninguna especialidad.")
            else:
                lista_temporal = especialidades_ingresadas.split(",")
                for nombre_especialidad in lista_temporal:
                    nombre_limpio = nombre_especialidad.strip()

                    if not nombre_limpio:
                        continue
                    if nombre_limpio in especialidades:
                        print(f"Advertencia: La especialidad {nombre_limpio} ya existe. No se agrego")
                    else:
                        especialidades.append(nombre_limpio)
                        cupos.append(0)
                        print(f"Especialidad {nombre_limpio} fue agregada con exito.")
        case "2":
            print("---Asignar Cupos a Especialidades---")
            if not especialidades:
                print("ERROR: Primero debe ingresar especialidades en la opcion 1.")
            else:
                for i in range(len(especialidades)):
                    cupos_str = input(f"Ingrese los cupos para {especialidades[i]}: ")

                    if cupos_str.isdigit():
                        cupos_int = int(cupos_str)
                        cupos[i] = cupos_int
                        print(f"Se asignaron {cupos_int} cupos a {especialidades[i]}.")
                    else:
                        print(f"Entrada no valida para {especialidades[i]}. Se mantendra el valor anterior ({cupos[i]}).")
                print("\n Proceso de asignacion de cupos finalizado!")
        case "3":
            print("\n--- Agenda de Cupos por Especialidad ---")
            if not especialidades:
                print("No hay especialidades registradas para mostrar.")
            else:
                print("Especialidad / Cupos disponibles:")
                for i in range(len(especialidades)):
                    print(f"- {especialidades[i]}: {cupos[i]} cupos")
        case "4":
            print("\n--- Consultar Cupos por Especialidad ---")
            if not especialidades:
                print("No hay especialidades registradas para consultar.")
            else:
                nombre_consulta = input("Ingrese el nombre de la especialidad a consultar: ").strip()
                

                if nombre_consulta in especialidades:
                    indice = especialidades.index(nombre_consulta)
                    print(f"La especialidad {nombre_consulta} tiene {cupos[indice]} cupos disponibles.")
                else:
                    print(f"ERROR: La especialidad {nombre_consulta} no fue encontrada.")

        case "5":
            print("\n--- Especialidades con 0 Cupos ---")
            if not especialidades:
                print("No hay especialidades registradas.")
            else:
                se_encontro_alguna = False
                
                for i in range(len(especialidades)):
                    if cupos[i] == 0:
                        print(f" - {especialidades[i]}")
                        se_encontro_alguna = True

                if not se_encontro_alguna:
                    print("Todas las especialidades registradas tiene cupos disponibles")
        case "6":
            print("\n--- Agregar Nueva Especialidad ---")

            nueva_especialidad = input("Ingrese el nombre de la nueva especialidad: ").strip()
            cupos_str = input(f"Ingrese los cupos iniciales para {nueva_especialidad}: ")

            if cupos_str.isdigit() and int(cupos_str) >= 0:
                if nueva_especialidad and nueva_especialidad not in especialidades:
                    especialidades.append(nueva_especialidad)
                    cupos.append(int(cupos_str))
                    print(f"Especialidad {nueva_especialidad} agregada con exito!!")
                else:
                    print("ERROR: El nombre de la especialidad no puede estar vacio o ya existe en la lista.")
            else:
                print("ERROR: La cantidad de cupos debe ser un numero positivo o cero.")

        case "7":
            print("\n--- Actualizar Cupos(Reservar / Cancelar) ---")
            if not especialidades:
                print("No hay especialidades registradas.")
            else:
                nombre_modificar = input("Ingrese el nombre de la especialidad a actualizar: ").strip()
                if nombre_modificar in especialidades:
                    indice = especialidades.index(nombre_modificar)
                    accion = input(f" Desea [R]Reservar o [C]Cancelar un cupo para {nombre_modificar}?: ").strip().lower()
                    if accion == "r":
                        if cupos[indice] > 0:
                            cupos[indice] -= 1
                            print(f"Reserva exitosa!! Quedan {cupos[indice]} como en {nombre_modificar}")
                        else:
                            print(f"ERROR: No quedan cupos disponibles para {nombre_modificar}")
                    elif accion == "c":
                        cupos[indice] += 1
                        print(f" Cancelacion exitosa!! Ahora hay {cupos[indice]} cupos en {nombre_modificar}")
                    else:
                        print("Error: Acción no válida. Por favor, elija 'R' o 'C'.")
                else:
                    print(f"ERROR: La especialidad {nombre_modificar} no fue encontrada.")
        case "8":
            print("\n--- Agenda de Cupos por Especialidad (Completa) ---")
            if not especialidades:
                print("No hay especialidades registradas.")
            else:
                print("Especialidad / Cupos disponibles:")
                for i in range(len(especialidades)):
                    print(f"- {especialidades[i]}: {cupos[i]} cupos")
        case "9":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opcion no valida, por favor, intente de nuevo.")

