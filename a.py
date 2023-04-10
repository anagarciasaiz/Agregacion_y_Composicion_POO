class Ciudad:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def add_edif(self, edif):
        self.edificios.append(edif)
    
    def get_edifs(self):
        return self.edificios
    def __del__(self):
        self.nombre = ""
        self.edificios = []

class Edificio:
    nombre = ""
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre


class Empresa:
    def __init__(self, nombre, list_empleados, list_edificios):
        self.nombre = nombre
        self.list_empleados = list_empleados
        self.list_edificios = list_edificios

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    
martin = Empleado("Martin")
salim = Empleado("Salim") 
xing = Empleado("Xing")
edif_a = Edificio("A")
edif_b = Edificio("B")
edif_c = Edificio("C")
list_edificios = [edif_a, edif_b, edif_c]
list_empleados = [martin, salim, xing]
yoohoo = Empresa("Yoohoo!", list_empleados, list_edificios)
ny = Ciudad("Nueva York")
la = Ciudad("Los Angeles")
ny.add_edif(edif_a)
ny.add_edif(edif_b)
la.add_edif(edif_c)
