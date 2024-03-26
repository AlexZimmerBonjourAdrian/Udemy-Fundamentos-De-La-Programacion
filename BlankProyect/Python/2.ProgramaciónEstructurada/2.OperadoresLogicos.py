#Operadores Logicos

numero_1 = 12
numero_2 = 13
numero_3 = 20

#Operadores Racionales
# #<
# if(numero_1 < numero_2):
#      print(numero_1, "Es menor que", numero_2)
# #>
# elif(numero_1 > numero_2):
#      print(numero_1, "Es mayor que", numero_2)
#<=
# if(numero_1 <= numero_2):
#      print(numero_1, "Es menor igual que", numero_2)
#>=
# elif(numero_1 >= numero_2):
#      print(numero_1, "Es mayor igual que", numero_2)
#!=
# if(numero_1 != numero_2):
#      print(numero_1, "Es diferente a que", numero_2)
# #==
# elif(numero_1 == numero_2):
#      print(numero_1, "Es igual que", numero_2)
#Operadores Logicos

#And
if(numero_1 == numero_2 and numero_1 < numero_3):
     print(numero_1, "Es igual", numero_2, " y ", numero_1, "Es menor a ", numero_3)
#Or
if(numero_1 == numero_2 or numero_1 < numero_3):
     print(numero_1, "Es igual", numero_2, " o ", numero_1, "Es menor a ", numero_3)

#Not

if(not(numero_1 == numero_2) and numero_1 < numero_3):
     print(numero_1, "Es diferente", numero_2, " y ", numero_1, "Es menor a ", numero_3)

