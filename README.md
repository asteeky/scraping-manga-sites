# Meus Scripts de Download

Este repositório contém scripts para baixar conteúdo de diferentes sites.

## TSUKI MANGAS (Descontinuado)

Script para baixar capítulos de mangá do antigo site Tsuki Mangas.

**Atenção:** Este script está descontinuado devido à desativação do site Tsuki Mangas.

### Pré-requisitos

* Python 3.9.13 (tem que ser esta versão ou inferior)
* [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

### Bibliotecas Necessárias

* selenium
* beautifulsoup4
* requests

### Instalação das Dependências

```bash
pip install selenium beautifulsoup4 requests undetected-chromedriver
```

# Downloader de Capítulos de Mangá (nekotoons.site)

Este script Python foi projetado para baixar todas as imagens de um capítulo de mangá específico do site `nekotoons.site` e salvá-las em uma pasta local.

## Funcionalidades

* Baixa imagens de uma URL de capítulo fornecida.
* Cria uma pasta nomeada com o identificador do capítulo (ex: `capitulo_811`) para armazenar as imagens.
* Filtra e baixa apenas as imagens relevantes do conteúdo do mangá.
* Salva as imagens em formato `.jpg`.

## Pré-requisitos

Antes de executar o script, você precisará ter o Python instalado em seu sistema. Além disso, são necessárias as seguintes bibliotecas Python:

* `requests`: Para fazer requisições HTTP.
* `beautifulsoup4`: Para fazer o parsing do HTML da página.

## Instalação das Dependências

Você pode instalar as bibliotecas necessárias usando o pip:

```bash
pip install requests beautifulsoup4
``` 

