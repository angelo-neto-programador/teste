# Escreva um programa em Python que calcule a área de um círculo com base no raio inserido pelo usuário.

import math

raio = float(input("Digite o valor do raio do círculo: "))

area = math.pi * raio**2

print(f'A área do círculo com raio {raio} é: {area:.2f}')

