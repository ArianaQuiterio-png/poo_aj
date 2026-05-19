class Perro:
    def __init__(self,pelaje,raza,peso,color,tamano,no_patas,
                 altura,color_ojos,tamano_orejas,fuerza_mordida):
        self.pelaje=pelaje
        self.raza=raza
        self.peso=peso
        self.color=color
        self.tamano=tamano
        self.no_patas=no_patas
        self.altura=altura
        self.color=color
        self.color_ojos=color_ojos
        self.tamano_orejas=tamano_orejas
        self.fuerza_mordida=fuerza_mordida
        print(f"El pelaje es {self.pelaje}")
        print(f"La raza es {self.raza}")
        print(f"El peso es {self.peso}")
        print(f"El color es {self.color}")
        print(f"Es de tamaño {self.tamano}")
        print(f"Tiene {self.no_patas}")
        print(f"Su altura es de {self.altura}")
        print(f"Su altura es de {self.altura}")
        print(f"Sus ojos son de color {self.color_ojos}")
        print(f"Su fuerza de mordida es {self.fuerza_mordida}")
perro_pastor_aleman= Perro ("de manto doble","pastor aleman","30 kilos","Negro con cafe", "Grande",
                            "4 patas","60 cm","cafes","10 cm","238 PSI")