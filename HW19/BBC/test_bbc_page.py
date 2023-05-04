from bbc_page_locators import BBCPageLocators
from HW19.BBC.bbc_base_page import BBCBasePage
import pytest


class TestBBC(BBCPageLocators):
    def test_promo_image_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.PROMO_IMAGE_CSS)
        assert element.is_displayed()

    def test_promo_image_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.PROMO_IMAGE_XPATH)
        assert element.is_displayed()

    def test_home_page_block_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.HOME_PAGE_BLOCK_CSS)
        assert element.is_displayed()

    def test_home_page_block_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.HOME_PAGE_BLOCK_XPATH)
        assert element.is_displayed()

    def sport_block_element_css(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.SPORT_BLOCK_CSS)
        assert element.is_displayed()

    def sport_block_element_xpath(self, driver):
        page = BBCBasePage(driver, 'https://www.bbc.com/news')
        page.open_page()
        element = page.element_is_visible(self.SPORT_BLOCK_XPATH)
        assert element.is_displayed()
