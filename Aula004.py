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
ceil() = faz um arredondamento para cima;
floor() = faz arredondamento para baixo;
trunc() = ira ilimidar numeros da virgula para frente, sem fazer arredondamento;
pow() = que é potencia, que vai funcionar de forma semelhante aos " ** ";
sqrt() = calcula a raiz quadrada;
factorial() = para calculo de fatorial;
"""

import math

num = int(input('digite um numero: '))

raiz = math.sqrt(num)
print(raiz)


"""
BIBLIOTECA RANDOM COMANDOS:
randon.random() = gera um numero aleatorio entre 0 e 1 (TYPE FLOAT)
random.randint(c,b) = gera um numero inteiro(de c A b) 
"""

