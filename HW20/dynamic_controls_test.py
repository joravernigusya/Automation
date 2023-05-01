from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_cd():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://the-internet.herokuapp.com/dynamic_controls")

    # Найти чекбокс.
    driver.find_element(By.XPATH, "//input[@type='checkbox']")

    # Нажать на кнопку "Remove".
    remove_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Remove')]"
    )
    remove_button.click()

    wait = WebDriverWait(driver, 10)

    # Дождаться надписи "It's gone!".
    wait.until(
        EC.invisibility_of_element_located(
            (By.XPATH, "// *[ @ id = 'message']"))
    )

    # Проверка, что чекбокс больше не отображается на странице.
    assert wait.until_not(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkbox"]'))
    )

    # Найти input
    input_field = driver.find_element(By.XPATH, "//input[@type='text']")

    # Проверка, что он input disabled
    assert not input_field.is_enabled()

    # Нажатие на кнопку "Enable"
    enable_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Enable')]"
    )
    enable_button.click()

    # Ожидание надписи “It's enabled!”
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))

    # Проверка, что input enabled
    assert input_field.is_enabled()

    driver.quit()
