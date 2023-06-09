import allure

from DemoQA.pages.alerts_frame_windows_page import (
    BrowserWindowsPage,
    AlertsPage
)


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            # Тест проверяет, что новая вкладка успешно открывается на
            # странице браузера.
            browser_windows_page = BrowserWindowsPage(driver,
                                                      "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', \
                "the new tab has not opened or an incorrect tab has opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            # Тест проверяет, что новое окно успешно открывается на странице
            # браузера.
            browser_windows_page = BrowserWindowsPage(driver,
                                                      "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', \
                "the new window has not opened or an incorrect window has opened"

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            # Тест проверяет открытие оповещения.
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert did not show up"

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver):
            # Тест проверяет открытие оповещения через 5 секунд.
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', \
                "Alert did not show up"

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            # Тест проверяет открытие оповещения с подтверждением.
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Alert did not show up"

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            # Тест проверяет открытие оповещения с запросом.
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert did not show up"
