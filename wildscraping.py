import undetected_chromedriver as uc  
from bs4 import BeautifulSoup
import time
import os
import requests

# Configura o driver
def start_driver():
    options = uc.ChromeOptions()
    options.headless = False  
    driver = uc.Chrome(options=options)
    return driver

def download_image(img_url, save_path):
    img_data = requests.get(img_url).content
    with open(save_path, 'wb') as handler:
        handler.write(img_data)
    print(f"Imagem salva em: {save_path}")

def scrape_images(url, download_folder):
    driver = start_driver()
    driver.get(url)

    time.sleep(5) 

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    img_tags = soup.find_all('img')

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for i, img in enumerate(img_tags):
        img_url = img.get('src')
        if img_url and img_url.startswith('http'):
            file_name = os.path.join(download_folder, f"imagem_{i}.jpg")
            download_image(img_url, file_name)

    driver.quit()

# URL of the website from where you want to download the images
url = 'https://exemple'

#Folder where the images will be saved
download_folder = 'C:/Users/xxx/Desktop/test'
scrape_images(url, download_folder)
