from DemoQA.pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            """
            Тест открывает страницу "https://demoqa.com/text-box",
            заполняет все поля на странице, проверяет заполнение формы и
            выводит результаты в командной строке.
            """
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields()
            (
                output_name,
                output_email,
                output_cur_addr,
                output_per_addr,
            ) = text_box_page.check_filled_form()
            print(
                f"{output_name}\n{output_email}\n{output_cur_addr}\n{output_per_addr}"
            )
