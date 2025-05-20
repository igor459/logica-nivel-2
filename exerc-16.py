# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("digite a nota da 1 avaliação:"))
nota2 = float(input("digite a nota da 2 avaliação:"))
media = (nota1 + nota2) / 2
if media>= 6:
    print(F"Aprovado com media{media:.2f}")
else:
    print(F"Reprovado com media{media:.2f}")
