
import datetime
from data.dados import playlist, contador_id


def adicionar_musica(titulo, artista, prazo_final=None, urgencia=False):
    global contador_id
    musica = {
        "id": contador_id,
        "titulo": titulo,
        "artista": artista,
        "data_inclusao": datetime.datetime.now().strftime("%d/%m/%Y"),
        "status": "Pendente",
        "prazo_final": prazo_final,
        "urgencia": urgencia
    }
    playlist.append(musica)
    contador_id += 1
    print(f"Música '{titulo}' adicionada na playlist!")


def listar_musicas():
    if not playlist:
        print("A playlist está vazia! Adicione músicas você goste")
        return

    print("\n--- Playlist Loopify ---")
    for musica in playlist:
        print(f"[{musica['id']}] {musica['titulo']} - {musica['artista']} | "
              f"Status: {musica['status']} | "
              f"Urgente: {'Sim' if musica['urgencia'] else 'Não'} | "
              f"Prazo: {musica['prazo_final'] if musica['prazo_final'] else '---'}")
    print("------------------------\n")


def marcar_como_tocada(id_musica):
    for musica in playlist:
        if musica["id"] == id_musica:
            musica["status"] = "Tocada"
            print(f"Música '{musica['titulo']}' foi marcada como tocada!")
            return
    print("Música não encontrada!")


def remover_musica(id_musica):
    for musica in playlist:
        if musica["id"] == id_musica:
            playlist.remove(musica)
            print(f" Música '{musica['titulo']}' removida da playlist!")
            return
    print("Música não encontrada!")
