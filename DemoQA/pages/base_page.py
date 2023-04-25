from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """
    Класс определяет базовую страницу, которая содержит методы для работы с
    веб-элементами
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Функция проверяет, что элемент, заданный локатором, видим на странице.
        :param locator: локатор элемента на странцие
        :param timeout: время ожидания, в течение которого выполняется поиск
        элемента
        :return: элемент, если он найден и видимый на странице
        """
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def elements_are_visible(self, locator, timeout=5):
        """
        Функция проверяет, что все элементы, заданные локатором, видимы на
        странице.
        :param locator: локатор элементов на странице
        :param timeout: время ожидания, в течение которого выполняется поиск
        элементов
        :return: список элементов, если они найдены и видимы на странице
        """
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=5):
        """
        Функция проверяет наличие элемента на странице.
        :param locator: локатор элемента на странице
        :param timeout: время ожидания, в течение которого выполняется поиск
        элементов
        :return: элемент, если он присутствует на странице
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Функция проверяет наличие нескольких элементов на странице
        :param locator: локатор элемента на странице
        :param timeout: время ожидания, в течение которого выполняется поиск
        элементов
        :return: cписок элементов, если они присутствуют на странице
        """
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def elements_is_not_visible(self, locator, timeout=5):
        """
        Функция проверяет, что элемент не отображается на странице
        :param locator: локатор элемента на странице
        :param timeout: время ожидания, в течение которого выполняется поиск
        элементов
        :return: True, если элемент не отображается на странице, иначе
        генерируется исключение
        """
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def elements_is_clickable(self, locator, timeout=5):
        """
        Функция проверяет, что элемент можно кликнуть
        :param locator: локатор элемента на странице
        :param timeout: время ожидания, в течение которого выполняется поиск
        элементов
        :return: элемент, если он кликабелен, иначе генерируется исключение
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Функция используется для прокрутки страницы к указанному элементу
        :param element:  элемент, к которому нужно прокрутить страницу
        :return: не возвращает никакого значения
        """
        self.driver.execute_script("argument[0].scrollIntoView;", element)
