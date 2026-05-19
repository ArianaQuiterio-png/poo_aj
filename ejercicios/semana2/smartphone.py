class Smartphone:
    def __init__(self,pantalla,tamano,camara,grosor,peso,
                 material,puerto,bordes,sensor_huella,botones):
        self.pantalla=pantalla
        self.tamano=tamano
        self.camara=camara
        self.grosor=grosor
        self.peso=peso
        self.material=material
        self.puerto=puerto
        self.bordes=bordes
        self.sensor_huella=sensor_huella
        self.botones=botones
        print(f"Pantalla {self.pantalla}")
        print(f"Tamaño {self.tamano}")
        print(f"Camara {self.camara}")
        print(f"Grosor {self.grosor}")
        print(f"Peso {self.peso}")
        print(f"Material {self.material}")
        print(f"Puerto {self.puerto}")
        print(f"Bordes {self.bordes}")
        print(f"Sensor huella {self.sensor_huella}")
iphone= Smartphone("6.1 pulgadas", "146.7 mm de alto", "2 camaras", 
                   "7.4 mm", "162 gramos","Ceramic shield y aluminio",
                   "Lightning", "Planos", None, "Apagado y encendido y volumen")