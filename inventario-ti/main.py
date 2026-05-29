from database import *
from enums import *

inicializar_arquivos()
inicializar_vulnerabilidades()

while True:
    print("1. Cadastrar ativo")
    print("2. Buscar ativo")
    print("3. Atualizar ativo")
    print("4. Remover ativo")
    print("5. Gerenciar vulnerabilidades")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        responsavel = input("Digite o responsável: ")
        setor = input("Digite o Setor: ")
        print("Tipos: 1-notebook, 2-celular, 3-computador, 4-servidor, 5-redes")
        tipo = input("Digite o tipo: ")
        salvar_ativos(id, nome, responsavel, setor, tipo)

    elif opcao == "2":
        busca = input("Digite o ID, ou nome para realizar uma busca: ")
        if busca.isdigit():
            ativo = buscar_ativo(int(busca))
        else:
            ativo = buscar_ativo_por_nome(busca)
        if ativo is None:
            print("Ativo não encontrado")
            print()
        else:
            print(ativo)

    elif opcao == "3":
        id = int(input("Digite o ID do ativo a atualizar: "))
        ativo = buscar_ativo(id)
        if ativo is None:
            print("Ativo não encontrado!")
        else:
            nome = input("Digite o novo nome: ")
            responsavel = input("Digite o novo responsável: ")
            setor = input("Digite o novo setor: ")
            print("Tipos: 1-notebook, 2-celular, 3-computador, 4-servidor, 5-redes")
            tipo = input("Digite o novo tipo: ")
            atualizar_ativo(id, nome, responsavel, setor, tipo)
            print("Ativo atualizado com sucesso!")

    elif opcao == "4":
        remover = int(input("Para remover o ativo, digite o ID: "))
        ativo = buscar_ativo(remover)
        if ativo is None:
            print("Ativo não encontrado.")
        else:
            remover_ativos(remover)
            print("Ativo removido com sucesso!")

    elif opcao == "5":
        print("1. Adicionar vulnerabilidade")
        print("2. Visualizar vulnerabilidades")
        sub_opcao = input("Escolha: ")

        if sub_opcao == "1":
            add_vuln_ID_ativo = int(input("Digite o ID do ativo: "))
            ativo = buscar_ativo(add_vuln_ID_ativo)
            if ativo is None:
                print("Ativo não encontrado.")
            else:
                add_vuln_desc = input("Digite a descrição: ")
                add_vuln_categ = input("Digite a categoria: ")
                print("Severidade: 1-baixa, 2-media, 3-alta, 4-critica")
                add_vuln_severidade = input("Digite a severidade: ")
                print("Status: 1-aberta, 2-tratamento, 3-corrigida, 4-aceita_como_risco")
                add_vuln_status = input("Digite o status: ")
                salvar_vulnerabilidade(add_vuln_ID_ativo, add_vuln_desc, add_vuln_categ, add_vuln_severidade, add_vuln_status)
                print("Vulnerabilidade adicionada com sucesso!")

        elif sub_opcao == "2":
            id_ativo = int(input("Digite o ID do ativo: "))
            vulns = carregar_vulnerabilidades(id_ativo)
            if not vulns:
                print("Nenhuma vulnerabilidade encontrada.")
            else:
                for v in vulns.values():
                    print(v)

    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")