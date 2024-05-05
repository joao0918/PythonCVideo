# MANIPULANDO TEXTO

# FATIAMENTO STR

from re import split


frase = 'joao pedro o lindao gato'

print(frase[0:10]) # de 0 ate 9
print(frase[0:10:2]) # de 0 ate 9 pulando de 2 em 2
print(frase[:9]) # inicio ate 9
print(frase[3:]) # 3 ate o fim
print(frase[3::2]) # 3 ate o fim de 2 em 2

# ANALISE DE STR

print(len(frase)) # le o numero de caracteres de um frase
print(frase.count('o')) # Ele le o numero de 'o' dentro da frase
print(frase.count('o',0,13)) # Aqui ele vai ler entre 0 e 13 quantas que tem
print(frase.find('jo')) # Quantas vezes ele encontrou 
print(frase.find('android')) # algo que não existe responde como '-1'
print('joao' in frase) # existe curso em frase

# TRANSFORMAÇÃO

print(frase.replace('joao','android')) # vai procurar joao e trocar por android, ele substitui
print(frase.upper()) # Ficar td em letras maiusculas
print(frase.lower()) # Fica td em minusculos
print(frase.capitalize()) # jogar tudo para minusculo e a 1 letra em maiusculo
print(frase.title()) # Todas as letras após os espaços ficarao com letras mauscula
print(frase.strip()) # Remove espaços inuteis do inicio e do final
print(frase.rstrip()) # Remove os espaços da direita
print(frase.lstrip()) # Remove os espaços da esquerda

# DIVISAO

print(frase.split()) # Divide a frase de acordo com os espaços, ele quebra essas rases em novos itens de uma lista, divide em uma lista

# JUNÇÃO
joao = frase.split()
print(joao[3][2])
print('-'.join(joao))
"""
A string ela é imutavel, portando fazendo assim ela não vai conseguir ser alterada
a não ser que eu guarde dentro da variavel "frase"
"""

"""EXERCICIOS DA AULA"""

# DESAFIO 1

nome = input('Escreva seu nome completo: ')

print(nome.upper())
print(nome.lower())

nome = nome.split()
print(len(''.join(nome)) + 1)
print(len(nome[0]))


# DESAFIO 2

num = int(input('digite um numero: '))

print(f'Unidade: {num%10}\nDezena: {(num%100)//10}\nCentena: {(num%1000)//100}\nMilhar: {(num%10000)//1000}')

# DESAFIO 3

nome_cidade = str(input('Digite o nome da dua cidade:'))
nome_cidade = nome_cidade.upper()

comeca_com_santo = nome_cidade.split()
comeca_com_santo = comeca_com_santo[0].find('SANTO')


if comeca_com_santo == -1:
    print(f'A cidade {nome_cidade.lower().title()} não começa com "santo"')

else:
    print(f'A cidade {nome_cidade.lower().title()} começa com "santo"')

# DESAFIO 4

name = str(input('Digite seu nome: '))
name = name.lower()
tem_silva = name.find('silva')

if tem_silva == -1:
    print(f'O nome {name.title()} não tem "silva"')

else:
    print(f'O nome {name.title()} tem "silva"')

# DESAFIO 5

frase1 = str(input('Digite uma frase: '))

print(frase1.count('a')) # quantidade de a
print(frase1.find('a')) # primeiro a
print(frase1.find('a',-1)) # ultimo a

# DESAFIO 6

nomeCompleto = str(input('Seu nome completo: '))
nomeseparado = nomeCompleto.split()

print(nomeseparado[0])
print(nomeseparado[-1])