
n = int(input("Digite o valor de n: "))


for i in range(n):
    # Imprime "_" (sublinhado) i vezes e "*" (asterisco) (n-i) vezes
    print("_" * i + "*" * (n - i))