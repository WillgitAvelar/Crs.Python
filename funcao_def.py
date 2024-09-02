#Em Python, a palavra-chave def é usada para definir uma função.
# Uma função é um bloco de código reutilizável que realiza uma tarefa específica. 
# Funções permitem que você organize seu código de maneira modular e eficiente.

#Sintaxe Básica de uma Função
#Aqui está um exemplo básico de como uma função é definida em Python:

def nome_da_funcao(parametro1, parametro2):
    # Corpo da função
    resultado = parametro1 + parametro2
    return resultado

#def: Inicia a definição da função.
#nome_da_funcao: O nome que você escolhe para a função. Deve seguir as regras de nomes de variáveis em Python.
#parametro1, parametro2: Parâmetros são valores que você pode passar para a função para personalizar seu comportamento. Você pode ter quantos parâmetros forem necessários, incluindo nenhum.
#:: Os dois pontos indicam o início do corpo da função.
#Corpo da função: O bloco de código indentado que define o que a função faz.
#return: (Opcional) Usado para retornar um valor da função. Se return não for usado, a função retornará None por padrão.

#Vamos definir uma função simples que soma dois números:
def soma(a, b):
    resultado = a + b
    return resultado

#Agora, podemos chamar essa função em qualquer parte do nosso código:
resultado = soma(3, 5)
print(resultado)  # Saída: 8


#Funções Sem Parâmetros
#Você também pode definir uma função que não aceita parâmetros:

def diga_ola():
    print("Olá!")
    
#Chame a função assim:
diga_ola()  # Saída: Olá!

#Funções Com Parâmetros Padrão
#Você pode definir valores padrão para os parâmetros de uma função. Se o valor não for fornecido ao chamar a função, o valor padrão será usado:
def cumprimentar(nome="Mundo"):
    print(f"Olá, {nome}!")
#Chamadas da função:
cumprimentar("Maria")  # Saída: Olá, Maria!
cumprimentar()         # Saída: Olá, Mundo!


#Funções com Argumentos Variáveis
#Você pode usar *args e **kwargs para passar um número variável de argumentos para uma função:

#*args permite passar um número variável de argumentos posicionais.
#**kwargs permite passar um número variável de argumentos nomeados.
#Exemplo:



def minha_funcao(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

minha_funcao(1, 2, 3, a=4, b=5)


args: (1, 2, 3)
kwargs: {'a': 4, 'b': 5}
#Funções Aninhadas e Escopo
#Você pode definir funções dentro de outras funções. Isso cria uma função aninhada. As variáveis definidas dentro de uma função têm escopo local e não são acessíveis fora dessa função.


def funcao_externa():
    x = 10
    def funcao_interna():
        print(x)
    funcao_interna()

funcao_externa()  # Saída: 10

#Docstrings
#Você pode adicionar uma docstring (uma string multilinha) logo após a definição da função para documentar seu propósito e como ela deve ser usada.


def soma(a, b):
    """
    Soma dois números e retorna o resultado.

    Parâmetros:
    a (int, float): O primeiro número.
    b (int, float): O segundo número.

    Retorna:
    int, float: O resultado da soma de a e b.
    """
    return a + b
#A docstring pode ser acessada com a função help ou o atributo __doc__:

print(soma.__doc__)






