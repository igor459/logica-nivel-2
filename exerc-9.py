# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 
custofabrica = float(input("informe o custo de fabrica do carro:"))
distribuidor = custofabrica * 0.28
imposto = custofabrica * 0.45
custofinal = custofabrica + distribuidor + imposto
print(f"custo final ao consumidor: R${custofinal:.2f}")
