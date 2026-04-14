# Flickr Album Uploader

Aplicação desenvolvida em Python para fazer upload de fotos para o Flickr, através da API, e organizá-las automaticamente em álbuns a partir de um arquivo CSV.


## Requisitos

- Python 3
- Conta no Flickr


## Instale as dependências:

pip install flickrapi python-dotenv pandas


## Configuração

### Criar app no Flickr

Acesse: https://www.flickr.com/services/apps/create/apply

Crie uma aplicação não comercial

Copie a API Key e API Secret

Acesse: https://www.flickr.com/services/apps/by/me

Clique no app criado

Em editar fluxo de autenticação, selecione Aplicação Desktop


### Criar arquivo .env

FLICKR_API_KEY=seu_api_key
FLICKR_API_SECRET=seu_api_secret


### Criar arquivo CSV

album_title,album_directory
Viagem 2024,/caminho/para/fotos/viagem
Aniversario,/caminho/para/fotos/aniversario


### Uso

python upload_photos.py "nome_arquivo.csv"
