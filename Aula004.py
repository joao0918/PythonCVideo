# UTILIZANDO MODULOS

"""
Nessa parte utilizaremos bibliotecas em python, que são uma extenção.
utilizando a "import" + biblioteca
Nesse caso ele importa tudo que tem dentro de um biblioteca. Mas generalista

Mas podemos importar somente oque precisamos utilizando: "from" + biblioteva + "import" + comanda.
Esse é mais expecifico 

Exemplos de bibliotecas:
math;

"""

"""
BIBLIOTECA MATH COMANDOS:
math.ceil() = faz um arredondamento para cima;
floor() = faz arredondamento para baixo;
trunc() = ira ilimidar numeros da virgula para frente, sem fazer arredondamento;
pow() = que é potencia, que vai funcionar de forma semelhante aos " ** ";
sqrt() = calcula a raiz quadrada;
factorial() = para calculo de fatorial;
"""

#import math

#num = int(input('digite um numero: '))

#raiz = math.sqrt(num)
#print(math.floor(raiz))


"""
BIBLIOTECA RANDOM COMANDOS:
randon.random() = gera um numero aleatorio entre 0 e 1 (TYPE FLOAT)
random.randint(c,b) = gera um numero inteiro(de c A b) 
"""

#import random

#num = random.randint(1,10)
#print(num)

"""
Install Biblioteca

dentro do terminal digite "pip install nome_biblioteca"
dessa forma pode istalar bibliotecas em python
"""
#import emoji

#print(emoji.emojize('Python is :thumbs_up:'))

"""EXERCICIOS DA AULA"""

# DESAFIO 1

import math

#catetoOposto = int(input("Digite um valor: "))
#catetoAdjacente =int(input("Digite um valor: "))

#hipotenusa = math.ceil(math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2)))

#print(hipotenusa)

# DESAFIO 2

import math

angulo = float(input("Digite o valor do angulo: "))

sen = math.cos(angulo)
cos = math.sin(angulo)
tag = math.tan(angulo)

print(f'O valor do cosseno = {cos:.3f}, seno = {sen:.3f}, tangente = {tag:.3f}')

# DESAFIO 3

import random

print('Programa de sorteio!!!')
num = int(input("Ate que numero deseja sortear: "))

sorteio = random.randint(1,num)

print(f'O numero sorteado foi = {sorteio}')


# DESAFIO 4

import random

listaNome = []
for i in range(1,5):
    nome = str(input('Qual nome do aluno: '))
    listaNome.append(nome)

random.shuffle(listaNome) # ele embaralha a lista de forma aleatoria

print(listaNome)


# DESAFIO 5
    
