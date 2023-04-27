import random
from DemoQA.locators.elements_page_locators import (
    TextBoxPageLocators,
    CheckBoxLocators
)
from DemoQA.pages.base_page import BasePage


class TextBoxPage(BasePage, TextBoxPageLocators):
    """
    класс TextBoxPage наследуется от BasePage и предоставляет методы для
    заполнения полей формы и проверки правильности заполнения формы
    """

    def fill_all_fields(self, full_name, email, current_address,
                        permanent_address):
        """
        Метод заполняет все поля на странице веб-формы и отправляет ее
        """
        self.element_is_visible(self.FULL_NAME).send_keys(
            full_name)
        self.element_is_visible(self.EMAIL).send_keys(email)
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(
            current_address)
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys(
            permanent_address)
        self.element_is_visible(self.SUBMIT).click()

    def check_filled_form(self):
        """
        Метод проверяет, заполнены ли все поля формы. Возвращает значения
        полей ФИО, электронной почты, текущего адреса и постоянного адреса.
        """
        full_name = self.element_is_present(self.CREATED_FULL_NAME).text
        email = self.element_is_present(self.CREATED_EMAIL).text
        current_address = self.element_is_present(
            self.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(
            self.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage, CheckBoxLocators):
    def open_full_list(self):
        # Метод раскрывает полный список чекбоксов на странице.
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        # Метод выбирает случайный чекбокс из списка.
        item_list = self.elements_are_visible(self.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        # Метод возвращает список выбранных чекбоксов.
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.',
                                                                     '').lower()

    def get_out_put_result(self):
        # Метод возвращает список результатов вывода.
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
