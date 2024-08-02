'''
TIPOS INT E FLOAT

int -> números inteiros 
O tipo int representa qualquer numero, positivo ou negativo. Int sem sinal é considerado Positivo

Float -> Números com ponto flutuantes o tipo float representa qualquer numero positivo ou negativo com ponto flutuantes
Float sem sinal é considerado positivo


'''
#tipos primitivos
print ("String") #string
print(-1234) #int 
print(2.2) #float

#A FUNÇÃO type MOSTRA O TIPO QUE O PYTHON INFERIU AO VALOR.
#Quando não temos certeza do valor podemos usar a função TYPE, isso irá nos retornar qual é o tipo daquela argumento
print(type('Hello World!')) #<class 'str'>

print(type(1)) #<class 'int'>
#inteiro

#Outro tipo que existe em python são os números de casas decimais, chamados de FLOAT ou Pontos Flutuante
print(type(1.22)) #<class 'float'>

#Se mandarmos imprimir a função abaixo vai retornar str, porque python entende que tudo dentro de aspas é string
print(type("2")) #<class 'str'>
#ou 
print(type("2.2")) #<class 'str'>

#Tambem temos os números Complexos, números complexos são definidos por 2 valores - 
# a Parte real e a parte imaginária em python é escrito na forma real + imag j.
print(type(2 + 3j)) #<class 'complex'>   (?) 

print(1.1, 10.11) #Float
print(0.0, -1.5)#Float
print(type(1.1), type(-0), type(-0.0))