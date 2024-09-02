
#o que faz o f strg?
#Em Python, o f é usado para criar f-strings, que são uma forma de formatar strings de maneira simples e expressiva. 
# As f-strings foram introduzidas no Python 3.6 e permitem incorporar expressões dentro de strings, que são avaliadas 
# no momento da execução.

nome = "Maria"
idade = 30
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos." #Neste exemplo, a f-string permite inserir as variáveis nome e idade diretamente dentro da string.
print(mensagem)

#As f-strings também permitem expressões mais complexas, como:
largura = 10
altura = 5
area = f"A área do retângulo é {largura * altura} metros quadrados."
print(area)
