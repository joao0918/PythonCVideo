# CONDIÇÕES PARTE 1
"""
se e senao(if and else) e temos uma particularidade chamada elif
usando:

if condição:
    faça tal coisa(TRUE)
else:
    senao faça isso(FALSE)

"""

# tempo = int(input('quantos anos tem seu carro? '))

# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro velho')

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))

# media = (n1+n2)/2

# print(f' sua media foi {media}')

# print('Parabens' if media >= 8 else 'estude amis ')

import os
from random import randint
from time import sleep

def clear():
    input('\nPRESS ENTER TO FINISH')
    os.system('cls')


def desafio1():
    print(f'Vou pensar em um numero de 0 até 5, tente adivinhar...')
    num_pensado = randint(0,5)
    numero = int(input('Digite um numero: '))

    print('Processando...')
    sleep(3)
    if numero == num_pensado:
        print('User venceu')
    else:
        print('User perdeu')
        print(f'A maquina pensou no numero {num_pensado}')
    clear()

def desafio2():
    car_speed = int(input('Digite a valocidade do carro: '))

    if car_speed > 80:
        speeding_fine = (car_speed - 80) * 7.00
        print('A velocidade maxima permitda é 80km/h...')
        print(f'You ware fined in {speeding_fine}') 
    else:
        print('Esta dentro do limite de velocidade')
    clear()

def desafio3():
    number_integer = int(input('Digite um numero qualquer: '))

    if (number_integer % 2) == 0:
        print(f'Number entered is even(par)')

    else:
        print(f'Number entered is odd(impar)')

    clear()

def desafio4():
    trip_distance = int(input('Qual a distancia da viagem? '))
    
    if trip_distance <= 200:
        pass_value = 0.50 * trip_distance
        print(f'The value pass = {pass_value}')

    else:  
        pass_value = 0.45 * trip_distance
        print(f'The value pass = {pass_value}')

    clear()

from datetime import date

def desafio5():
    leap_year = int(input('Digite o ano, coloque zero para analisar o ano atual: '))
    if leap_year == 0:
        leap_year = date.today().year # pega o ano atual da maquina

    leap_year_calc = leap_year % 100
    if ((leap_year_calc % 4) == 0) or (leap_year_calc == 00):
        print(f'The year({leap_year}) is leap')
    else:
        print(f'The year({leap_year}) is not leap')

    clear()

def desafio6():
    number_one = int(input('Digite o first numero: '))
    number_two = int(input('Digite o second numero: '))
    number_tree = int(input('Digite o third numero: '))

    smaller = number_tree

    if (number_one < number_two) and (number_one < number_tree):
        smaller = number_one
    if (number_two < number_one) and (number_two < number_tree):
        smaller = number_two


    bigger = number_tree

    if (number_one > number_two) and (number_one > number_tree):
        bigger = number_one
    if (number_two > number_one) and (number_two > number_tree):
        bigger = number_two
    
        

    print(f'the smaller number is {smaller} and the bigger number is {bigger}')
    
    clear()

def desafio7():
    employee_wage = float(input('How much do you earn: ')) # salario do funcionario = quanto voce ganha 

    if employee_wage > 1250.00:
        calc_increase = (employee_wage * 0.10)
        new_salary = employee_wage + calc_increase
        print(f'The increase was {calc_increase:.2f}, the new salary was {new_salary:.2f}')

    else:
        calc_increase =(employee_wage * 0.15)
        new_salary = employee_wage + calc_increase
        print(f'The increase was {calc_increase:.2f}, the new salary was {new_salary:.2f}')

    clear()

def desafio8():
    straigh_one = int(input('Digite o comprimento da first reta: '))
    straigh_two = int(input('Digite o comprimento da second reta: '))
    straigh_tree = int(input('Digite o comprimento da tried reta: '))

    valid1 = straigh_tree < (straigh_one + straigh_two) 
    valid2 = straigh_one < (straigh_two + straigh_tree) 
    valid3 = straigh_two < (straigh_one + straigh_tree)

    if valid1 and valid2 and valid3:
        print('\033[0;33;44;mYes, is possible\033[m') # isso na teoria colocaria cor no text do terminal

    else:
        print('Not is possible')


"""EXERCICIOS DA AULA"""

# CHALLENGE 1
# desafio1()

# CHALLENGE 2
# desafio2()

# CHALLENGE 3
# desafio3()

# CHALLENGE 4
# desafio4()

# CHALLENGE 5
# desafio5()

# CHALLENGE 6
# desafio6()

# CHALLENGE 7
# desafio7()

# CHALLENGE 8
desafio8()


