# 5-crie um programa que leia o nome de tres pessoas: João Maia, João Abrantes e Pedro. Para os respectivos nomes imprima:'oi eu sou joao maia', 'oi eu sou joao abrantes', 'oi eu sou pedro', e caso o nome nao seja nenhum dos tres imprima 'oi meu nome é {nome}'
# Resposta:

nome = input("Informe seu nome: ")

if nome == 'João Maia':
    print("Oi eu sou João Maia")
    
elif nome == 'João Abrantes':
    print("Oi eu sou João abrantes")
    
elif nome == 'Pedro':
    print("Oi eu sou Pedro")
    
else:
    print("Oi meu nome é", nome)