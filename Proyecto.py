# =========================
# SISTEMA SOFTWARE 
# =========================

from abc import ABC, abstractmethod


# -------- CLASE ABSTRACTA --------
class Persona(ABC):
    def __init__(self, nombre):
        # Constructor de la clase Persona
        self.nombre = nombre

    @abstractmethod
    def mostrar_datos(self):
        pass


# -------- CLASE CLIENTE --------
class Cliente(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre)  # Llamada a la clase padre
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def mostrar_datos(self):
        print("Cliente:", self.get_nombre(), "| Edad:", self.get_edad())


# -------- CLASE SERVICIO --------
class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def mostrar_servicio(self):
        print("Servicio:", self.nombre, "| Costo:", self.costo)


# -------- CLASE RESERVA --------
class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"
        print("Reserva confirmada")

    def mostrar_reserva(self):
        print("\n--- RESERVA ---")
        self.cliente.mostrar_datos()
        self.servicio.mostrar_servicio()
        print("Estado:", self.estado)


# -------- FUNCION LOGS --------
def guardar_error(mensaje):
    with open("errores.txt", "a") as archivo:
        archivo.write(mensaje + "\n")


# -------- PROGRAMA PRINCIPAL --------

clientes = []
servicios = []
reservas = []

while True:
    print("\n1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # REGISTRAR CLIENTE
    if opcion == "1":
        nombre = input("Ingrese nombre: ")

        if nombre == "":
            print("Error: nombre vacío")
            guardar_error("Nombre vacío")
            continue

        try:
            edad = int(input("Ingrese edad: "))
        except:
            print("Error: la edad debe ser un número")
            guardar_error("Error en edad")
            continue

        cliente = Cliente(nombre, edad)
        clientes.append(cliente)
        print("Cliente registrado")

    # CREAR SERVICIO
    elif opcion == "2":
        nombre = input("Nombre del servicio: ")

        if nombre == "":
            print("Error: nombre vacío")
            guardar_error("Nombre servicio vacío")
            continue

        try:
            costo = float(input("Costo: "))
        except:
            print("Error: el costo debe ser un número")
            guardar_error("Error en costo")
            continue

        servicio = Servicio(nombre, costo)
        servicios.append(servicio)
        print("Servicio creado")

    # CREAR RESERVA
    elif opcion == "3":
        if len(clientes) == 0 or len(servicios) == 0:
            print("Debe haber clientes y servicios primero")
            guardar_error("Reserva sin datos")
        else:
            cliente = clientes[0]
            servicio = servicios[0]

            reserva = Reserva(cliente, servicio)
            reserva.confirmar()
            reservas.append(reserva)

    # VER RESERVAS
    elif opcion == "4":
        for r in reservas:
            r.mostrar_reserva()

    # SALIR
    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
