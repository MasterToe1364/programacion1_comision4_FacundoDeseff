titulos = []
ejemplares = []
while True:
    print("\n--- Menu Principal ---")
    print("1. Ingresar titulos a la lista.")
    print("2. Ingresar los ejemplares para cada titulo.")
    print("3. Mostrar catalogo.")
    print("4. Consultar disponibilidad de un titulo.")
    print("5. Listar los titulos que se encuentren agotados")
    print("6. Agregar un titulo y su stock a la lista.")
    print("7. Actualizar los ejemplares (Prestamo / Devolucion)")
    print("8. Salir del Menu")

    opcion = input("Ingrese una opcion del Menu para realizar una accion: ").strip()
    if not opcion.isdigit():
        print("Error: Por favor ingrese un numero del Menu")
        continue


    match opcion:
        case "1":
            print("Ingresar titulos a la lista")
            ingresar_titulos = input("Ingrese los titulos que desee agregar a la lista separados con una coma: ").strip()
            lista_provisoria = ingresar_titulos.split(",")
            for lista_nueva in lista_provisoria:
                lista_limpia = lista_nueva.strip()
                titulos.append(lista_limpia)
                ejemplares.append(0)
                print("Los titulos fueron agregados a la lista con exito!!")
        case "2":
            print("\n---Ingresar los ejemplares a cada titulo de la lista---")
            if not titulos:
                print("No se han registrado titulos todavia.")
            else:
                for i in range(len(titulos)):
                    ingresar_ejemplares = input(f"Ingrese la cantidad de ejemplares para {titulos[i]}: ")
                    if ingresar_ejemplares.isdigit():
                        ejemplar_limpio = int(ingresar_ejemplares)
                        ejemplares[i] = ejemplar_limpio
                    else:
                        print(f"Error: Ejemplares invalidos para {titulos[i]}, el numero de ejemplares no cambiará: ({ejemplar_limpio[i]})")
                else:
                    print("Los ejemplares fueron agregados con éxito!!")
        case "3":
            print("\n--- Mostrar lista de Titulos y Ejemplares ---")
            if not titulos:
                print("No se han registrado Titulos todavia.")
            else:
                print("Titulos / Ejemplares")
                for i in range(len(titulos)):
                    print(f"- {titulos[i]}: {ejemplares[i]} ejemplares")
        case "4":
            print("\n--- Consultar la disponibilidad de un Título ---")
            if not titulos:
                print("No se han registrado titulos todavia.")
            else:
                consultar_titulo = input("Ingrese el nombre del titulo que desea consultar: ").strip()
                if consultar_titulo in titulos:
                    indice = titulos.index(consultar_titulo)
                    print(f"El titulo ({consultar_titulo}) tiene {ejemplares[indice]} ejemplares")
                else:
                    print(f"El titulo {consultar_titulo} no se encuentra registrado en la lista")

        case "5":
            print("\n--- Listar los titulos que se encuentran agotados ---")
            if not titulos:
                print("No se encontraron titulos registrados todavia.")
            else:
                titulos_sin_ejemplares: False
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print(f"- {titulos[i]}: {ejemplares[i]} ejemplares")
                        titulos_sin_ejemplares = True
                        if not titulos_sin_ejemplares:
                            print("No se encontraron titulos sin ejemplares")
        case "6":
            print("\n--- Agregar titulos y sus ejemplares a la lista ---")
            nuevo_titulo = input("Ingrese el nombre del nuevo titulo que desee agregar a la lista: ").strip().lower()
            nuevo_ejemplar = input("Ingrese la cantidad de ejemplares que tendra el nuevo titulo: ")
            if nuevo_titulo and nuevo_titulo not in titulos:
                if nuevo_ejemplar.isdigit() and int(nuevo_ejemplar) >= 0:
                    titulos.append(nuevo_titulo)
                    ejemplares.append(int(nuevo_ejemplar))
                    print(f"El titulo ({nuevo_titulo}) fue agregado exitosamente")
                else:
                    print("Error: Numero invalido, por favor tiene que ingresar un numero positivo o 0.")
            else:
                print("Error: No puede ingresar un espacio vacio, o el nuevo titulo ya se encuentra registrado en la lista!!")
        case "7":
            print("\n--- Actualizar ejemplares (Prestamo / Devolucion) ---")
            if not titulos:
                print("No hay titulos registrados todavia.")
            else:
                titulos_modificar = input("Ingrese el titulo para retirar o devolver un ejemplar: ").strip().lower()
                if titulos_modificar in titulos:
                    indice = titulos.index(titulos_modificar)
                    accion = input("Ingrese P[Prestamo] o D[Devolucion] para realizar una accion: ").strip().lower()
                    if accion == "p":
                        if ejemplares[indice] > 0:
                            ejemplares[indice] -= 1
                            print(f"Prestamo exitoso, queda {ejemplares[indice]} ejemplares disponibles para {titulos_modificar}")
                        else:
                            print(f"No quedan ejemplares disponibles para {titulos_modificar}")
                    elif accion == "d":
                        ejemplares[indice] += 1
                        print(f"La devolucion se realizó con éxito. Quedan {ejemplares[indice]} ejemplares disponibles para {titulos_modificar}")
                    else:
                        print("Error: Por favor ingrese una opcion valida.")
                else:
                    print(f"No se encontro {titulos_modificar} en la lista")
        case "8":
            print("Saliendo del Menu...")
            break
        case _:
            print("Error: Por favor ingrese un numero del Menu.")