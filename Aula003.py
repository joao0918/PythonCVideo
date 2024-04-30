# OPERAÇOES ARITMEDICAS
"""
# TRADUÇÃO DAS PALAVRAS USADAS:
# PRINT = IMPRIMIR
"""

print(5+2)
print(5-2)
print(5*2)
print(5**2)
print(5/2)
print(5%2)
print(5//2)

"""
OP. ARITMEDICAS :

"+" = ADIÇÃO
"-" = SUBTRAÇÃO
"*" = MULTIPLICAÇÃO
"/" = DIVISÃO
"%" = RESTO DA DIVISÃO
"**" = POTÊNCIA
"//" = DIVISÃO INTEIRA

OP RELACIONAL
"==" = PARA TESTE SE UMA COISA É IGUAL A OUTRA, "=" É USADA PARA ATRIBUIÇÃO
"""

"""
ORGEM DE PRECENDÊNCIA

1. - "()"
2. - "**"
3. - *, /, //, % "sera calculado oque vier primeiro"
4. - "+" e "-" "sera calculado oque vier primeiro"

formatação {:.3f}
para não pular linha and=' '
para quebrar linha \n 
"""

print(5+3*2)
print(3*5+2**2)
print(3*(5+4)**2)

"""EXERCICIOS DA AULA"""

# DESAFIO 1
num = int(input('Digite um numero: '))

print(f'Seu sucessor é {num + 1} e seu antecessor é {num - 1}')

# DESAFIO 2
num = int(input('Digite um numero: '))

print(f'Aqui esta o seu dobro = {num*2}, seu triplo = {num*3} e sua raiz quadrada = {num**(1/2):.1f}')

# DESAFIO 3
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))

print(f'Aqui está a sua média = {(nota1 + nota2) / 2}')

# DESAFIO 4

m = float(input('Digite um valor em metros: '))

print(f'Aqui esta seu valor digitado em metros convertido para centimetros = { m / 60}')
print(f'Aqui esta centimetros convertido para milimetros = {(m / 60) / 60}')

# DESAFIO 5

num = int(input('Digite um numero: '))

for i in range(0 ,11):
    print(f'{num} x {i} = {num * i}')

# DESAFIO 6
    
maneyInDorlar = float(input('Digite quanto de dinheiro voce tem: '))

convert = maneyInDorlar * 3.37

print(f'Valor convertido em dolar: {convert}')

# DESAFIO 7

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

metrosQuadrados = largura * altura
latasDeTinta = metrosQuadrados / 2

print(f'Quantidade de latas de tinta necessaria: {latasDeTinta} m2')

# DESAFIO 8

produtoSemDesconto = float(input('Digite o valor do produto para aplicar o desconto de 5%: '))

produtoComDesconto = produtoSemDesconto - (produtoSemDesconto * 0.05 )

print(f'Valor do produto com desconto: {produtoComDesconto}')

# DESAFIO 9

salario = float(input('Digite o seu salario: '))

salarioComAumento = salario + (salario * 0.15 )

print(f'Seu salario teve um aumento para: {salarioComAumento:.2f}')

