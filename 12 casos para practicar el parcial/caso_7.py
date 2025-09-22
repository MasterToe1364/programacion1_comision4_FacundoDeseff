alumnos = []
asistencias = []

while True:
    print("\n --- Sistema de gestion de alumnos ---")
    print("1. Ingresar nombres de estudiantes.")
    print("2. Mostrar listado con asistencia.")
    print("3. Consultar asistencia por estudiante.")
    print("4. Listar estudiante con asistencia 0.")
    print("5. Agregar un nuevo estudiante. ")
    print("6. Marcar asistencia a un estudiante.")
    print("7. Salir.")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre_ingresados = input("Ingresar el nombre de los estudiantes separados por comas: ")
        nuevos_alumnos = [nombre.strip() for nombre in nombre_ingresados.split(",")]

        for alumno in nuevos_alumnos:
            if alumno:
                if alumno not in alumnos:
                    alumnos.append(alumno)
                    asistencias.append(0)
                else:
                    print(f"El estudiante {alumno} ya se encuentra en la lista.")
        print("Estudiantes registrados!!")
    elif opcion == "2":
        print("\n ---Listado de estudiantes y asistencias---")
        if not alumnos:
            print("No hay estudiantes registrado.")
        else:
            for i in range(len(alumnos)):
                print(f"{alumnos[i]}: {asistencias[i]} asistencias")
    elif opcion == "3":
        nombre_consulta = input("Ingrse el nombre del alumno a consultar:").strip()
        if nombre_consulta in alumnos:
            indice = alumnos.index(nombre_consulta)
            print(f"El estudiante {nombre_consulta} tiene {asistencias[indice]} asistencias!!")
        else:
            print(f"El estudiante {nombre_consulta} no fue encontrado.")
    elif opcion == "4":
        print("\n ---Estudiantes con 0 asistencias ---")
        alumnos_con_cero = [alumnos[i] for i in range(len(alumnos)) if asistencias[i] == 0]
        if not alumnos_con_cero:
            print("No hay estudiantes con 0 asistencias.")
        else:
            for alumno in alumnos_con_cero:
                print(alumno)
    elif opcion == "5":
        nuevo_alumno = input("Ingrese el nombre del nuevo estudiante:").strip()
        if nuevo_alumno:
            if nuevo_alumno not in alumnos:
                alumnos.append(nuevo_alumno)
                asistencias.append(0)
                print(f"Estudiante {nuevo_alumno} agregado exitosamente!!")
            else:
                print("El nombre del usuario no puede estar vacio.")
    elif opcion == "6":
        nombre_asistencia = input("Ingrese el nombre del estudiante a marcar asistencia: ").strip()
        if nombre_asistencia in alumnos:
            indice = alumnos.index(nombre_asistencia)
            asistencias[indice] += 1
            print(f"Asistencia marcada para {nombre_asistencia}.")
        else:
            print(f"El estudiante {nombre_asistencia} no fue encontrado.")
    elif opcion == "7":
        print("Saliendo del programa.....")
        break

