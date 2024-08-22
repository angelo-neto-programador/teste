import math

raio = float(input("Digite o valor do raio da esfera: "))

# a) Calcula o comprimento da esfera
comprimento = 2 * math.pi * raio

# b) Calcula a área da esfera
area = 4 * math.pi * raio**2

# c) Calcula o volume da esfera
volume = (4/3) * math.pi * raio**3


print(f"Comprimento da esfera: {comprimento:.2f}")
print(f"Área da esfera: {area:.2f}")
print(f"Volume da esfera: {volume:.2f}")