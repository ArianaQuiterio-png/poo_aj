class Libro:
    def __init__(self,titulo,num_paginas,edicion,fecha_publicacion,caratula,
                 tipo_papel,peso,tamano,color,separador):
        self.titulo=titulo
        self.num_paginas=num_paginas
        self.edicion=edicion
        self.fecha_publicacion=fecha_publicacion
        self.caratula=caratula
        self.tipo_papel=tipo_papel
        self.peso=peso
        self.tamano=tamano
        self.color=color
        self.separador=separador
        print(f"El titulo del libro es {self.titulo}")
        print(f"Tiene {self.num_paginas}")
        print(f"Es edicion {self.edicion}")
        print(f"Se publico el {self.fecha_publicacion}")
        print(f"Su caratula es {self.caratula}")
        print(f"Su papel es {self.tipo_papel}")
        print(f"Su peso es de {self.peso}")
        print(f"Su tamaño es {self.tamano}")
        print(f"El color del libro es {self.color}")
        print(f"Tiene separador {self.separador}")
Amor_libro= Libro("Yo antes de ti","496 paginas","Rustica","15 de enero del 2012",
                  "Blanca con solapas, tiene fondo azul claro con los protagonistas",
                  "Tipo ahuesado","500 gramos","15 x 23 cm","Portada multicolor",None)


