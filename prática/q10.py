def calcular_tabela_preco_carro(valor_carro):
    # Desconto para pagamento à vista
    desconto_vista = 0.20
    preco_vista = valor_carro * (1 - desconto_vista)
    
    # acréscimos para cada quantidade de parcelas
    acrescimos = {
        6: 0.03,
        12: 0.06,
        18: 0.09,
        24: 0.12,
        30: 0.15,
        36: 0.18,
        42: 0.21,
        48: 0.24,
        54: 0.27,
        60: 0.30
    }
    
    # Exibir preço à vista
    print(f"Preço à vista (com 20% de desconto): R$ {preco_vista:.2f}")
    print("Quantidade de Parcelas | Preço Final (R$) | Valor da Parcela (R$)")
    print("-" * 50)
    
    # Calcular e exibir preço final e valor das parcelas para cada opção
    for parcelas, acrescimo in acrescimos.items():
        preco_final = valor_carro * (1 + acrescimo)
        valor_parcela = preco_final / parcelas
        print(f"{parcelas:>20} | {preco_final:>15.2f} | {valor_parcela:>18.2f}")


valor_carro = float(input("Digite o valor do carro: R$ "))
calcular_tabela_preco_carro(valor_carro)
