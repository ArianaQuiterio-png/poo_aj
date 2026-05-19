class Transporte:
    def __init__(self, llantas,ventanas,modelo,marca,puertas,
                 aire_acondicionado,color,placa,capacidad,cajuela):
        self.llantas=llantas
        self.ventanas=ventanas
        self.modelo=modelo
        self.marca=marca
        self.puertas=puertas
        self.aire_acondicionado=aire_acondicionado
        self.color=color
        self.placa=placa
        self.capacidad=capacidad
        self.cajuela=cajuela
        print(f"Tiene {self.llantas}")
        print(f"Tiene {self.ventanas}")
        print(f"Es modelo {self.modelo}")
        print(f"Es marca {self.marca}")
        print(f"Tiene {self.puertas}")
        print(f"Aire acondicionado {self.aire_acondicionado}")
        print(f"Es de color {self.color}")
        print(f"Tiene placa {self.placa}")
        print(f"Tiene una capacidad de {self.capacidad}")
        print(f"Su cajuela es {self.cajuela}")
uber= Transporte ("4 llantas", "4 ventanas", "Versa", "Nissan", "4 puertas",
                  None, "Negro", "1234231", "4 personas", "Grande")

                  