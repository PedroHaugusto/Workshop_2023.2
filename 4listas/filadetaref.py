# 1- Fila de tarefas: 
# Resposta:

tarefas = []
while True:
    print("Digite o que fazer:")
    print("1. Adicionar tarefa")
    print("2. Executar fila de tarefas")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a descrição da tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada à fila.")
    elif escolha == "2":
        if tarefas:
            executar = tarefas.pop(0)
            print("Executando:", executar)
        else:
            print("A fila de tarefas está vazia.")
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")