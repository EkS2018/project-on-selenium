from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        registration_e_mail_new_user = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ID)
        registration_e_mail_new_user.send_keys(email)
        registration_password_new_user = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_ID_1)
        registration_password_new_user.send_keys(password)
        registration_password_new_user_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_ID_2)
        registration_password_new_user_repeat.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_CSS)
        registration_button.click()
