from DemoQA.pages.base_page import BasePage
from DemoQA.locators.widgets_page_locators import MenuPageLocators


class MenuPage(BasePage, MenuPageLocators):
    def check_menu(self):
        # Метод выполняет проверку пунктов меню на веб-странице.
        menu_item_list = self.elements_are_present(self.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
