from DemoQA.locators.elements_page_locators import TextBoxPageLocators
from DemoQA.pages.base_page import BasePage


class TextBoxPage(BasePage):
    """
    класс TextBoxPage наследуется от BasePage и предоставляет методы для
    заполнения полей формы и проверки правильности заполнения формы
    """

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """
        Функция заполняет все поля на странице веб-формы и отправляет ее
        """
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Yan")
        self.element_is_visible(self.locators.EMAIL).send_keys("yan@gmail.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("Moscow")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("Moscow")
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_form(self):
        """
        Функция проверяет, заполнены ли все поля формы. Возвращает значения
        полей ФИО, электронной почты, текущего адреса и постоянного адреса.
        """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS
        ).text
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS
        ).text
        return full_name, email, current_address, permanent_address
