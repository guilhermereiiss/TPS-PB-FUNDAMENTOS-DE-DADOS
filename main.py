from funcoes import adicionar_musica, listar_musicas, marcar_como_tocada, remover_musica
from data.db_connection import init_db
from data.auth import verificar_login

def login():
    print("\n=== Login Loopify ===")
    email = input("Email: ")
    password = input("Senha: ")
    return verificar_login(email, password)

def menu():
    while True:
        print("\n=== Loopify - Gerenciador de Playlist ===")
        print("1 - Adicionar música")
        print("2 - Listar músicas")
        print("3 - Marcar música como tocada")
        print("4 - Remover música")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da música: ")
            artista = input("Artista: ")
            prazo = input("Prazo final (DD/MM/AAAA) ou ENTER para ignorar: ")
            urgencia = input("É urgente ouvir? (s/n): ").lower() == "s"
            adicionar_musica(titulo, artista, prazo if prazo else None, urgencia)

        elif opcao == "2":
            listar_musicas()

        elif opcao == "3":
            listar_musicas()
            try:
                id_musica = int(input("ID da música a marcar como tocada: "))
                marcar_como_tocada(id_musica)
            except ValueError:
                print("ID inválido!")

        elif opcao == "4":
            listar_musicas()
            try:
                id_musica = int(input("ID da música a remover: "))
                remover_musica(id_musica)
            except ValueError:
                print(" ID inválido!")

        elif opcao == "5":
            print("Saindo do Loopify...")
            break

        else:
            print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    init_db()  
    success, _ = login()  
    if success:  
        menu()  
    else:
        print("Acesso negado. Encerrando o programa.")