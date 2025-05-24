# Meus Scripts de Download

Este repositório contém scripts para baixar conteúdo de diferentes sites.

---

## TSUKI MANGAS (Descontinuado)

Script para baixar capítulos de mangá do antigo site Tsuki Mangas.

**Atenção:** Este script está descontinuado devido à desativação do site Tsuki Mangas.

### Pré-requisitos

* Python 3.9.13 (tem que ser está versão ou uma inferior)
* É necessário instalar o `undetected-chromedriver`. Você pode encontrá-lo em: [https://github.com/ultrafunkamsterdam/undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

### Bibliotecas Necessárias

* selenium
* beautifulsoup4
* requests

### Instalação das Dependências

```bash
pip install selenium beautifulsoup4 requests undetected-chromedriver
Downloader de Capítulos de Mangá (nekotoons.site)
Este script Python foi projetado para baixar todas as imagens de um capítulo de mangá específico do site nekotoons.site e salvá-las em uma pasta local.

Funcionalidades
Baixa imagens de uma URL de capítulo fornecida.
Cria uma pasta nomeada com o identificador do capítulo (ex: capitulo_811) para armazenar as imagens.
Filtra e baixa apenas as imagens relevantes do conteúdo do mangá.
Salva as imagens em formato .jpg.
Pré-requisitos
Python instalado em seu sistema. (O texto original mencionava Python 3.9.13 para o Tsuki Mangas. Se esta for a versão para o Nekotoons também, você pode especificá-la aqui. Caso contrário, "Python instalado" é suficiente, e o usuário usará a versão que tiver configurada.)
Observação: A listagem original para Nekotoons incluiu selenium em uma parte, mas não na seção de instalação específica. Confirme se selenium é realmente necessário para este script.
Bibliotecas Necessárias
requests
beautifulsoup4 (Se selenium for necessário também para nekotoons.site, adicione-o aqui)
selenium
Instalação das Dependências
Você pode instalar as bibliotecas necessárias usando o pip:

Bash

pip install requests beautifulsoup4
(Se selenium também for necessário para nekotoons.site, o comando seria:)

Bash

pip install requests beautifulsoup4 selenium
