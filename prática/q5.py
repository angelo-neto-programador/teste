# Escreva um programa Python que receba uma sequência de n valores, imprima na ordem inversa à da leitura.

n = int(input("Quantos valores você deseja inserir? "))
valores = []

for i in range(n):
    valor = input(f"Digite o valor {i+1}: ")
    valores.append(valor)

print("Valores na ordem inversa:")
for valor in reversed(valores):
    print(valor)