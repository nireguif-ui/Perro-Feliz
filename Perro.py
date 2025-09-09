class Perro_feliz:
   
    def __init__(self,edad,nombre,color_ojos):
        
        self.edad = int (edad)
        self.nombre = nombre
        self.color_ojos = color_ojos

    def comer(self):
        print(f"Le dieron de comer a {self.nombre}, es feliz.")
    def pasear(self):
        print(f"Pasearon a {self.nombre}, es feliz.")
    def acariciar(self):
        print(f"Acariciaron a {self.nombre}, es feliz.")

mi_perro = Perro_feliz(3, "Tommy", "Cafe")

mi_perro.comer()
mi_perro.pasear()
mi_perro.acariciar()