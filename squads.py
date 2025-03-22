#Se crea la clase Cuadrilla
class Squad:
    # Constructor de la clase Squad para representar una cuadrilla
    def __init__(self, squad_id, squad_name):
        self.squad_id = squad_id
        self.squad_name = squad_name
        self.members = []  # Lista para almacenar los miembros de la cuadrilla
        self.assigned_work = None  # Obra asignada (puede ser None si no se asignó ninguna)
    
    # Método para agregar miembros a la cuadrilla
    def add_member(self, member):
        self.members.append(member)
    
    # Método para asignar una obra a la cuadrilla
    def assign_work(self, work):
        self.assigned_work = work
    
    # Método para mostrar los miembros de la cuadrilla
    def show_members(self):
        print(f"Squad {self.squad_name} ({self.squad_id}):")
        for member in self.members:
            print(f"- {member}")
    
    # Método para mostrar el trabajo asignado a la cuadrilla
    def show_assigned_work(self):
        if self.assigned_work:
            print(f"La cuadrilla {self.squad_name} esta asignada al proyecto: {self.assigned_work.work_name}")
        else:
            print(f"La cuadrilla {self.squad_name} aún no se le ha asignado ningún proyecto.")


class Work:
    def __init__(self, work_id, work_name, description):
        self.work_id = work_id
        self.work_name = work_name
        self.description = description
    
    # Método para mostrar los detalles de la obra
    def show_details(self):
        print(f"Work {self.work_name} ({self.work_id}): {self.description}")

# Función principal que maneja la interacción con el usuario
def create_work():
    # Ingreso de datos de la obra
    work_id = int(input("Ingrese el ID del proyecto: "))
    work_name = input("Ingrese el nombre de la obra: ")
    description = input("Una breve descripción: ")

    # Creación de la obra con los datos ingresados
    work1 = Work(work_id, work_name, description)

    # Ingreso de datos de la cuadrilla
    squad_id = int(input("Ingrese el ID de la cuadrilla: "))
    squad_name = input("Ingrese el nombre de la cuadrilla: ")

    # Creación de la cuadrilla con los datos ingresados
    squad1 = Squad(squad_id, squad_name)

    # Ingreso de miembros de la cuadrilla
    num_members = int(input("Cuantos miembros tiene esta cuadrilla? "))
    for i in range(num_members):
        member_name = input(f"Número {i + 1}: ")
        squad1.add_member(member_name)