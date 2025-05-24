import os

import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin



# URL do capítulo desejado

capitulo_url = "https://nekotoons.site/manga/L%C3%A1grimas%2bSobre%2bFlores%2bMurchas/capitulo_811"




capitulo_id = capitulo_url.rstrip("/").split("/")[-1]


output_folder = os.path.join(r"coloque o diretório dos downloads", capitulo_id)

if not os.path.exists(output_folder):

    os.makedirs(output_folder)

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \

                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}


response = requests.get(capitulo_url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")

    img_tags = soup.find_all("img")

    

    count = 0

    for i, img in enumerate(img_tags):

        img_url = img.get("src")

        if not img_url:

            continue

       

        if "uploads" not in img_url:

            continue


        img_url = urljoin(capitulo_url, img_url)

        img_response = requests.get(img_url, headers=headers)

        if img_response.status_code == 200:

            count += 1

            img_filename = os.path.join(output_folder, f"image_{count}.jpg")

            with open(img_filename, "wb") as f:

                f.write(img_response.content)

            print(f"Imagem {count} do {capitulo_id} baixada com sucesso!")

        else:

            print(f"Falha ao baixar a imagem {i+1}")

else:

    print("Falha ao acessar a página do capítulo.")



print("Download completo.")
