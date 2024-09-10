from abc import ABC, abstractmethod

# Clase abstracta para la gestión de tareas
class GestorDeTareas(ABC):
    @abstractmethod
    def crear_tarea(self, descripcion, prioridad):
        pass
    
    @abstractmethod
    def editar_tarea(self, id_tarea, nueva_descripcion, nueva_prioridad):
        pass
    
    @abstractmethod
    def eliminar_tarea(self, id_tarea):
        pass
    
    @abstractmethod
    def mostrar_tareas(self):
        pass

# Clase para manejar tareas individuales
class Tarea():
    def __init__(self, id_tarea, descripcion, prioridad):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"ID: {self.id_tarea}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"

# Implementación del Gestor de Tareas
class Gestor(GestorDeTareas):
    def __init__(self):
        self.tareas = {}
        self.contador_id = 1

    def crear_tarea(self, descripcion, prioridad):
        tarea = Tarea(self.contador_id, descripcion, prioridad)
        self.tareas[self.contador_id] = tarea
        print(f"Tarea creada: {tarea}")
        self.contador_id += 1
    
    def editar_tarea(self, id_tarea, nueva_descripcion, nueva_prioridad):
        if id_tarea in self.tareas:
            self.tareas[id_tarea].descripcion = nueva_descripcion
            self.tareas[id_tarea].prioridad = nueva_prioridad
            print(f"Tarea editada: {self.tareas[id_tarea]}")
        else:
            print("Tarea no encontrada.")
    
    def eliminar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            print(f"Tarea eliminada: {self.tareas.pop(id_tarea)}")
        else:
            print("Tarea no encontrada.")
    
    def mostrar_tareas(self):
        if self.tareas:
            for tarea in self.tareas.values():
                print(tarea)
        else:
            print("No hay tareas.")

# Función principal
def main():
    gestor = Gestor()
    
    while True:
        print("\nGestor de Tareas")
        print("1. Crear tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea: ")
            gestor.crear_tarea(descripcion, prioridad)
        
        elif opcion == "2":
            id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_prioridad = input("Ingrese la nueva prioridad: ")
            gestor.editar_tarea(id_tarea, nueva_descripcion, nueva_prioridad)
        
        elif opcion == "3":
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
            gestor.eliminar_tarea(id_tarea)
        
        elif opcion == "4":
            gestor.mostrar_tareas()
        
        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
