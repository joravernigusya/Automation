from selenium.webdriver.common.by import By


class BBCPageLocators:
    PROMO_IMAGE_CSS = (By.CSS_SELECTOR, 'gel-2/3@m gs-u-display-block')
    PROMO_IMAGE_XPATH = (
        By.XPATH,
        '//*[@id="u4853366156481725"]/div/div/div/div[1]/div/div/div[2]')
    HOME_PAGE_BLOCK_CSS = (By.CSS_SELECTOR, 'orb-nav-section orb-nav-blocks')
    HOME_PAGE_BLOCK_XPATH = (By.XPATH, '//*[@id="homepage-link"]')
    SPORT_BLOCK_CSS = (By.CSS_SELECTOR, '.orb-nav-sport')
    SPORT_BLOCK_XPATH = (By.XPATH, '//*[@id="orb-header"]/div/nav[2]/ul/li[3]')
