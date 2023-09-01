# 3- Crie um programa que leia dois numeros e que exiba True se o primeiro numero for maior que o primeiro e False se o primeiro numero for menor ou igual ao segundo numero
# Resposta:

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

if numero1 > numero2:
    print("True")
    
elif numero2 >= numero1:
    print("False")