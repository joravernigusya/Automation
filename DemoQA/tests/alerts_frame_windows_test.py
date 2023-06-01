import allure

from DemoQA.pages.alerts_frame_windows_page import BrowserWindowsPage


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
