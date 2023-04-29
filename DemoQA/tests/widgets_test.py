from DemoQA.pages.widgets_page import MenuPage


class TestMenuPage:
    def test_menu_items(self, driver):
        """
        Тест открывает веб-страницу с меню, проверяет наличие элементов меню и
        сравнивает полученные данные с ожидаемым списком значений
        """
        menu_page = MenuPage(driver, "https://demoqa.com/menu")
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item',
                        'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2',
                        'Main Item 3']
