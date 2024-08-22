#  Escreva um programa em Python para calcular a diferença entre um determinado número e 17.
#  Se o número for maior que 17, retorne o dobro da diferença absoluta.

numero = float(input("Digite um número: "))

diferenca = numero - 17

if numero >17:
    resultado = abs(diferenca) * 2
else:
    resultado = abs(diferenca)

print(f"O resultado é: {resultado}")
