class Mesa:
    def __init__(self, material, ancho, diseno,tamano,tipo,altura,
                 color,portabilidad,soporte,no_patas):
        self.material=material
        self.ancho=ancho
        self.diseno=diseno
        self.tamano=tamano
        self.tipo=tipo
        self.altura=altura
        self.color=color
        self.portabilidad=portabilidad
        self.soporte=soporte
        self.no_patas=no_patas
        print(f"El material es {self.material}")
        print(f"Su ancho es de {self.ancho}")
        print(f"Su diseño es {self.diseno}")
        print(f"El tamaño es {self.tamano}")
        print(f"El tipo es {self.tipo}")
        print(f"La altura es {self.altura}")
        print(f"El color es {self.color}")
        print(f"Portabilidad {self.portabilidad}")
        print(f"Su soporte es {self.soporte}")
        print(f"Tiene {self.no_patas}")
mesa_estudiante= Mesa ("madera y fierro", "1.10 m","de oficina","grande","para estudiante",
                       "1.30 m","blanca y negro",None,None,"4 patas" )