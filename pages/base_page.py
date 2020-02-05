from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CSS_SELECTOR_OF_MESSAGE_4), "basket is not empty"
        message_6 = self.browser.find_element(*BasketPageLocators.CSS_SELECTOR_OF_MESSAGE_6).text
        assert message_6.find("Ваша корзина пуста") != -1, "there is no message that the trash is empty"


    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
   
