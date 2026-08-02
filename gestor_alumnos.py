

def crear_alumno(alumnos):
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    carrera = input("Ingrese la carrera: ")

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }

    alumnos.append(alumno)
    print("Alumno registrado exitosamente.")

def listar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    print("Lista de alumnos:")
    for i, alumno in enumerate(alumnos, start=1):
        print(f"{i}. Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Carrera: {alumno['carrera']}")
        print("--------------------------------------------------")

def actualizar_alumno(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    listar_alumnos(alumnos)
    indice = int(input("Ingrese el número del alumno que desea actualizar: ")) - 1

    if 0 <= indice < len(alumnos):
        nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
        edad = input("Ingrese la nueva edad (deje en blanco para no cambiar): ")
        carrera = input("Ingrese la nueva carrera (deje en blanco para no cambiar): ")

        if nombre:
            alumnos[indice]['nombre'] = nombre
        if edad:
            alumnos[indice]['edad'] = edad
        if carrera:
            alumnos[indice]['carrera'] = carrera

        print("Alumno actualizado correctamente.")
    else:
        print("Número de alumno inválido.")

def eliminar_alumno(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    listar_alumnos(alumnos)
    indice = int(input("Ingrese el número del alumno que desea eliminar: ")) - 1

    if 0 <= indice < len(alumnos):
        alumnos.pop(indice)
        print("Alumno eliminado correctamente.")
    else:
        print("Número de alumno inválido.")


def guardar_alumnos(alumnos):
    with open("alumnos.txt", "w") as archivo:
        for alumno in alumnos:
            archivo.write(f"{alumno['nombre']},{alumno['edad']},{alumno['carrera']}\n")
    print("Alumnos guardados en 'alumnos.txt'.")


def cargar_alumnos():
    alumnos = []
    try:
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                nombre, edad, carrera = linea.strip().split(",")
                alumno = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera
                }
                alumnos.append(alumno)
        print("Alumnos cargados desde 'alumnos.txt'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'alumnos.txt'. Se creará uno nuevo al guardar.")

    return alumnos

print("Se agrega nuevo texto de prueba para ver si funciona el commit y push")

alumnos = cargar_alumnos()
opcion = 0
while opcion != 6:
    print("\nGestor de Alumnos")
    print("1. REGISTRAR alumno")
    print("2. LISTAR tar alumnos")
    print("3. ACTUALIZAR alumno")
    print("4. ELIMINAR alumno")
    print("5. GUARDAR alumnos")
    print("6. SALIR")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            crear_alumno(alumnos)
        elif opcion == 2:
            listar_alumnos(alumnos)
        elif opcion == 3:
            actualizar_alumno(alumnos)
        elif opcion == 4:
            eliminar_alumno(alumnos)
        elif opcion == 5:
            guardar_alumnos(alumnos)
        elif opcion == 6:
            guardar_alumnos(alumnos)
            print("Saliendo del programa.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    except:
        print("Debe ingresar una opcion numerica valida. Por favor, intente nuevamente.")

