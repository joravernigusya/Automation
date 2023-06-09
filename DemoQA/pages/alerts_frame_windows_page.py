import random
import time

import allure
from selenium.common import UnexpectedAlertPresentException

from DemoQA.locators.alerts_frame_windows_locators import \
    BrowserWindowsPageLocators, AlertsPageLocators
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


class AlertsPage(BasePage, AlertsPageLocators):

    @allure.step('get text from alert')
    def check_see_alert(self):
        # Метод получает текст из оповещения.
        self.element_is_visible(self.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_alert_appear_5_sec(self):
        # Метод проверяет появление оповещения через 5 секунд.
        self.element_is_visible(
            self.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    @allure.step('check confirm alert')
    def check_confirm_alert(self):
        # Метод проверяет оповещение с подтверждением.
        self.element_is_visible(self.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(
            self.CONFIRM_RESULT).text
        return text_result

    @allure.step('check prompt alert')
    def check_prompt_alert(self):
        # Метод проверяет оповещение с запросом.
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.PROMPT_RESULT).text
        return text, text_result
