# Escreva um programa Python para combinar dois dicionários adicionando valores para chaves comuns.

dic1 = {'x': 53, 'y': 27, 'z': 100}
dic2 = {'x': 33, 'y': 5, 'z': 1000}

dic_combinado = {key: dic1.get(key, 0) + dic2.get(key, 0) for key in set(dic1) | set(dic2)}

print(f"O dicionário combinado é: {dic_combinado}")
