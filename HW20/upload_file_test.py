from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_upload_file():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://the-internet.herokuapp.com/upload")

    # Находим кнопку для выбора файла.
    file_input = driver.find_element("css selector", "#file-upload")
    file_path = "C:/Users/Yan/Downloads/image.jpeg"

    # Загрузка файла.
    file_input.send_keys(file_path)

    # Находим кнопку "Upload" и кликаем на нее.
    upload_button = driver.find_element("css selector", "#file-submit")
    upload_button.click()

    # Проверка успешной загрузки файла и его отображения.
    uploaded_file = driver.find_element("css selector", "#uploaded-files")
    assert (
        uploaded_file.text == "image.jpeg"
    ), "Ошибка загрузки файла или файл не отображается на странице."

    driver.quit()
