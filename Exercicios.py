"""
nome = 'will'
sobrenome = 'Avelar'
idade = 17
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura_metros = 1.75


print('Nome:', nome)
print('Sobre Nome:', sobrenome )
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maio de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

#O Exerecicio aqui é criar as variáveis já que so tinhamos os prints prontos

nome = 'Will'
altura = 1.75
peso = 75
imc = peso // altura ** 2

print('Seu nome é',  nome)
print('Sua altura é', altura)
print('Seu peso é', peso)
print('Seu IMC é',  imc)



primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')




if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')

    """

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")