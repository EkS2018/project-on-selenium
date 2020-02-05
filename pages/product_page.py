from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time

class ProductPage(BasePage):
    def find_and_click_button_1(self):
        button_1 = self.browser.find_element_by_class_name(ProductPageLocators.button_1_class)
        button_1.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def compare_name_and_price_of_goods(self):
        time.sleep(1)
        name_of_product = self.browser.find_element_by_tag_name(ProductPageLocators.tag_name).text
        price = self.browser.find_element_by_xpath(ProductPageLocators.xpath_of_price).text
        message = self.browser.find_element_by_xpath(ProductPageLocators.xpath_of_message).text
        price_2 = self.browser.find_element_by_xpath(ProductPageLocators.xpath_of_message_2).text
        assert (name_of_product == message and price == price_2), "product name or price do not match"

    
