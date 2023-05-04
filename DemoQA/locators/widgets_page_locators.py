from selenium.webdriver.common.by import By


class MenuPageLocators:
    # Класс определяет локаторы элементов страницы, относящихся к меню.
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")
