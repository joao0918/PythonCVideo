# TUDO DENTRO DE PARENTESES É UM FUNÇÃO
"""
# TRADUÇÃO DAS PALAVRAS USADAS:
# PRINT = IMPRIMIR
# INPUT = ENTRADA, LEIA
"""

print('Hello, World')
print(7+4)

# VARIAVEIS
"""
Sempre escrevar em letras minisculas e se for composto usar o camelCase, toda var recebe valores
"""

nome = 'joao'
idade = 20
peso = 69.8

print(nome,idade,peso)


# RECEBER DADOS
"""
#Leia oque o user digitar
"""
nome = input('qual seu nome? ')
idade = input('qual sua idade? ')
peso = input('qual seu peso? ')

print(nome,idade,peso)

"""EXERCICIOS DA AULA"""
# DESAFIO 1
nome = str(input('Digite seu nome: '))
print(f'Seja Bem-Vindo {nome}')


# DESAFIO 2
dia = int(input('Dia = '))
mes = str(input('Mes = '))
ano = int(input('Ano = '))
print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto? ')

# DESAFIO 3

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

soma = num1 + num2

print(f'Soma entre eles = {soma}')