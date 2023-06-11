import random
import time

import allure
from selenium.common import UnexpectedAlertPresentException

from DemoQA.locators.alerts_frame_windows_locators import \
    BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators
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


class FramesPage(BasePage, FramesPageLocators):
    @allure.step('check frame')
    # Метод проверяет фрейм.
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

class NestedFramesPage(BasePage, NestedFramesPageLocators):
    @allure.step('check nested frame')
    # Метод проверяет вложенный фрейм.
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.PARENT_TEXT).text
        child_frame = self.element_is_present(self.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.CHILD_TEXT).text
        return parent_text, child_text
