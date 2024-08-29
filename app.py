import os

medicamentos = [{"nome":"Paracetamol", "Categoria":"Tarja Branca","ativo": True},
    {"nome":"Valium", "Categoria":"Tarja Preta","ativo": False},
    {"nome":"Ritalina", "Categoria":"Tarja Amarela","ativo": True}]


def mostra_titulo():
    print("""
    ███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░        
    ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗
    █████╗░░███████║██████╔╝██╔████╔██║███████║██║░░╚═╝██║███████║
    ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██╔══██║                         
    ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║██║░░██║
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝     

    ░█████╗░███╗░░██╗██████╗░██████╗░███████╗
    ██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
    ███████║██╔██╗██║██║░░██║██████╔╝█████╗░░
    ██╔══██║██║╚████║██║░░██║██╔══██╗██╔══╝░░
    ██║░░██║██║░╚███║██████╔╝██║░░██║███████╗
    ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚══════╝""")

def mostra_escolhas():
    print("1. Cadastrar Medicamentos")
    print("2. Listar Medicamentos")
    print("3. Ativar Estoque ")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        print(texto)
        print(" ")

    def retorna_menu():
        input(" Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastra_medicamentos():
        exibir_subtitulo("Cadastar medicamentos")

        nome_medicamento = input(" Digite o nome do medicamento que deseja cadastrar ")
        categoria_medicamento = input( f"Digite a categoria do {nome_medicamento} para cadastrar: ")
        dados_do_medicamento = {"nome":nome_medicamento, "Categoria":categoria_medicamento, "ativo":True}
        medicamentos.append(dados_do_medicamento)
        print(f" O mediacamento {nome_medicamento} foi cadastrado com sucesso\n")

        retorna_menu()
        

    def listar_medicamentos():
        exibir_subtitulo("Lista de medicamentos cadastrados")
        for medicamento in medicamentos:
            nome_medicamento = medicamento["nome"]
            categoria_medicamento = medicamento["Categoria"]
            ativo = medicamento["ativo"]
            print(f" - {nome_medicamento} | {categoria_medicamento} | {ativo}")

        retorna_menu()


    def finalizar_programa():
        os.system("cls") 
        print("Finalizando o programa\n") 

    def opcao_invalida():
        print("Esse caracter não é permitido")
        input("Aperte qualquer tecla para voltar")
        main()  

    try:

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastra_medicamentos()
        elif opcao_escolhida == 2:
            listar_medicamentos()
        elif opcao_escolhida == 3:
            print("Você escolheu Ativar Estoque")
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()