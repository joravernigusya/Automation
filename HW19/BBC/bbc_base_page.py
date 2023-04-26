from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BBCBasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator):
        return wait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
