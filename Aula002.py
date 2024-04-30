# TIPOS PRIMITIVOS
"""
# TRADUÇÃO DAS PALAVRAS USADAS:
# PRINT = IMPRIMIR
# INPUT = ENTRADA, LEIA
# TYPE = TIPO
# IS = É
# SPACE = ESPAÇO
# NUMERIC = NUMERICO(A)
# UPPER = SUPERIOR 
# LOWER = BAIXO
# TITLE = TÍTULO
"""

num = int(input('digite um numero: ')) # 2
num2 = int(input('digite mais um numero: '))# 3
s = num + num2
"""
Aqui ele coloca um ao lado do outro, usando o tipo primitivo INT ele recebera somente numero inteiros.
E existem varios outros como: 

flot - numeros com virgula sendo POSITIVO ou NEGATIVO
bool - sendo numero TRUE ou FALSE
str - todas palavras escrevitas ou entao entre aspas que occore dele virar uma str ou str vazia ''
"""

print(s) # CONSIDERO UMA str = 23, USANDO int ISSO SERÁ 5
print(type(s)) # COMMAND SERVE PARA VER O TIPO DE VALOR 

"""EXERCICIOS DA AULA"""

# DESAFIO 1
num = int(input('digite um numero: ')) # 2
num2 = int(input('digite mais um numero: '))# 3
s = num + num2

print(f'soma entre eles é = {s}')

# DESAFIO 2

var = input('digite algo: ')
print(var.isalnum())

"""
variavel.isspace() = ira verificar se somente tem espaços
variavel.isnumeric() = ira verificar se é um numero
variavel.isalpha() = ira verificar se é alfabetico, sendo somente letras
variavel.isalnum() = ira verificar se é alfabetico e numerico
variavel.isupper() = ira verificar se está em maiusculo (a frase inteira)
variavel.islower() = ira verificar se está em minusculo (a frase inteira)
variavel.istitle() = ira verificar se está capitalizada, ou iniciando com uma letra maiuscula

    OBS: 
# A VARIAVEL ANTES DO PONTO (a.is) CHAMAMOS DE "objeto" E TODO OBJETO TEM 
UMA CARACTERISTICAS E REALIZA FUNCIONALIDADE, E TODOS OBJETOS STRING TEM ESSES METODOS
"""