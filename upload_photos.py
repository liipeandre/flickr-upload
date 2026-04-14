import os
import sys
import pandas

import apis.api_flickr as api_flickr


def main():

    print("")

    if len(sys.argv) != 2:
        print("Uso: python upload_photos.py <caminho_do_arquivo_csv>")
        print("Observacoes:")
        print("O arquivo csv deve ter as colunas: album_title, album_directory")
        print("O limite de requisicoes da Flickr API eh de 3600 requisicoes por hora"
              "Cada requisicao possui um delay de 2 segundos para não ultrapassar esse limite"
        )
        sys.exit(1)

    csv_file = sys.argv[1]

    if not os.path.exists(csv_file):
        print(f"Arquivo não encontrado: {csv_file}")
        sys.exit(1)

    dataframe = pandas.read_csv(csv_file)
    api_flickr.upload_photos(dataframe)


if __name__ == '__main__':
    main()
