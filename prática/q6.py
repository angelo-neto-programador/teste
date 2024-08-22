# Dados dois vetores em python x e y, ambas com n elementos, imprimir o produto escalar desses vetores.

n = int(input("Digite o número de elementos dos vetores: "))

x = []
y = []


print("Insira os elementos do vetor x:")
for i in range(n):
    elemento = float(input(f"Elemento {i+1}: "))
    x.append(elemento)


print("Insira os elementos do vetor y:")
for i in range(n):
    elemento = float(input(f"Elemento {i+1}: "))
    y.append(elemento)


produto_escalar = sum(a * b for a, b in zip(x, y))


print(f"O produto escalar dos vetores x e y é: {produto_escalar}")
