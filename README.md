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

# Baixador de Capítulos do Nekotoons 🐾
Este script em Python permite baixar todas as imagens de um capítulo de mangá diretamente do site nekotoons.site, salvando-as em uma pasta local no seu computador.

 Como Funciona
O script:

Acessa a URL de um capítulo de mangá.

Encontra todas as tags <img> que contenham imagens do conteúdo do mangá.

Filtra apenas as imagens válidas (aquelas que possuem "uploads" no link).

Baixa e salva as imagens localmente com nomes como image_1.jpg, image_2.jpg, etc.

 Pré-requisitos
Python 3.x

Bibliotecas Python:

requests

beautifulsoup4

selenium

undetected-chromedriver (se quiser adaptar para scraping com proteção)

Instalação das Dependências
bash
Copiar
Editar
pip install selenium beautifulsoup4 requests undetected-chromedriver
🛠️Como Usar
Clone ou copie este script.

Modifique as seguintes variáveis no código:

python
Copiar
Editar
capitulo_url = "URL do capítulo que deseja baixar"
output_folder = os.path.join(r"coloque o diretório dos downloads", capitulo_id)
Exemplo:

python
Copiar
Editar
capitulo_url = "https://nekotoons.site/manga/Lágrimas+Sobre+Flores+Murchas/capitulo_811"
output_folder = os.path.join(r"C:\Users\SeuNome\Downloads\Mangas", capitulo_id)
Execute o script:

bash
Copiar
Editar
python baixar_capitulo.py
📂 Estrutura de Saída
As imagens serão salvas dentro de uma pasta com o nome do capítulo (ex: capitulo_811), dentro do diretório que você especificou.

⚠️ Aviso
Este script depende da estrutura atual do site nekotoons.site Mudanças no layout ou comportamento da página podem exigir ajustes no código.

