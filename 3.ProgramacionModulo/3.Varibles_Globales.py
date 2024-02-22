#variables globales

#Declarada de esta manera python la considera de forma globale
#se puede tratar de declarar las variables

x=5
#las variables locales estan definidas dentro un metodo, esto puede ser una clase o una funcion

#vairalbe local, las variables locales son temporales y se usan dentro de las funciones para sus operaciones
def showXLocal():
   
    X = x + 2
    print("El valor de x es", x)

showXLocal()


#variable global
def showXGlobal():
   global x
   x = x + 2
   print("El valor de x es", x)

showXGlobal()

#esta es una forma doferete de acceder a una variable global
def X():
    global x
    x=10

X()

def mostrarX():
    print("El valor de x es ", x)

mostrarX()

#este es un adelanto del siguiente modulo

# class person:
#     nombre = "Juan"

#     #anteriormente no podiamos modificar una variable global ahora si, por que?
#     #por que esta no es una variable global es local, local de la clase
#     #nadie ademas de la clase y las funciones la pueden modificar o ver
#     #si queremos volverla global suaremos los metodos anteriormente hechos

#     def cambiar_nombre(self, nuevo_nombre):
#         self.nombre = nuevo_nombre
    

    
#     print(nombre)

    

    