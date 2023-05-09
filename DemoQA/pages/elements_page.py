import random

from DemoQA.generator.generator import generated_person
from DemoQA.locators.elements_page_locators import (
    TextBoxPageLocators,
    CheckBoxLocators,
    RadioButtonPageLocators,
    ButtonsPageLocators,
    WebTableLocators
)
from DemoQA.pages.base_page import BasePage


class TextBoxPage(BasePage, TextBoxPageLocators):
    """
    класс TextBoxPage наследуется от BasePage и предоставляет методы для
    заполнения полей формы и проверки правильности заполнения формы
    """

    def set_value(self, locator, value):
        """
        Метод устанавливает значение атрибута value для элемента, заданного
        локатором.
        """
        element = self.element_is_visible(locator)
        self.driver.execute_script(f"arguments[0].value = '{value}';", element)

    def get_attribute(self, locator, attribute_name):
        """
        Метод получает значение заданного атрибута элемента, заданного
        локатором.
        """
        element = self.element_is_visible(locator)
        return element.get_attribute(attribute_name)

    def fill_all_fields(self):
        """
        Метод заполняет все поля на странице веб-формы и отправляет ее.
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.EMAIL).send_keys(email)
        self.element_is_visible(
            self.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(
            self.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """
        Метод проверяет, заполнены ли все поля формы. Возвращает значения
        полей ФИО, электронной почты, текущего адреса и постоянного адреса.
        """
        full_name = \
            self.element_is_present(self.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.CREATED_EMAIL).text.split(':')[1]
        current_address = \
            self.element_is_present(self.CREATED_CURRENT_ADDRESS).text.split(
                ':')[1]
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


class RadioButtonPage(BasePage, RadioButtonPageLocators):
    def click_on_the_radio_button(self, choice):
        """
        Метод для щелчка по радиокнопке на странице.
        """
        choices = {'yes': self.YES_RADIO_BUTTON,
                   'impressive': self.IMPRESSIVE_RADIO_BUTTON,
                   'no': self.NO_RADIO_BUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        """
        Метод для получения результата вывода на странице.
        """
        return self.element_is_present(self.OUTPUT_RESULT).text


class ButtonsPage(BasePage, ButtonsPageLocators):

    def click_on_double_button(self):
        # Метод производит двойной клик на элементе, который является
        # видимым на странице.
        self.action_double_click(
            self.element_is_visible(self.DOUBLE_BUTTON))
        return self.check_clicked_on_the_button(self.SUCCESS_DOUBLE)

    def click_on_right_click_button(self):
        # Метод производит клик правой кнопкой мыши на элементе, который
        # является видимым на странице.
        self.action_right_click(
            self.element_is_visible(self.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.SUCCESS_RIGHT)

    def click_on_click_me_button(self):
        # Метод производит клик на элементе, который является видимым на
        # странице.
        self.element_is_visible(self.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, button_locator):
        # Метод проверяет, был ли произведен клик на кнопке с указанным
        # локатором и возвращает текст, который содержится в этой кнопке.
        return self.element_is_present(button_locator).text


class WebTablePage(BasePage, WebTableLocators):
    def add_new_person(self):
        # Метод добавляет новые записи в таблицу на странцие
        # https://demoqa.com/webtables.
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary),
                    department]

    def check_new_added_person(self):
        # Метод для получения списка новых добавленных пользователей.
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        # Метод для поиска пользователя по заданному ключевому слову.
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        # Метод для получения данных найденного пользователя.
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element("xpath", "//div[@class='rt-tr-group']")
        return row.text.splitlines()


