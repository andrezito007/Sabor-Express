import os

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

def mostra_opcao():

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
            print("Você escolheu Cadastrar Medicamentos")
        elif opcao_escolhida == 2:
            print("Você escolheu Listar Medicamentos")
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
    mostra_opcao()

if __name__ == "__main__":
    main()