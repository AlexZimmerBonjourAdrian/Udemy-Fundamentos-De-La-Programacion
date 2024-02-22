#continue, break,

#break:
#permite salir de bucle actual  continuar con la ejecucion del codigo
print("Break")
for i in range(10):
    if i == 5:
        break
    print(i)
print("El bucle ha terminado")

print(" ")

print("continue")
#continue:
#permite saltarse el resto de la interacion actual y continuar con la siguiente iteracion
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("El bucle ha terminado")

print(" ")

print("pass")
#pass:
#permite saltarse a la siguiente intencion actual y continuar con la siguiente interacion
def my_function():
    pass

my_function()

print(" ")


print("return")
#return:
#permite pasar a la siguinte iteracion sin realizar ninguna accion
#la funcion puede devolver un valor hay se usa return tambien
def suma(a, b):
    return a + b

result = suma(2, 3)
print(result)

print(" ")

print("yield")
#yield:
#permite generar un valor y continuar con la ejecucion de la funcion en la proxima llamada
def fibonacci(n):
    a, b = 0, 1
    
    #_ se utliza para ignorar un valor de una expression esto es por que, no nesecitamos lo que regresa range
    for _ in range(n):
        #se usa devolver los elementos de forma secuencial, esto es para esperar un input 
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

print(" ")

def numeros_enteros():
    for i in range(10):
        yield i

generador = numeros_enteros()
print(generador.__next__())  # Imprime 0
print(generador.__next__())  # Imprime 1
print(generador.__next__())  # Imprime 2
print(generador.__next__())  # Imprime 3


print(" ")
for numero in generador:
    print(numero)


numeros_enteros()
print(" ")

