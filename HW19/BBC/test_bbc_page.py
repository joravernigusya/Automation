from bbc_page_locators import BBCPageLocators
from HW19.BBC.bbc_base_page import BBCBasePage
import pytest


class TestBBC(BBCPageLocators):
    def test_first_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.PROMO_IMAGE_CSS)
        assert element.is_displayed()

    def test_first_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.PROMO_IMAGE_XPATH)
        assert element.is_displayed()

    def test_second_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.HOME_PAGE_BLOCK_CSS)
        assert element.is_displayed()

    def test_second_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.HOME_PAGE_BLOCK_XPATH)
        assert element.is_displayed()

    def test_third_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.SPORT_BLOCK_CSS)
        assert element.is_displayed()

    def test_third_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.SPORT_BLOCK_XPATH)
        assert element.is_displayed()
