import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import filecmp


def test_download_file():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://the-internet.herokuapp.com/download")

    # Ссылка на скачивание файла и его url
    download_link = driver.find_element("css selector", "a[href*='some-file.txt']")
    download_url = download_link.get_attribute("href")

    # Скачивание файла
    response = requests.get(download_url)

    # Сохранение скачанного файла
    downloaded_file_path = "C:/Users/Yan/Downloads/some-file.txt"
    with open(downloaded_file_path, "wb") as file:
        file.write(response.content)

    # Сравнение скачанного файла с базовым файлом
    base_file_path = "C:/Users/Yan/Downloads/base-file.txt"
    files_equal = filecmp.cmp(base_file_path, downloaded_file_path)

    # Результат сравнения
    if files_equal:
        print("Скачанный файл идентичен базовому файлу.")
    else:
        print("Скачанный файл отличается от базового файла.")

    driver.quit()
