# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(int('1'), type(int('2')))#Neste caso foi passado a função int pra ser feita a coerção do tipo
#Foi convertido o numero 1 em inteiro pq estava como str.
print(int('1') + 1) #Suponhamos que queremos converter o '1' que está como str em int para fazer a soma  
#deveremos colocar a função int para que isso aconteça

print(float('1') + 1) #neste caso fizemos a coerção para um float 
print(type(float('1') + 1))  #neste caso envolvemos o float para saber a tipo 

print(bool(' ')) #uma str que possa ter apenas uma espaço é considerada True
print(bool('')) #uma str vazia é considerada False

print(str(11) + 'b') # convertendo um int para str - neste caso ele concatenou 

