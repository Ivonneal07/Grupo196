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



# -------- EXCEPCIONES -------

class SoftwareFJError(Exception): pass

class ClienteMenorEdadError(SoftwareFJError): pass

class ParametrosInvalidosError(SoftwareFJError): pass





# -------- CLASE RESERVA --------

class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente

        self.servicio = servicio

        self.estado = "Pendiente"



    def confirmar(self):

        """Procesamiento con manejo de excepciones"""

        try:

            # Validaciones

            if self.cliente.get_edad() < 18:

                raise ClienteMenorEdadError(f"{self.cliente.get_nombre()} es menor de edad.")

            if self.duracion <= 0:

                raise ParametrosInvalidosError("La duración debe ser mayor a 0 días.")

           

            self.estado = "Confirmada"

            print(f"Reserva confirmada para {self.cliente.get_nombre()}")

        except (ClienteMenorEdadError, ParametrosInvalidosError) as e:

            self.estado = "cancelada"

            guardar_error(str(e))

            print(f"Error controlado: {e}")



    def cancelar(self):

        """Implementación de la cancelación"""

        if self.estado == "Confirmada" or self.estado == "Pendiente":

            self.estado = "Cancelada"

            print(f"La reserva de {self.cliente.get_nombre()} ha sido cancelada satisfactoriamente.")

        else:

            print(f"No se puede cancelar una reserva con estado: {self.estado}")



    def mostrar_reserva(self):

        print("\n--- DETALLE DE RESERVA ---")

        self.cliente.mostrar_datos()

        self.servicio.mostrar_servicio()

        print(f"Duración: {self.duracion} días | Estado: {self.estado}")



   



    def mostrar_reserva(self):

        print("\n--- RESERVA ---")

        self.cliente.mostrar_datos()

        self.servicio.mostrar_servicio()

        print("Estado:", self.estado)





# -------- FUNCION LOGS --------

def guardar_error(mensaje):

    with open("errores.txt", "a") as archivo:

        archivo.write(mensaje + "\n")





#---------VALIDACIONES-------



class Reserva:

    def __init__(self, cliente, servicio, duracion=1):

        self.cliente = cliente

        self.servicio = servicio

        self.duracion = duracion

        self.estado = "Pendiente"



    def confirmar(self):

        try:

            # Validaciones estrictas según requerimiento

            if self.cliente.get_edad() < 18:

                raise ClienteMenorEdadError(f"{self.cliente.get_nombre()} es menor de edad.")

            if self.duracion <= 0:

                raise ParametrosInvalidosError("La duración debe ser mayor a 0 días.")

           

            self.estado = "Confirmada"

            print(f"Reserva confirmada para {self.cliente.get_nombre()}")

        except (ClienteMenorEdadError, ParametrosInvalidosError) as e:

            self.estado = "cancelada"

            guardar_error(str(e))

            print(f"Error controlado: {e}")



    def mostrar_reserva(self):

        print("\n--- DETALLE DE RESERVA ---")

        self.cliente.mostrar_datos()

        self.servicio.mostrar_servicio()

        print(f"Duración: {self.duracion} días | Estado: {self.estado}")

       

#-------- 10 PRUEBAS AUTOMATICAS"



def ejecutar_10_pruebas():

    print("\n" + "="*45)

    print("SIMULACIÓN DE 10 OPERACIONES AUTOMÁTICAS")

    print("="*45)

    c_ok = Cliente("Andrés García", 25)

    c_no = Cliente("Juanito", 15)

    s_test = Servicio("Asesoría Especializada", 200.0)

   

    casos = [

        (c_ok, s_test, 3), (c_no, s_test, 1), (c_ok, s_test, 0),

        (c_ok, s_test, 5), (c_no, s_test, 2), (c_ok, s_test, -1),

        (c_ok, s_test, 1), (c_ok, s_test, 10), (c_no, s_test, 4),

        (c_ok, s_test, 2)

    ]

    for i, (cli, ser, dur) in enumerate(operaciones := casos, 1):

        print(f"Prueba #{i}:", end=" ")

        r = Reserva(cli, ser, dur)

        r.confirmar()





# -------- PROGRAMA PRINCIPAL --------



clientes = []

servicios = []

reservas = []



while True:

    print("\n1. Registrar cliente")

    print("2. Crear servicio")

    print("3. Crear reserva")

    print("4. Ver reservas")

    print("5. Ejecutar 10 pruebas automaticas")

    print("6. Salir")



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

            cliente = clientes[-1]

            servicio = servicios[-1]

         

            try:

                # 1. Pedimos el dato

                valor = input("Ingrese la duración de la reserva (días): ")

                valor_duracion = int(valor)

               

                # 2. Creamos la reserva con los 3 datos

                reserva = Reserva(cliente, servicio, valor_duracion)

               

                # 3. Validamos

                reserva.confirmar()

               

                # 4. Guardamos

                reservas.append(reserva)

               

            except ValueError:

                print("Error: La duración debe ser un número entero.")

                guardar_error("Entrada de duración no numérica")

            except Exception as e:

                print(f"Error inesperado: {e}")

           

    # VER RESERVAS

    elif opcion == "4":

        for r in reservas:

            r.mostrar_reserva()

       

    # EJECUTAR PRUEBAS

    elif opcion == "5":

        ejecutar_10_pruebas()

    # SALIR

    elif opcion == "6":

        print("Saliendo...")

        break

    else:

        print("Opción inválida")
