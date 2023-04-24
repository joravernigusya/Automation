from DemoQA.locators.elements_page_locators import TextBoxPageLocators
from DemoQA.pages.base_page import BasePage


class TextBoxPage(BasePage, TextBoxPageLocators):
    """
    класс TextBoxPage наследуется от BasePage и предоставляет методы для
    заполнения полей формы и проверки правильности заполнения формы
    """

    def fill_all_fields(self):
        """
        Функция заполняет все поля на странице веб-формы и отправляет ее
        """
        self.element_is_visible(self.FULL_NAME).send_keys("Yan")
        self.element_is_visible(self.EMAIL).send_keys("yan@gmail.com")
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys("Moscow")
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys("Moscow")
        self.element_is_visible(self.SUBMIT).click()

    def check_filled_form(self):
        """
        Функция проверяет, заполнены ли все поля формы. Возвращает значения
        полей ФИО, электронной почты, текущего адреса и постоянного адреса.
        """
        full_name = self.element_is_present(self.CREATED_FULL_NAME).text
        email = self.element_is_present(self.CREATED_EMAIL).text
        current_address = self.element_is_present(
            self.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(
            self.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address
