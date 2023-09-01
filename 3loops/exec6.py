# 6-utilizando estrutura de repeticao while crie um programa que faça a soma de todos os numeros digitados. o loop so devera parar quando for digitado 0
# Resposta: 

numeros = ()
total = 0
while numeros != 0:
    numeros = int(input("Digite o número, para somar digite 0: "))
    total = total + numeros
print("A soma total é: ", total)