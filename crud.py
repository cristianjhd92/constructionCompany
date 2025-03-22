#Empresa del sector de la construcción urbana necesita administrar sus procesos de vinculación laboral
#Fortaleza: Certificado de maestro de construcción
#Fortaleza: Grado de Ingeniero de obra pública
#Fortaleza: Manejo Ágil de proyectos
#Listado y asignación de obras por cuadrillas

# Se importa de decoradores.py la función validate_input para validar la entrada de datos
from decorators import validate_input

# Se crea la clase Person con los atributos document, name, lastname y age
class Person:
    # Se crea el constructor de la clase con los atributos document, name, lastname y age
    def __init__(self, document, name, lastname, age):
        # Con el __ se encapsulan los atributos de la clase
        self.__document = document
        self.__name = name
        self.__lastname = lastname
        self.__age = age
    
     # Se crean los métodos get para obtener los valores de los atributos de la clase
    def get_document(self):
        return self.__document
    
    def get_full_name(self):
        return f"{self.__name} {self.__lastname}"
    
    def get_age(self):
        return self.__age
    
    # Clase base DatabaseManager para manejo de datos
class DatabaseManager:
    # Se crea la lista de empleados, se usa __ para encapsular la lista y se inicializa vacía
    __employees = []  # Encapsulación de la lista de empleados
    
    # Se crea el método add_employee para agregar un empleado a la lista
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de empleados
    def add_employee(cls, employee): # Se recibe el objeto student como parámetro y cls hace referencia a la clase
        cls.__employees.append(employee) # Se agrega el objeto student a la lista de estudiantes
    
    # Se crea el método get_students para obtener la lista de estudiantes
    @classmethod
    def get_employees(cls): # cls hace referencia a la clase para acceder a la lista de empleados
        return cls.__employees # Se retorna la lista de empleados
    
    # Se crea el método remove_employee para eliminar un empleado de la lista
    @classmethod 
    def remove_employee(cls, employee): # Se recibe el objeto employee como parámetro y cls hace referencia a la clase
        cls.__employees.remove(employee)

# Clase Employee heredando de Person y DatabaseManager
class Employee(Person, DatabaseManager):
    # Se crea el constructor de la clase con los atributos document, name, lastname, age, work_station y strengths
    def __init__(self, document, name, lastname, age, work_station, strengths):
        # Se llama al constructor de la clase padre Person con los atributos document, name, lastname y age
        super().__init__(document, name, lastname, age)
        # Se encapsula el atributo work_station de la clase
        self.__work_station = work_station
        self.__strengths = strengths
    
    # Se crea el método get_work_station para obtener el valor del atributo work_station
    def get_work_station(self):
        # Se retorna el valor del atributo work_station
        return self.__work_station
    
    # Se crea el método get_strengths para obtener el valor del atributo strengths
    def get_strengths(self):
        # Se retorna el valor del atributo strengths
        return self.__strengths

    # Se crean los métodos de clase para realizar las operaciones CRUD

    # Se crea el método create_employee para crear un empleado
    @classmethod
    def create_employee(cls):
        # Se solicitan los datos del empleado
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento: ")
        name = input("Ingrese los nombres del empleado: ")
        lastname = input("Ingrese los apellido del empleado: ")
        age = input("Ingrese la edad: ")
        work_station = input("Ingrese el cargo (Ingeniero, Maestro de Obra, Obrero): ")
        strengths = input("""De las siguientes fortalezas cual tiene el empleado:
1: Certificado de maestro de construcción
2: Grado de Ingeniero de obra pública
3: Manejo Ágil de proyectos
Ingrese la fortaleza correspondiente por favor: """)
        print("-------------------------------------------------------")
        
        # Se crea un objeto employee con los datos ingresados
        employee = cls(document, name, lastname, age, work_station, strengths)
        # Se agrega el objeto employee a la lista de empleados
        cls.add_employee(employee)
        # Se muestra un mensaje de confirmación
        print("-------------------------------------------------------")
        print("Empleado agregado exitosamente")
        print("-------------------------------------------------------")
    
    # Se crea el método show_employees para mostrar todos los empleados
    @classmethod
    def show_employees(cls):
        # Se obtiene la lista de empleados con el método get_employees
        employees = cls.get_employees()
        # Se verifica si la lista de empleados está vacía
        if not employees:
            # Se muestra un mensaje indicando que no hay empleados registrados
            print("-------------------------------------------------------")
            print("No hay empleados registrados.")
            print("-------------------------------------------------------")
            # Se retorna
            return
        # Se recorre la lista de empleados
        for employee in employees:
            # Se muestra los datos de cada empleado
            print("-------------------------------------------------------")
            print("Número de documento:", employee.get_document())
            print("Nombre Completo:", employee.get_full_name())
            print("Edad:", employee.get_age())
            print("Cargo:", employee.get_work_station())
            print("Fortaleza:", employee.get_strengths())
            print("-------------------------------------------------------")
    
    # Se crea el método find_employee para buscar un empleado por número de documento
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de empleados
    @validate_input # Se aplica el decorador validate_input para validar la entrada de datos
    def find_employee(cls):
        # Se solicita el número de documento del empleado a buscar
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del empleado a buscar: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de empleados llamando al método get_employees
        for employee in cls.get_employees():
            # Se verifica si el número de documento del empleado es igual al ingresado
            if employee.get_document() == document:
                # Se muestran los datos del empleado
                print("-------------------------------------------------------")
                print("Número de documento:", employee.get_document())
                print("Nombre Completo:", employee.get_full_name())
                print("Edad:", employee.get_age())
                print("Cargo:", employee.get_work_station())
                print("Fortaleza:", employee.get_strengths())
                print("-------------------------------------------------------")
                # Se retorna True si se encuentra el empleado
                return True
        # Se retorna False si no se encuentra el empleado
        return False
    
    # Se crea el método update_employee para actualizar los datos de un empleado
    @classmethod
    @validate_input
    def update_employee(cls):
        # Se solicita el número de documento del empleado a actualizar
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del empleado del cual desea actualizar sus datos: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de empleados llamando al método get_employees
        for employee in cls.get_employees():
            # Se verifica si el número de documento del empleado es igual al ingresado
            if employee.get_document() == document:
                # Se solicita el dato a actualizar
                print("-------------------------------------------------------")
                query = input("¿Qué dato desea actualizar? (nombres, apellidos, edad, cargo): ")
                print("-------------------------------------------------------")
                # Se verifica el dato a actualizar
                if query == "nombres":
                    # Se solicitan los nuevos nombres del empleado
                    employee._Person__name = input("Ingrese los nuevos nombres: ")
                    print("-------------------------------------------------------")

                elif query == "apellidos":
                    # Se solicitan los nuevos apellidos del empleado
                    employee._Person__lastname = input("Ingrese los nuevos apellidos: ")
                    print("-------------------------------------------------------")
                
                elif query == "edad":
                    # Se solicita la nueva edad del empleado
                    employee._Person__age = input("Ingrese la nueva edad: ")
                    print("-------------------------------------------------------")
                
                elif query == "cargo":
                    # Se solicita la nueva categoría del empleado
                    employee.__work_station = input("Ingrese el nuevo cargo (Ingeniero, Maestro de obra, Obrero): ")
                    print("-------------------------------------------------------")
                
                else:
                    # Se muestra un mensaje indicando que el dato ingresado es incorrecto
                    print("Dato no válido")
                    print("-------------------------------------------------------")
                    # Se retorna False si el dato ingresado es incorrecto
                    return False
                # Se muestra un mensaje de confirmación
                print("-------------------------------------------------------")
                print("Empleado actualizado exitosamente")
                print("-------------------------------------------------------")
                # Se retorna True si se actualiza el empleado
                return True
        # Se retorna False si no se encuentra el empleado
        return False
    
    # Se crea el método delete_employee para eliminar un empleado
    @classmethod
    @validate_input
    def delete_employee(cls):
        # Se solicita el número de documento del empleado a eliminar
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del empleado a eliminar: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de empleados llamando al método get_employees
        for employee in cls.get_employees():
            # Se verifica si el número de documento del empleado es igual al ingresado
            if employee.get_document() == document:
                # Se elimina el empleado de la lista de empleados llamando al método remove_employee de la clase DatabaseManager
                cls.remove_employee(employee)
                # Se muestra un mensaje de confirmación
                print("-------------------------------------------------------")
                print("Empleado eliminado exitosamente")
                print("-------------------------------------------------------")
                # Se retorna True si se elimina el empleado
                return True
        # Se retorna False si no se encuentra el empleado
        return False

