# 2-crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. mostre que ele foi multado. a multa é de 7R$ por cada km acima do limite
# Resposta:

velocidade = float(input("Informe a velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado!, valor da multa:",  multa)