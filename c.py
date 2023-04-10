class Cristal:
    def __init__(self, tipo):
        self.tipo = tipo

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def superficie_acristalada(self):
        return sum([ventana.superficie for ventana in self.ventanas])

class Ventana:
    def __init__(self, pared, superficie, cristal):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
        if cristal is None:
            raise Exception("El cristal de la ventana es obligatorio")
        self.cristal = cristal

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        return sum([pared.superficie_acristalada() for pared in self.paredes])

class Cortina:
    def __init__(self, orientacion, superficie):
        self.pared = Pared(orientacion)
        self.ventana = Ventana(self.pared, superficie, Cristal("Ninguna"))

pared_norte = Pared("NORTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
pared_oeste = Pared("OESTE")

ventana_norte = Ventana(pared_norte, 0.5, Cristal("Simple"))
ventana_sur = Ventana(pared_sur, 2, Cristal("Doble"))
ventana_este = Ventana(pared_este, 1, Cristal("Triple"))
ventana_oeste = Ventana(pared_oeste, 1, Cristal("Simple"))

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

cortina = Cortina("NORTE", 0.5)

print(casa.superficie_acristalada())
