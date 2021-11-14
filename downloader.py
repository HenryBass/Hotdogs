from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

imgmax = 100
delay = 0.1

urls = []

Path = "D:\Hotdog Scraping\chromedriver.exe"

dogno = 0
wd = webdriver.Chrome(Path)

def scroll_down(wd):
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        image = image.resize((224, 224))
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success - " + url)
    except Exception as e:
        print('FAILED -', e)



url = "https://www.google.com/search?q=hotdog&tbm=isch&tbs=il:cl&hl=en&sa=X&ved=0CAAQ1vwEahcKEwj4xKSp6pb0AhUAAAAAHQAAAAAQAg&biw=1903&bih=929"
wd.get(url)

for i in range(0, 100):
    scroll_down(wd)

hotdogs = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

for hotdog in hotdogs:
    if hotdog.get_attribute('src') in urls:
        break

    if hotdog.get_attribute('src') and 'http' in hotdog.get_attribute('src'):
        urls.append(hotdog.get_attribute('src'))
        print(f"Found {len(urls)}")
    scroll_down(wd)

for i in urls:
    download_image("D:/Hotdog Scraping/CCHotdogs/" , i, "Hotdog#" + str(dogno) + ".jpg")
    dogno+=1

wd.quit()