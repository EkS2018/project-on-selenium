from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_LINK = (By.ID, "login_link")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_ID = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_ID_1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_ID_2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON_CSS = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators():
    button_1_class = ('btn-add-to-basket')
    tag_name = ('h1')
    xpath_of_price = ('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    xpath_of_message = ('//*[@id="messages"]/div[1]/div/strong')
    xpath_of_message_2 = ('//*[@id="messages"]/div[3]/div/p[1]/strong')

class BasketPageLocators():
    button_2_class = ('btn-add-to-basket')
    XPATH_OF_MESSAGE_3 = (By.XPATH ,'//*[@id="messages"]/div[1]/div/strong')
    BASKET_LINK = (By.LINK_TEXT, 'Посмотреть корзину')
    CSS_SELECTOR_OF_MESSAGE_4 = (By.CSS_SELECTOR, "#id_form-0-quantity")
    CSS_SELECTOR_OF_MESSAGE_6 = (By.CSS_SELECTOR, "#content_inner > p")

    

    
