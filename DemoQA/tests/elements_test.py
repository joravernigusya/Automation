import time
import random

import allure

from DemoQA.pages.elements_page import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonPage,
    ButtonsPage,
    WebTablePage,
    LinksPage,
    UploadAndDownloadPage,
    DynamicPropertiesPage
)


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/text-box",
            заполняет все поля на странице, проверяет заполнение формы и
            сверяет заполненные данные с данными, которые получились на выходе.
            """
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            (
                full_name,
                email,
                current_address,
                permanent_address,
            ) = text_box_page.fill_all_fields()
            (
                output_name,
                output_email,
                output_cur_addr,
                output_per_addr,
            ) = text_box_page.check_filled_form()
            time.sleep(10)
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_cur_addr, (
                "The current address " "does not match"
            )
            assert (
                    "Permananet Address :" + permanent_address ==
                    output_per_addr
            ), "The permanent address does not match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/text-box" и
            проверяет функциональность чекбоксов на веб-странице.
            """
            check_box_page = CheckBoxPage(driver,
                                          "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_out_put_result()
            assert input_checkbox == output_result, "Чекбоксы не были выбраны"

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radio_button(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/radio-button" и
            проверяет функциональность радиокнопок.
            """
            radio_button_page = RadioButtonPage(
                driver, "https://demoqa.com/radio-button"
            )
            radio_button_page.open()

            # Выбор кнопки "Yes" и проверка результата
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()

            # Выбор кнопки "Impressive" и проверка результата
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()

            # Выбор кнопки "No" и проверка результата
            radio_button_page.click_on_the_radio_button("no")
            output_no = radio_button_page.get_output_result()

            assert output_yes == "Yes", "'Yes' was not selected"
            assert output_impressive == "Impressive", "'Impressive' was not " \
                                                      "selected"
            assert output_no == "No", "'No' was not selected"

    @allure.feature('Buttons page')
    class TestButtonsPage:
        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_buttons(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/buttons" и
            проверяет корректность работы кнопок.
            """
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double_text = button_page.click_on_double_button()
            right_text = button_page.click_on_right_click_button()
            click_text = button_page.click_on_click_me_button()
            assert (
                    double_text == "You have done a double click"
            ), "The double click button was not pressed"
            assert (
                    right_text == "You have done a right click"
            ), "The right click button was not pressed"
            assert (
                    click_text == "You have done a dynamic click"
            ), "The dynamic click button was not pressed"

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.title('Сheck to add a person to the table')
        def test_web_table_add_person(self, driver):
            """
            Тест проверяет добавление новой записи в таблицу на странице
            https://demoqa.com/webtables и проверяет, что добавленная запись
            появляется в таблице.
            """
            web_table_page = WebTablePage(driver,
                                          "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "The person was not found in " \
                                               "the table"

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            """
            Тест проверяет поиск записи в таблице на странице
            https://demoqa.com/webtables и проверяет, что найденная запись
            присутствует в таблице.
            """
            web_table_page = WebTablePage(driver,
                                          "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "The person was not found in " \
                                             "the table"

        @allure.title('Checking to update the persons info in the table')
        def test_web_table_update_person_info(self, driver):
            # Тест проверяет обновление информации о человеке на странице
            # https://demoqa.com/webtables.
            web_table_page = WebTablePage(driver,
                                          "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "The person card has not been changed"

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person(self, driver):
            # Тест проверяет удаление человека на странице
            # https://demoqa.com/webtables из таблицы
            web_table_page = WebTablePage(driver,
                                          "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_count_row(self, driver):
            # Тест проверяет изменение количества отображаемых строк в
            # таблице на странице https://demoqa.com/webtables.
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_footer()
            web_table_page.remove_fixedban()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not ' \
                                   'been changed or has changed incorrectly'

    @allure.feature('Links page')
    class TestLinksPage:
        @allure.title('Checking the link')
        def test_check_link(self, driver):
            # Тест проверяет, что ссылка на странице https://demoqa.com/links
            # перенаправляет пользователя на правильный URL.
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link is broken or url is " \
                                             "incorrect"

        @allure.title('Checking the broken link')
        def test_broken_link(self, driver):
            # Тест проверяет, что нерабочая ссылка на странице
            # https://demoqa.com/links возвращает ожидаемый HTTP-статус.
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link(
                'https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or the status code " \
                                         "in son 400"

    @allure.feature('Upload and Download page')
    class TestUploadAndDownload:
        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            # Тест проверяет процесс загрузки файла.
            upload_download_page = UploadAndDownloadPage(driver,
                                                         'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "the file has not been uploaded"

        @allure.title('Check download file')
        def test_download_file(self, driver):
            # Тест проверяет процесс скачивания файла.
            upload_download_page = UploadAndDownloadPage(driver,
                                                         'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "the file has not been downloaded"

        @allure.feature('Dynamic properties page')
        class TestDynamicPropertiesPage:
            @allure.title('Check dynamic properties')
            def test_dynamic_properties(self, driver):
                # Тест проверяет функциональность динамических свойств
                # страницы, а именно изменение цвета элементов.
                dynamic_properties_page = DynamicPropertiesPage(driver,
                                                                'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open()
                color_before, color_after = dynamic_properties_page.check_changed_of_color()
                assert color_after != color_before, 'colors have not been changed'
