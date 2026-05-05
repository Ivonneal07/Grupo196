# =========================
# SISTEMA SOFTWARE 
# =========================

# -------- CLASE CLIENTE --------
class Cliente:
    def __init__(self, nombre, edad):
        # Se guardan los datos del cliente
        self.nombre = nombre
        self.edad = edad

    def mostrar_cliente(self):
        print("Cliente:", self.nombre, "| Edad:", self.edad)


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
        self.cliente.mostrar_cliente()
        self.servicio.mostrar_servicio()
        print("Estado:", self.estado)


# -------- PROGRAMA PRINCIPAL --------

# Listas para guardar datos
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
            continue

        edad = input("Ingrese edad: ")

        if not edad.isdigit():
            print("Error: la edad debe ser número")
            continue

        cliente = Cliente(nombre, edad)
        clientes.append(cliente)
        print("Cliente registrado")

    # CREAR SERVICIO
    elif opcion == "2":
        nombre = input("Nombre del servicio: ")

        if nombre == "":
            print("Error: nombre vacío")
            continue

        costo = input("Costo: ")

        if not costo.replace('.', '', 1).isdigit():
            print("Error: el costo debe ser número")
            continue

        servicio = Servicio(nombre, costo)
        servicios.append(servicio)
        print("Servicio creado")

    # CREAR RESERVA
    elif opcion == "3":
        if len(clientes) == 0 or len(servicios) == 0:
            print("Debe haber clientes y servicios primero")
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
