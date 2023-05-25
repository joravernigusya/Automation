import base64
import os
import random

import allure
import requests
from selenium.webdriver.common.by import By

from DemoQA.utils.generator import generated_person, generated_file
from DemoQA.locators.elements_page_locators import (
    TextBoxPageLocators,
    CheckBoxLocators,
    RadioButtonPageLocators,
    ButtonsPageLocators,
    WebTableLocators,
    LinksPageLocators,
    UploadAndDownloadPageLocators
)
from DemoQA.pages.base_page import BasePage


class TextBoxPage(BasePage, TextBoxPageLocators):
    """
    класс TextBoxPage наследуется от BasePage и предоставляет методы для
    заполнения полей формы и проверки правильности заполнения формы
    """

    def get_attribute(self, locator, attribute_name):
        """
        Метод получает значение заданного атрибута элемента, заданного
        локатором.
        """
        element = self.element_is_visible(locator)
        return element.get_attribute(attribute_name)

    @allure.step("Fill in all fields")
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

    @allure.step('check filled form')
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
    @allure.step('open full list')
    def open_full_list(self):
        # Метод раскрывает полный список чекбоксов на странице.
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
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

    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        # Метод возвращает список выбранных чекбоксов.
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.',
                                                                     '').lower()

    @allure.step('get output result')
    def get_out_put_result(self):
        # Метод возвращает список результатов вывода.
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage, RadioButtonPageLocators):
    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self, choice):
        """
        Метод для щелчка по радиокнопке на странице.
        """
        choices = {'yes': self.YES_RADIO_BUTTON,
                   'impressive': self.IMPRESSIVE_RADIO_BUTTON,
                   'no': self.NO_RADIO_BUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step('get output result')
    def get_output_result(self):
        """
        Метод для получения результата вывода на странице.
        """
        return self.element_is_present(self.OUTPUT_RESULT).text


class ButtonsPage(BasePage, ButtonsPageLocators):
    @allure.step('click on double button')
    def click_on_double_button(self):
        # Метод производит двойной клик на элементе, который является
        # видимым на странице.
        self.double_click(
            self.element_is_visible(self.DOUBLE_BUTTON))
        return self.check_clicked_on_the_button(self.SUCCESS_DOUBLE)

    @allure.step('click on right click button')
    def click_on_right_click_button(self):
        # Метод производит клик правой кнопкой мыши на элементе, который
        # является видимым на странице.
        self.right_click(
            self.element_is_visible(self.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.SUCCESS_RIGHT)

    @allure.step("click on right 'click me' button")
    def click_on_click_me_button(self):
        # Метод производит клик на элементе, который является видимым на
        # странице.
        self.element_is_visible(self.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.SUCCESS_CLICK_ME)

    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, button_locator):
        # Метод проверяет, был ли произведен клик на кнопке с указанным
        # локатором и возвращает текст, который содержится в этой кнопке.
        return self.element_is_present(button_locator).text


class WebTablePage(BasePage, WebTableLocators):
    @allure.step('add new person')
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
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(
                department)
            self.element_is_visible(self.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary),
                    department]

    @allure.step('check added people')
    def check_new_added_person(self):
        # Метод для получения списка новых добавленных пользователей.
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('find some person')
    def search_some_person(self, key_word):
        # Метод для поиска пользователя по заданному ключевому слову.
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check found person')
    def check_search_person(self):
        # Метод для получения данных найденного пользователя.
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element("xpath",
                                         "//div[@class='rt-tr-group']")
        return row.text.splitlines()

    @allure.step('update person information')
    def update_person_info(self):
        # Метод получает данные о человеке из генератора "generated_person()",
        # затем обновляет возраст этого человека на странице таблицы и
        # возвращает обновленный возраст в виде строки.
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.UPDATE_BUTTON).click()
        self.element_is_visible(self.AGE_INPUT).clear()
        self.element_is_visible(self.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.SUBMIT).click()
        return str(age)

    @allure.step('delete person')
    def delete_person(self):
        #  Метод удаляет человека из таблицы.
        self.element_is_visible(self.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        # Метод проверяет, был ли удален человек из таблицы.
        return self.element_is_present(self.NO_ROWS_FOUND).text

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        # Метод проверяет, сколько строк отображается на каждой странице
        # таблицы, изменяя количество строк на каждой странице с помощью
        # выпадающего списка на странице и подсчитывая количество строк.
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_present(self.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(
                (By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        # Метод проверяет количество строк на текущей странице таблицы.
        list_rows = self.elements_are_present(self.FULL_PEOPLE_LIST)
        return len(list_rows)

    @allure.step('remove footer')
    def remove_footer(self):
        # Метод скрывает футер на странице веб-таблицы.
        self.driver.execute_script(
            "document.getElementsByTagName('footer')[0].remove();")

    @allure.step('remove fixedban')
    def remove_fixedban(self):
        # Метод скрывает фиксированную панель на странице таблицы.
        self.driver.execute_script(
            "document.getElementById('fixedban').style.display = 'none'")


class LinksPage(BasePage, LinksPageLocators):
    @allure.step('check simple link')
    def check_new_tab_simple_link(self):
        # Метод проверяет простую ссылку на веб-странице.
        simple_link = self.element_is_visible(self.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('check broken link')
    def check_broken_link(self, url):
        # Метод проверяет нерабочую ссылку на веб-странице.
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage, UploadAndDownloadPageLocators):
    @allure.step('upload file')
    # Метод используется для загрузки файла на веб-страницу.
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('download file')
    # Метод используется для скачивания файла с веб-страницы.
    def download_file(self):
        link = self.element_is_present(self.DOWNLOAD_FILE).get_attribute(
            'href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\Yan\Desktop\PythonAutomation\filetest' \
                         rf'{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file
