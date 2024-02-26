# i = 0

# def normarecurcive():
#     global i 
#     i += 1
#     print(i)
#     if(i>=5):
#         print("Se termino")
#         return
#     normarecurcive()

# normarecurcive()

# def recursividadonVariables(X):

#     print(X)
#     if X >= 5: 
#         return
        
#     return recursividadonVariables(X+1)

#     print(recursividadonVariables(0))

# Lista_Mix= [1,2,3,4,5,"No", "No"]

# def EsunNumero(List, index):
#     if index < len(List) :
      
#         if (str)(List[index]).isdigit():
#           print(List[index])
#           print("Es un numero!")
#         else:
#             print(List[index])
#             print("No es un numero")
    
#         EsunNumero(List,index+1)
#     else:
#         return
    
# EsunNumero(Lista_Mix, 0)


def indices(List):
    for i in range(len(List)):
        yield i

def FindNumber(List, numberSearch):
    for index in indices(List):
        if List[index] == numberSearch:
            return numberSearch
    return 
    
print(" ")
numero_List = [1,2,3,4,5,6,7,8]
print(FindNumber(numero_List, 0))