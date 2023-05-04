from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Класс с локаторами элементов на странице ввода информации (пустые
    # заполненные поля формы).
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxLocators:
    # Класс содержит локаторы элементов на странице с чекбоксами.
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    # Класс, содержащий локаторы элементов страницы с радиокнопками.
    YES_RADIO_BUTTON = (
        By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (
        By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
