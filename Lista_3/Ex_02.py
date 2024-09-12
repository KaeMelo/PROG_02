agenda_telefonica = {}

def incluir_novo_nome(nome, *telefones):
    if nome not in agenda_telefonica:
        agenda_telefonica[nome] = list(telefones)
    else:
        agenda_telefonica[nome].extend(telefones)

def incluir_telefone(nome, telefone):
    if nome in agenda_telefonica:
        agenda_telefonica[nome].append(telefone)
    else:
        incluir_novo_nome(nome, telefone)

def excluir_telefone(nome, telefone):
    if nome in agenda_telefonica:
        if telefone in agenda_telefonica[nome]:
            agenda_telefonica[nome].remove(telefone)
            if len(agenda_telefonica[nome]) == 0:
                del agenda_telefonica[nome]
                print(f"{nome} foi excluído da agenda, pois não possui mais telefones.")
            else:
                print(f"Telefone {telefone} excluído com sucesso para {nome}.")
        else:
            print(f"Telefone {telefone} não encontrado para {nome}.")
    else:
        print(f"{nome} não encontrado na agenda.")

def excluir_nome(nome):
    if nome in agenda_telefonica:
        del agenda_telefonica[nome]
        print(f"{nome} foi excluído da agenda.")
    else:
        print(f"{nome} não encontrado na agenda.")

def consultar_telefone(nome):
    if nome in agenda_telefonica:
        print(f"Telefones de {nome}: {', '.join(agenda_telefonica[nome])}")
    else:
        print(f"{nome} não encontrado na agenda.")

while True:
    print("\n======= Agenda Telefônica =======")
    print("Escolha uma opção:")
    print("1. Incluir novo nome")
    print("2. Incluir telefone")
    print("3. Excluir telefone")
    print("4. Excluir nome")
    print("5. Consultar telefone")
    print("6. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome a ser incluído: ")
        telefones = input("Digite os telefones separados por vírgula: ").split(",")
        incluir_novo_nome(nome, *telefones)
    elif opcao == "2":
        nome = input("Digite o nome para adicionar telefone: ")
        telefone = input("Digite o telefone a ser incluído: ")
        incluir_telefone(nome, telefone)
    elif opcao == "3":
        nome = input("Digite o nome para excluir telefone: ")
        telefone = input("Digite o telefone a ser excluído: ")
        excluir_telefone(nome, telefone)
    elif opcao == "4":
        nome = input("Digite o nome a ser excluído: ")
        excluir_nome(nome)
    elif opcao == "5":
        nome = input("Digite o nome para consultar telefones: ")
        consultar_telefone(nome)
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
