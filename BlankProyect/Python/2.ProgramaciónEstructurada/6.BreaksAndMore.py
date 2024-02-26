#Break
print("break")
for i in range(10):
    if i== 5:
        break
    print(i)
print("El bucle ha terminado")

print("continuar")
for i in range(10):
    if i % 2== 0:
        continue
    print(i)
print("El bucle ha terminado")

print("continuar")
for i in range(10):
    if i % 2== 0:
        pass
    print(i)
print("El bucle ha terminado")


print("return")

def suma(a,b):
    return a+b
#return tambien puede ser para finalizar una funcion sin que devuelva nada o evitar un error
result = suma(2,3)
print(result)

print(" ") 

print("yield")

def fibonacci(n):
    a,b = 0, 1

    for _ in range(n):
        yield a
        a,b = b, a + b

for num in fibonacci(10):
    print(num)

print(" ")

def numeros_enteros():
    for i in range(19):
        yield i

print(numeros_enteros())

print("Generador de numeros enteros")
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