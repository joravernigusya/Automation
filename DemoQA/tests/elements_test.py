import time
import pytest
from DemoQA.pages.elements_page import \
    (TextBoxPage,
     CheckBoxPage,
     RadioButtonPage,
     ButtonsPage
     )


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/text-box",
            заполняет все поля на странице, проверяет заполнение формы и
            сверяет заполненные данные с данными, которые получились на выходе.
            """
            # Входные данные
            full_name = "Yan"
            email = "yan@gmail.com"
            current_address = "Msw"
            permanent_address = "Msw"

            # Инициализация страницы
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            # Заполнение полей формы
            text_box_page.set_value(text_box_page.FULL_NAME, full_name)
            text_box_page.set_value(text_box_page.EMAIL, email)
            text_box_page.set_value(text_box_page.CURRENT_ADDRESS,
                                    current_address)
            text_box_page.set_value(text_box_page.PERMANENT_ADDRESS,
                                    permanent_address)
            text_box_page.element_is_visible(text_box_page.SUBMIT).click()

            # Получение заполненных данных
            (
                output_name,
                output_email,
                output_cur_addr,
                output_per_addr,
            ) = text_box_page.check_filled_form()

            # Проверка заполненных данных
            assert output_name == "Name:" + full_name, "Имя не совпадает"
            assert output_email == "Email:" + email, "Почта не совпадает"
            assert (
                    output_cur_addr.strip() == "Current Address :" + current_address
            ), "Текущий адрес не совпадает"
            assert (
                    output_per_addr.strip() == "Permananet Address :" + permanent_address
            ), "Постоянный адрес не совпадает"

    class TestCheckBox:
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
            time.sleep(5)
            assert input_checkbox == output_result, "Чекбоксы не были выбраны"

    class TestRadioButton:
        def test_radio_button(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/radio-button" и
            проверяет функциональность радиокнопок.
            """
            radio_button_page = RadioButtonPage(driver,
                                                "https://demoqa.com/radio-button")
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
            assert output_impressive == "Impressive", \
                "'Impressive' was not selected"
            assert output_no == "No", "'No' was not selected"

    class TestButtonsPage:
        def test_different_click_on_the_buttons(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/buttons" и
            проверяет корректность работы кнопок.
            """
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double_text = button_page.click_on_double_button()
            right_text = button_page.click_on_right_click_button()
            click_text = button_page.click_on_click_me_button()
            assert double_text == "You have done a double click", \
                "The double click button was not pressed"
            assert right_text == "You have done a right click", \
                "The right click button was not pressed"
            assert click_text == "You have done a dynamic click", \
                "The dynamic click button was not pressed"
