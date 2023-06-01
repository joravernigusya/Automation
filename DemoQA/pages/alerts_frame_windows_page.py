import allure

from DemoQA.locators.alerts_frame_windows_locators import \
    BrowserWindowsPageLocators
from DemoQA.pages.base_page import BasePage


class BrowserWindowsPage(BasePage, BrowserWindowsPageLocators):

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self):
        # Метод выполняет проверку открытия новой вкладки.
        self.element_is_visible(self.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.TITLE_NEW).text
        return text_title

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        # Метод выполняет проверку открытия нового окна.
        self.element_is_visible(self.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.TITLE_NEW).text
        return text_title
