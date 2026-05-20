class Coche:
    def __init__(self,marca,modelo,puertas,ventanas,llantas,
                 capacidad,color,cajuela,aire_acondicionado,
                 estandar):
        self.marca=marca
        self.modelo=modelo
        self.puertas=puertas
        self.ventanas=ventanas
        self.llantas=llantas
        self.capacidad=capacidad
        self.color=color
        self.cajuela=cajuela
        self.aire_acondicionado=aire_acondicionado
        self.estanadar=estandar
        print(f"La marca es {self.marca}")
        print(f"El modelo es {self.modelo}")
        print(f"Tiene {self.puertas}")
        print(f"Tiene {self.ventanas}")
        print(f"Tiene {self.llantas}")
        print(f"Tiene una capacidad de {self.capacidad}")
        print(f"Es de color {self.color}")
        print(f"Su cajuela es {self.cajuela}")
        print(f"Tiene aire acondicionado {self.aire_acondicionado}")
        print(f"Es {self.estanadar}")
corvette= Coche("Chevrolet","Corvette C7","2 puertas","2 y un parabrisas",
                "4 llantas","2 personas","Negro","Pequeña",True,"Automatico")
