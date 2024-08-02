"""
BOOLLEAN e 

Tipos de dados boll (Boolean)
Ao questionar algo em um programa se existem duas respostas possíveis 
Sim (true) Não (False)
Existem vários operadores para "questionar"
dentre eles o == uqe é um comparador lógico que questiona se um valor é igual a outro 

"""

#CONSTANTES
#True, False, None > essas tbm são palavras chave de python
#True e False são valores Booleanos que representam verdadeiro ou falso 

print(10 == 10) #Sim -> True (Verdadeiro)
print (10 == 1) #Não -> False (Falso)
print(type(10 == 10)) #Nesse caso está me retornando o tipo e não se é true ou false
print(type(20 == 30)) #Nesse caso está me retornando o tipo e não se é true ou false



print(2 > 1)

2 < 1
print(1 > 2)

print(bool(5 > 3))

print(bool(1 == 1))

#Quando bool() não recebe uma expressão vai retornar true ou false
print(bool(0))
print(bool(''))
print(bool(None))
print(bool(1))
print(bool(-190))
print(bool(13.5))
print(bool('Teste'))
print(bool(False))

#O none é um vaor do tipo nonetype é usado para representar uma abstenção de valor.
type(None)
print(type)

#Operadores de comparação 
# a == b         igual
# a != b         diferente  
# a < b          menor    
# a > b          maior
# a <= b         menor ou igual 
# a => b         maor ou igual 

#Outro operadores que retornam Boleanos não 

# a is b         true se a e b forem identics 
# a is not b     true se a e b não são identicos
# a in b         true se a é membro de b 
# a not in b     true se a não é menbro de b 

#Importante lembra que == e is funcionam de maneira diferente

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)

x = [0, 2, 3]
y = [1, 2, 3]
print(x == y)


x is x
print(x is x)

x is not x
print(x is not x)

