import yt_dlp
import os

def baixar_playlist_mp3(url_playlist):
    
    # Primeiro determina uma pasta para salvar as musicas baixadas
    # Depois verifica se ela ja existe e cria se nao existir
    pasta_destino = "musicas_baixadas"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Configurações do modulo yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best', # Baixa a melhor qualidade de audio possivel
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',   # Converte a musica/video para MP3
            'preferredquality': '192', # Bitrate de 192kbps - parece que é padrao e qualidade decente
        },

        {
                # força CBR em vez de VBR
                'key': 'FFmpegMetadata',
            }
        ],

        'restrictfilenames': True,
        # Onde salvar (na pasta destino) e o nome do arquivo quando salvo (preferencia titulo da música)
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'ignoreerrors': True, # Se der erro em um video, pula para o proximo para nao travar a execução
        'quiet': False,       # Mostra o progresso no terminal. Em true o progresso fica oculto
    }

    # Log para o usuario entender o inicio do processo
    print(f"Iniciando download da playlist: {url_playlist}")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_playlist])
        print("\nSucesso! Todas as músicas foram baixadas.")
    except Exception as e:
        print(f"\nOcorreu um erro geral: {e}")

if __name__ == "__main__":
    url = input("Cole a URL da playlist do YouTube aqui: ")
    baixar_playlist_mp3(url)
    