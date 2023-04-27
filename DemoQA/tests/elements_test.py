import time
import pytest
from DemoQA.pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/text-box",
            заполняет все поля на странице, проверяет заполнение формы и
            сверяет заполненные данные с данными, которые получились на выходе.
            """
            full_name = "Yan"
            email = "yan@gmail.com"
            current_address = "Msw"
            permanent_address = "Msw"
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields(
                full_name, email, current_address, permanent_address
            )
            (
                output_name,
                output_email,
                output_cur_addr,
                output_per_addr,
            ) = text_box_page.check_filled_form()
            assert output_name == "Name:" + full_name, "Имя не совпадает"
            assert output_email == "Email:" + email, "Почта не совпадает"
            assert (
                output_cur_addr == "Current Address :" + current_address
            ), "Текущий адрес не совпадает"
            assert (
                output_per_addr == "Permananet Address :" + permanent_address
            ), "Постоянный адрес не совпадает"

    class TestCheckBox:
        def test_check_box(self, driver):
            """
             Тест открывает страницу "https://demoqa.com/text-box" и
             проверяет функциональность чекбоксов на веб-странице.
            """
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_out_put_result()
            time.sleep(5)
            assert input_checkbox == output_result, "Чекбоксы не были выбраны"
