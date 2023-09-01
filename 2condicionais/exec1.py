# 1-crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)
# Resposta:

idade = int(input("Informe sua idade: "))

if idade > 18:
    print("Apto")
    
elif idade < 18:
    print("Não apto")
