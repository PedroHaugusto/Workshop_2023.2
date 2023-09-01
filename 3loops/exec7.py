# 7-utilizando estrutura de repeticao while crie um programa que leia exclusivamente o sexo como 'F' e 'M' e o loop so deve terminar quando sexo for = sair. ao fim mostre a quantidade e mulheres e homens
# Resposta: 

mulheres = 0
homens = 0

while True:
    sexo = input("Digite o sexo (F para feminino, M para masculino, ou 'sair' para encerrar): ").upper()

    if sexo == "F":
        mulheres += 1
    elif sexo == "M":
        homens += 1
    elif sexo == "SAIR":
        break
    else:
        print("Opção inválida. Digite 'F' para feminino, 'M' para masculino, ou 'sair' para encerrar.")

print(f"Quantidade de mulheres: ", mulheres)
print(f"Quantidade de homens: ", homens)
