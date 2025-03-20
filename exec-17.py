# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano = float(input("digite o ano atual:"))
nasc = float(input("digite o ano que nasceu:"))
idade = (ano - nasc)
if idade >= 18:
    
    print("Pode votar!")
else:
    print("Não pode votar!")
