#Creacion de clases y como interactuan entre si con una clase principal sin metodos mas que los setter y getters
class Persona():
     def __init__(self, Nombre,Apellido,FechaDeNacimiento,EstadoCivil,Sexo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaDeNacimiento= FechaDeNacimiento
        self.EstadoCivil = EstadoCivil
        self.Sexo = Sexo

Per = Persona("Juan","lopez","8/9/2001","Soltero", "M")