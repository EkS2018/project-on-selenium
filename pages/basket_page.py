from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def find_and_click_button_2(self):
        button_2 = self.browser.find_element_by_class_name(BasketPageLocators.button_2_class)
        button_2.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.XPATH_OF_MESSAGE_3), "message is presented"

    def should_not_be_success_message_2(self):
        assert self.is_disappeared(*BasketPageLocators.XPATH_OF_MESSAGE_3), "message is presented"

       

        

