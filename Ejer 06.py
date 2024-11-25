#Escribir un programa que permita gestionar la base de datos de alumnado de un classroom.
alumnos = {}
opcion = input('Opciones:\n(1) Añadir alumno/a\n(2) Eliminar alumno/a\n(3) Mostrar alumno/a\n(4) Listar todo el alumnado\n(5) Listar alumnado aprobado\n(6) Terminar\nElige una opcion: ')
while opcion != "6":
    if opcion =="1":
        NIF = input("Introduce el NIF del alumno ")
        nombre = input("Como se llama el alumno ")
        apellidos = input("Apellidos de "+ nombre +" ")
        telefono = input("Telefono de "+ nombre +" ")
        correo = input("Dime el correo de "+ nombre +" ")
        aprobado = input(nombre + " ha aprobado? S/N ")
        alumno={"nombre":nombre, "apellidos":apellidos, "telefono":telefono, "correo":correo, "aprobado":aprobado=="S"}
        alumnos[NIF]=alumno
    if opcion =="2":
        NIF=input("Introduce NIF del alumno ")
        if NIF in alumnos:
            print(alumnos[NIF])
            del alumnos[NIF]
        else:
            print("El alumno con NIF", NIF, "no existe")
    if opcion =="3":
        NIF= input("Introduce el NIF del alumno ")
        if NIF in alumnos:
            print("NIF", NIF)
            for clave, valor in alumnos[NIF].items():
                print(clave.title() + ':', valor)
        else:
            print("El alumno con NIF", NIF, "no existe")
    if opcion =="4":
        print(alumnos)
    if opcion =="5":
         print('Alumnos aprobados')
         for clave, valor in alumnos.items():
            if valor['aprobado']:
                print(clave, valor['nombre'])
    opcion = input('Opciones:\n(1) Añadir alumno/a\n(2) Eliminar alumno/a\n(3) Mostrar alumno/a\n(4) Listar todo el alumnado\n(5) Listar alumnado aprobado\n(6) Terminar\nElige una opcion: ')