#FUNÇÃO PRINT 
#ARGUMENTOS
#QUEBRA DE LINHA \r\n ou simplismente feito automaticamente pelo CRLF (Caso esteja em windows mais antigo talves tenha que comandar \rou\n para quebrar linhas)

#... podemos usar tres pontos quando não concluimos ainda o comando py vai passar por ele sem dar erro   


print('Hello World')
# A Função print mada algo pra tela
# Ela recebe uma coisa que chamamos de argumento 

# Podemos utilizar o argumento 
print(12) 


#Print tambem funciona para números
print(1) # diferente da str ou string números não precisão de aspas 


# Ou caso queira usar mais de uma argumento separe-os por vitgula 
print(12, 65, "teste") 
#podemos chamar esse print acima de agumentos não nomeados, pois passamos os argumentos e queremos que a função print apenas exiba na tela.

print(12, 34, 56, sep="-")
print(78, 90, sep=',')
# Esses dois exemplos acima são argumentos nomeados - dentro do argumento chamamos a sep="" e dizemos como queremos separar os argumentos.

# Mais um argumento importante que podemos ver é o end=
print(12, 34, 56, sep="-", end="##\n")
print(78, 90, sep=',', end=".\n")

#repare que a palavra teste está entre aspas, pois ela é uma string.
#Strings são textos ou palavras que precisão estar dentro de aspas.
print("Teste com texto ou palavras")

# Em Python não utilizamos letras maiusculas por exemplo Print()

# O hasteg é utilizado para fazer comentários sem que sejam executados 

'''
Docstrings como comentários 
Outra forma de comentar é utilizando as aspas, dessa forma podemos comentas linhas 
mas lembrando que o py le o que está qui mas não interpreta
'''


#Pesquisar sobre: pypy, pep,  