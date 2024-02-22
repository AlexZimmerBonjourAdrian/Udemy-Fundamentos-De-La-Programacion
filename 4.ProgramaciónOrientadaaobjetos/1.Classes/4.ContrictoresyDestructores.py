
class celular:
    #Consturctor de celular
        def __init__(self, marca, modelo, camera,espacioDisco,ram,grafica):
            self.marca = marca
            self.modelo = modelo
            self.camera = camera
            self.espacioDisco = espacioDisco
            self.ram = ram
            self.grafica = grafica
         
        def __del__(self):
        #Los destructores son eliminar el objeto, y que realicen alguna accion o ejecuten un metodo antes se pueden utilizar este metodo
         print("Destroying object...")

print("Crear celulares")

celular_list = []      
celular_1 = celular("sansung","S23","40MPX", 60,"2GB","integrada 500mb")
celular_2 = celular("sansung","S23","40MPX", 60,"6GB","integrada 500mb")

print("Agregar a la lista")

celular_list.append(celular_1)
celular_list.append(celular_2)

print(len(celular_list))

print("Borrar el celular 1")

#Forma 1 de desruir un objeto pero no se eliina de la lista ya que es none no esta eliminado de memoria en si
celular_list[1] = None

#Forma 2 de desturir una objeto
del celular_list[0]


del celular_list[0]

#Produce un error ya que celular_1 y celular_2 dejaron de existir
# print(celular_list[0].ram)

print(len(celular_list))

#__init_ que objeto es un constructor para una objeto estandar
class Coche:
    def __init__(self, color, modelo, velocidad):
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad


#__new__ Este método se llama antes de que se cree un nuevo objeto de una clase. Su función es crear un objeto vacío y luego se llena con datos en el método

class Coche:
    #cls es un metodo que se usa para una clase que se esta creando
    def __new__(cls):
        obj = super().__new__(cls)
        obj.color = None
        obj.modelo = None
        obj.velocidad = None
        return obj

# __call__ Este método se llama cuando se llama a un objeto como si fuera una función. Su función es permitir que un objeto se pueda llamar como una función. El método __call__ se define dentro de la clase y se utiliza para definir la lógica de la función. Por ejemplo:
class Coche:
    def __call__(self, *args, **kwargs):
        print("Voy a conducir mi coche")
        # Lógica de la función aquí

coche = Coche() #objeto vacio que se puede rellenar con datos despues

coche = Coche()() #Este seria una funcion