class Alumno:
    def __init__(self,nombre, color_ojos,color_cabello,tez,cabello,
                 complexion,edad,carrera,matricula,horario_clases,taller,):
        self.nombre=nombre
        self.color_ojos=color_ojos
        self.color_cabello=color_cabello
        self.tez=tez
        self.cabello=cabello
        self.complexion=complexion
        self.edad=edad
        self.carrera=carrera
        self.matricula=matricula
        self.horario_clases=horario_clases
        self.taller=taller
        print(f"Su nombre es {self.nombre}")
        print(f"Es color de sus ojos es {self.color_ojos}")
        print(f"Su color de piel es {self.color_cabello}")
        print(f"Su piel es {self.tez}")
        print(f"Su cabello es {self.cabello}")
        print(f"Su complexion es {self.complexion}")
        print(f"Tiene {self.edad}")
        print(f"Su carrera es {self.carrera}")
        print(f"Su matricula es {self.matricula}")
        print(f"Su horario es {self.horario_clases}")
        print(f"Esta en taller de {self.taller}")
Angel= Alumno ("Angel","Cafe","Negro","Moreno","Lacio","Delgado","18 años",
               "Criminologia",152425443,"Matutino","Futbol")