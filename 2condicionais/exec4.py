# 4-crie um programa que receba uma quantidade de canetas pretas e azuis. A caneta azul vale R$2.00, a caneta preta vale R$2.50. Mostre a quantidade final a ser paga.
# Resposta:

canetapreta = int(input("Informe a quantidade de canetas pretas: "))
canetaazul = int(input("Informe a quantidade de canetas azuis: "))

valor_canetapreta = 2.50
valor_canetaazul = 2.00

total = (canetaazul * valor_canetaazul) + (canetapreta * valor_canetapreta)
print("O total é:", total)