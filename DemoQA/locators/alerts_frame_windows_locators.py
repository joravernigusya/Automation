from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    # Локаторы элементов на странице Browser Windows.
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    # Локаторы элементов на странице https://demoqa.com/alerts.
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (
        By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    # Добавлены локаторы элементов на странице https://demoqa.com/frames.
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramesPageLocators:
    # Локаторы элементов на странице https://demoqa.com/nestedframes.
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    # Локаторы элементов на странице https://demoqa.com/modal-dialogs.
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (
        By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    TITLE_LARGE_MODAL = (
        By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
