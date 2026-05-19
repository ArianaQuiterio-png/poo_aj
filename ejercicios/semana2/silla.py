class Silla:
    def __init__(self,material,ergonomia,portabilidad,no_patas,
                 color,altura,reclinable,tamaño,peso,diseno):
        self.material=material
        self.ergonomia=ergonomia
        self.portabilidad=portabilidad
        self.no_patas=no_patas
        self.color=color
        self.altura=altura
        self.reclinable=reclinable
        self.tamaño=tamaño
        self.peso=peso
        self.diseno=diseno
        print(f"El material es {self.material}")
        print(f"Ergonomia es {self.ergonomia}")
        print(f"Portabilidad {self.portabilidad}")
        print(f"Numero de patas {self.no_patas}")
        print(f"El color es {self.color}")
        print(f"La altura es de {self.altura}")
        print(f"Es reclinable {self.reclinable}")
        print(f"El tamaño es {self.tamaño}")
        print(f"El peso es {self.peso}")
        print(f"El diseño es {self.diseno}")
silla_estudiante= Silla ("tela negra y fierro", None, None, "4 patas", "negro y plateado",
                         "aproximadamente 1.10 m", None, "90 cm", "3.5 kilos", 
                         "Para estudiante")

        
