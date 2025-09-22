clases = []
cupos = []

while True:
    print("\n--- Inscripcion a Clases de Deportes ---")
    print("1. Ingresar la lista de clases.")
    print("2. Ingresar cupos por clase.")
    print("3. Mostrar clases por cupos.")
    print("4. Consultar cupos de una clase.")
    print("5. Mostrar las listas de clases sin cupos.")
    print("6. Agregar una nueva clase.")
    print("7. Actualizar cupos (Inscribir / Bajar)")
    print("8. Salir del menu.")

    opcion = input("Seleccione una opcion del menu por favor: ")

    match opcion:
        case "1":
            print("\n ---Ingresar la lista de clases---")
            lista_ingresada = input("Ingrese la lista de clases separando cada clase de otra con una (,): ").strip()
            lista_temporal = lista_ingresada.split(",")
            for nueva_lista in lista_temporal:
                lista_limpia = nueva_lista.strip()
                clases.append(lista_limpia)
                cupos.append(0)
            print("La lista fue agregada exitosamente!!")

        case "2":
            print("\n ---Ingresar los cupos por cada clase registrada---")
            if not clases:
                print("No hay clases registradas.")
            else:
                for i in range(len(clases)):
                    cupos_ingresados = input(f"Ingrese los cupos para la clase {clases[i]}: ")
                    if cupos_ingresados.isdigit():
                        numero_cupos = int(cupos_ingresados)
                        cupos[i] = numero_cupos
                    else:
                        print(f"Entrada no valida para {clases[i]}. Se mantendra el valor anterior ({cupos[i]}).")
                print("\nTodos los cupos fueron actualizados correctamente!!")
                

        case "3":
            print("\n ---Mostrar las clases con sus cupos---")
            if not clases:
                print("No hay clases registradas.")
            else:
                print("Clases / Cupos")
                for i in range(len(clases)):
                    print(f"- {clases[i]}: {cupos[i]} cupos")
        case "4":
            print("\n ---Ingrese la clase a la cual quiere consultar los cupos---")
            if not clases:
                print("No hay clases registradas.")
            else:
                clase_consulta = input("Ingrese la clasa a la cual quiere consultar sus cupos: ").strip()
                if clase_consulta in clases:
                    indice = clases.index(clase_consulta)
                    print(f"La clase {clase_consulta} tiene {cupos[indice]} cupos")
                else:
                    print("ERROR: La clase ingresada no fue encontrada.")

        case "5":
            print("\n ---Mostrar las listas de clases sin cupos---")
            if not clases:
                print("No hay clases registradas.")
            else:
                clases_sin_cupos = False
                for i in range(len(clases)):
                    if cupos[i] == 0:
                        print(f" - {clases[i]}")
                        clases_sin_cupos = True
                if not clases_sin_cupos:
                    print("Todas las clases tienen cupos disponibles.")

        case "6":
            print("\n ---Ingrese la nueva clase que quiere agregar a la lista---")
            nueva_clase = input("Ingrese el nombre de la nueva clase: ").strip()
            numero_cupos = input(f"Ingrese la cantidad de cupos para la clase {nueva_clase}: ")
            if nueva_clase and nueva_clase not in clases:
                if numero_cupos.isdigit() and int(numero_cupos) >= 0:
                    clases.append(nueva_clase)
                    cupos.append(int(numero_cupos))
                    print(f"La nueva clase {nueva_clase} fue agregada a la lista con exito!!")
                else:
                    print("ERROR: El número de cupos debe ser un número válido (positivo o cero).")
            else:
                print("ERROR: El nombre de la clase no puede estar vacío o ya existe.")

        case "7":
            print("\n ---Actualizar cupos (Inscribir / Bajar)")
            if not clases:
                print("No hay clases registradas.")
            else:
                nombre_modificar = input("Ingrese el nombre de la clase que desea actualizar: ").strip()
                if nombre_modificar in clases:
                    indice = clases.index(nombre_modificar)
                    accion = input(f"Use I[Inscribir] o B[Bajar]  un cupo para {nombre_modificar}: ").strip().lower()
                    if accion == "i":
                        if cupos[indice] > 0:
                            cupos[indice] -= 1
                            print(f"Inscripcion exitosa! Quedan {cupos[indice]} cupos disponibles para {nombre_modificar}")
                        else:
                            print(f"ERROR: No quedan cupos disponibles para la clase de {nombre_modificar}")
                    elif accion == "b":
                        cupos[indice] += 1
                        print(f"El cupo se dio de baja con exito!! Quedan {cupos[indice]} para la clase de {nombre_modificar}!")
                    else:
                        print("ERROR: Opcion no valida, por favor use (I / B)")
                else:
                    print(f"La especialidad {nombre_modificar} no fue encontrada.")
        case "8":
            print("\n ---Saliendo del Menu...---")
            break
        case _:
            print("Opcion no valida, por favor, intente de nuevo.")